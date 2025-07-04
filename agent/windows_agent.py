import os
import subprocess
import json
import schedule 
import argparse
import requests
import time
import logging
from datetime import datetime, timedelta

# Defines format of the log
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
def push(payload, ip):
    try: 
        r = requests.post(ip, data=payload)
        r.raise_for_status()
    except requests.exceptions.RequestException as e:
        print(f"An error occured: {e}")

def scrap_log(ip):
        # Currently scrapes logs from windows, the past 25 events from newest to oldest
        # Format is json for easy parsing
        # rd:true just means reverse order to newest to oldest
        # Feel free to add more logs this is just an example
        cmd = [
        'wevtutil', 'qe', 'System', 
        '/c:25',
        '/rd:true',
        '/f:json' ]
        output = subprocess.run(cmd, capture_output=True, text=True)
        push(output, ip)
        return output

def arg_parse():
    parser = argparse.ArgumentParser(description="A simple siem windows agent, usage: ")
    parser.add_argument('-i', '--ip-to-forward', help='ip of the machine we want to forward data too', required=True)
    args = parser.parse_args()
    return args

def main():
    '''

    Here is how this is going to work:
        - Get data( Any data we can generate for example network data logs from zeek or  Windows Event Logs )
        - Push the data to the processor who can then organize the data, check for malicous activity etc
    '''
    args = arg_parse()    # Feel free to adjust push/scrape rate
    # Time current at 5 minutes per push
    push_rate = 5
    sleep_rate = 295 # 5 * 300 - 10 this is to reduce computational power a bit 
    output = schedule.every(push_rate).minutes.do(scrap_log(args.ip_to_forward))
    while True:
        schedule.run_pending()
        time.sleep(sleep_rate)
        
main()

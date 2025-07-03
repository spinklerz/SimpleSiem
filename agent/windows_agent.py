import os
import subprocess
import json
import schedule
import time
import logging
from datetime import datetime, timedelta

# Defines format of the log
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def scrap_log_and_push(cmd):
        # Currently scrapes logs from windows, the past 25 events from newest to oldest
        # Format is json for easy parsing
        # rd:true just means reverse order to newest to oldest
        cmd = [
        'wevtutil', 'qe', 'System', 
        '/c:25',
        '/rd:true',
        '/f:json' ]
        output = subprocess.run(cmd, capture_output=True, text)
        return output

def push_logs():

    pass
def main():
    '''

    Here is how this is going to work:
        - Get data( Any data we can generate for example network data logs from zeek or  Windows Event Logs )
        - Push the data to the processor who can then organize the data, check for malicous activity etc
    '''
    # Feel free to adjust push/scrape rate
    # Time current at 5 minutes per push
    push_rate = 5
    sleep_rate = 290 # 5 * 300 - 10 this is to reduce computational power a bit 
    output = schedule.every(rate).minutes.do(scrap_log_and_push)
    while True:
        schedule.run_pending()
        time.sleep(sleep_rate)
        
main()

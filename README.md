# SimpleSiem
This project is aimed towards building an easy to set up SIEM, with the goal of simplicity, effectiveness, and highly customizable. Something you can spin up in ~5-10 minutes by just running these Python scripts. 




## Architecture
* Python agent
* Python processor
* sqlite3 db to store data 
* Python dashboard




## MVP 

- The agent is able to forward data to the processor.
- The processor analyzes/cleans/forwards data to the dashboard. 
- The dashboard is able to receive the data and is able to give real-time statistics.
- Strictly starting with network data 
- Basic alerting email and Slack




## Future Plans

- SOAR implementation
- reliable auth from SIEM to endpoints 
- dashboard data pull/search/etc.. 

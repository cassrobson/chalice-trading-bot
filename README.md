# Chalice Trading Bot

Uses AWS Chalice to deploy the algorithm in a Ubuntu virtual environment. 
Insomnia server receives WebHook Alerts from TradingView's real time data service based on preset upper and lower limits (when price of stock crosses-up/crosses-down, buy or sell orders are placed by source code in the virtual environment to the Alpaca API/Broker software. 

Current takes profit at a 5% gain, and has a stop loss set at -2%. 

Attached are screenshots of the bot in action (deploying chalice, integration between Insomnia and TradingView webhook alerts)





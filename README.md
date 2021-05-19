# TOTO toolkit
TOTO is a legalized form of lottery sold in Singapore. This tool helps to generate TOTO numbers and 
also check the result for a given day. 

## Installing the dependencies

`pip install -r requirements.txt`

## Running the scripts

`export TELEGRAM_TOTO_KEY=<your telegram bot API key>` <br/>

`export CHAT_ID=<your personal chat id>` <br/>

`export TOTO_CHAT_ID=<your group chat id>`<br/>

The CHAT_ID is used to receive admin messages while the TOTO_CHAT_ID is the group chat
to broadcast the scraped information. <br/>

`python3 toto_scraper.py`

This will scrape for TOTO results of the DATE field in the code and send the results to the
group chat if it is found.

`python3 toto_generator.py`

This will generate N rows of random TOTO numbers combination.

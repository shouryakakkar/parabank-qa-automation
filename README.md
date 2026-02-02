\# ParaBank QA Automation Project



\## Tech Stack

\- Selenium + PyTest (UI Automation)

\- Postman + Newman (API Automation)

\- Jenkins (CI)

\- Docker (ParaBank)



\## Features Tested

\- Login (positive \& negative)

\- Open New Account

\- Transfer Funds

\- REST API validation



\## How to Run

1\. Start ParaBank locally

2\. Run UI tests:

&nbsp;  pytest automation/tests

3\. Run API tests:

&nbsp;  newman run api-tests/parabank.postman\_collection.json -e api-tests/parabank\_env.json




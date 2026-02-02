ParaBank – End-to-End QA Automation Framework
📌 Project Overview

This project demonstrates an end-to-end QA automation framework for a banking web application (ParaBank), covering UI automation, API testing, and CI/CD integration.
The framework validates critical banking workflows across frontend and backend layers, ensuring data consistency, reliability, and production readiness.

🏦 Business Domain

Banking / Financial Services

Tested workflows simulate real-world banking operations such as:

User authentication

Account management

Fund transfers

Transaction validation

🛠️ Tech Stack

UI Automation

Selenium WebDriver

PyTest

Page Object Model (POM)

API Automation

Postman

Newman

REST APIs

XML & JSON response handling

CI/CD

Jenkins (Pipeline-based execution)

HTML Test Reports

Test Management & Tracking

JIRA (Test cases & defect tracking)

Database Validation

SQL (Backend data validation using SELECT queries)

Other Tools

Git & GitHub

Docker (ParaBank local setup)

🧪 Test Coverage
UI Automation (Selenium)

Login (Positive & Negative Scenarios)

Open New Bank Account

Fund Transfer

Smoke, Sanity & Regression Test Suites

API Automation (Postman / Newman)

Login API (Authentication & session handling)

Get Accounts API

Transfer Funds API

Backend transaction validation

⚙️ Project Structure
parabank-qa-automation/
├── automation/
│   ├── pages/               # Page Object classes
│   ├── tests/               # PyTest test cases
│   ├── conftest.py           # WebDriver setup
│   └── requirements.txt
│
├── api-tests/
│   ├── parabank.postman_collection.json
│   └── parabank_env.json
│
├── Jenkinsfile               # CI pipeline
└── README.md

🚀 How to Run the Project
🔹 Prerequisites

Python 3.x

Node.js & npm

Docker

Jenkins

Chrome Browser

▶️ Start ParaBank (Docker)
docker run -d -p 8080:8080 parasoft/parabank


Application URL:

http://localhost:8080/parabank

▶️ Run UI Tests (Locally)
pip install -r automation/requirements.txt
pytest automation/tests --html=ui-report.html

▶️ Run API Tests (Locally)
newman run api-tests/parabank.postman_collection.json \
-e api-tests/parabank_env.json \
-r html --reporter-html-export api-report.html

🔄 CI/CD Pipeline (Jenkins)

Automated execution of UI and API tests

Dependency installation handled inside pipeline

HTML reports generated for each build

Pipeline Stages

Code Checkout

Environment Setup

UI Automation Execution

API Automation Execution

Report Publishing

📊 Reports

UI Automation Report (ui-report.html)

API Automation Report (api-report.html)

Reports are published automatically in Jenkins after each pipeline run.

🧠 Key Highlights

End-to-end validation across UI and backend layers

XML response parsing and environment variable chaining

SQL-based backend data validation

CI-ready automation framework

Banking domain-focused test scenarios

📈 Impact

Reduced manual regression effort by ~60%

Improved test stability using explicit waits and POM

Early detection of integration issues via CI execution

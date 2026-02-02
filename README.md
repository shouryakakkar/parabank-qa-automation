# ParaBank – End-to-End QA Automation Framework

![CI Status](https://img.shields.io/badge/build-passing-brightgreen)

## 📌 Project Overview
This project demonstrates an **end-to-end QA automation framework** for a banking web application (ParaBank), covering **UI automation, API testing, and CI/CD integration**.  
The framework validates critical banking workflows across **frontend and backend layers**, ensuring data consistency, reliability, and production readiness.

---

## 🏦 Business Domain
**Banking / Financial Services**

Tested workflows simulate real-world banking operations such as:
- User authentication
- Account management
- Fund transfers
- Transaction validation

---

## 🛠️ Tech Stack

**UI Automation**
- Selenium WebDriver
- PyTest
- Page Object Model (POM)

**API Automation**
- Postman
- Newman
- REST APIs
- XML & JSON response handling

**CI/CD**
- Jenkins (Pipeline-based execution)
- HTML Test Reports

**Test Management & Tracking**
- JIRA (Test cases & defect tracking)

**Database Validation**
- SQL (Backend data validation using SELECT queries)

**Other Tools**
- Git & GitHub
- Docker (ParaBank local setup)

---

## 🧪 Test Coverage

### UI Automation (Selenium)
- Login (Positive & Negative Scenarios)
- Open New Bank Account
- Fund Transfer
- Smoke, Sanity & Regression Test Suites

### API Automation (Postman / Newman)
- Login API (Authentication & session handling)
- Get Accounts API
- Transfer Funds API
- Backend transaction validation

---

## 📸 Screenshots

<img width="1919" height="786" alt="image" src="https://github.com/user-attachments/assets/9d70f8ec-baa1-4490-88ce-6ceb99e764b8" />


<img width="1896" height="1079" alt="image" src="https://github.com/user-attachments/assets/816b3bb5-aeae-45a8-a07a-c23981fa7a50" />

<img width="1919" height="1042" alt="image" src="https://github.com/user-attachments/assets/70bb158e-783f-497a-8f81-22d32aee3b79" />

<img width="1919" height="1079" alt="image" src="https://github.com/user-attachments/assets/9defe96c-8d29-4099-b3a4-32580d6b050f" />

<img width="1919" height="1079" alt="image" src="https://github.com/user-attachments/assets/bfffd7bc-57fa-4031-9ca9-c0aed1aad3b4" />




## ⚙️ Project Structure

```
parabank-qa-automation/
├── automation/
│   ├── pages/
│   ├── tests/
│   ├── conftest.py
│   └── requirements.txt
│
├── api-tests/
│   ├── parabank.postman_collection.json
│   └── parabank_env.json
│
├── Jenkinsfile
├── screenshots/
└── README.md
```

---

## 🚀 How to Run the Project

### ▶️ Start ParaBank (Docker)
```bash
docker run -d -p 8080:8080 parasoft/parabank
```

Application URL:
```
http://localhost:8080/parabank
```

---

### ▶️ Run UI Tests (Locally)
```bash
pip install -r automation/requirements.txt
pytest automation/tests --html=ui-report.html
```

---

### ▶️ Run API Tests (Locally)
```bash
newman run api-tests/parabank.postman_collection.json \
-e api-tests/parabank_env.json \
-r html --reporter-html-export api-report.html
```

---

## 🔄 CI/CD Pipeline (Jenkins)

- Automated execution of **UI and API tests**
- Dependency installation handled inside pipeline
- HTML reports generated for each build

---

## 📊 Reports
- UI Automation Report (`ui-report.html`)
- API Automation Report (`api-report.html`)

---

## 📈 Impact
- Reduced manual regression effort by ~60%
- Improved test stability using explicit waits and POM
- Early detection of integration issues via CI execution

---

## 📌 Author
**Shourya Kakkar**

**QA Automation Engineer**  
Tech Stack: Selenium | Postman | Python | Java | Jenkins | JIRA | SQL

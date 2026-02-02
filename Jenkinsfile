pipeline {
    agent any

    stages {

        stage('Checkout Code') {
            steps {
                checkout scm
            }
        }

        stage('Setup Python Env') {
            steps {
                bat '''
                python -m venv venv
                call venv\\Scripts\\activate
                pip install -r automation\\requirements.txt
                '''
            }
        }

        stage('Run UI Tests') {
            steps {
                bat '''
                call venv\\Scripts\\activate
                pytest automation\\tests --html=ui-report.html
                '''
            }
        }

        stage('Run API Tests') {
            steps {
                bat '''
                newman run api-tests\\parabank.postman_collection.json ^
                -e api-tests\\parabank_env.json ^
                -r html --reporter-html-export api-report.html
                '''
            }
        }
    }

    post {
        always {
            publishHTML(target: [
                reportName: 'UI Automation Report',
                reportDir: '.',
                reportFiles: 'ui-report.html'
            ])
            publishHTML(target: [
                reportName: 'API Automation Report',
                reportDir: '.',
                reportFiles: 'api-report.html'
            ])
        }
    }
}

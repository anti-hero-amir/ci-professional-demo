pipeline {
    agent any

    environment {
        IMAGE_NAME = "ci-professional-demo"
        VENV_DIR = "venv"
    }

    stages {

        stage('Checkout') {
            steps {
                checkout scm
            }
        }

        stage('Set Up Python Environment') {
            steps {
                sh """
                python3 -m venv ${VENV_DIR}
                . ${VENV_DIR}/bin/activate
                pip install --upgrade pip
                pip install -r requirements.txt
                """
            }
        }

        stage('Lint Code') {
            steps {
                sh """
                . ${VENV_DIR}/bin/activate
                flake8 app
                """
            }
        }

        stage('Run Tests') {
            steps {
                sh """
                . ${VENV_DIR}/bin/activate
                coverage run -m pytest
                coverage xml
                """
            }
        }

        stage('Build Docker Image') {
            steps {
                sh "docker build -t ${IMAGE_NAME}:${BUILD_NUMBER} ."
            }
        }
    }

    post {
        always {
            archiveArtifacts artifacts: '**/*.xml', allowEmptyArchive: true
        }
        success {
            echo '✅ Pipeline executed successfully!'
        }
        failure {
            echo '❌ Pipeline failed. Check logs.'
        }
    }
}

pipeline {
    agent any

    stages {
        stage('Build') {
            steps {
                echo 'Building...'
                sh 'pip install -r requirements.txt'
                // sh 'python manage.py test'
            }
        }

        stage('Deploy') {
            steps {
                echo 'Deploying...'
                sh 'python3 manage.py runserver 34.155.164.205:8000'
            }
        }
    }
}

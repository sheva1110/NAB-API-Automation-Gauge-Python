pipeline {
    agent { dockerfile true }
    stages {
        stage('Test') {
            steps {
                sh 'Start run API automation testing'
                gauge run specs -v
            }
        }
    }
}

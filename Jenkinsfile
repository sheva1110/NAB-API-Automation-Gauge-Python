pipeline {
    agent { dockerfile true }
    stages {
        stage('Test') {
            steps {
                sh 'Start run NAB API automation testing'
                gauge run specs -v
            }
        }
    }
}

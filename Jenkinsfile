pipeline {
    agent any
    stages {
        stage('build'){
            steps{
                echo 'docker build'
                sh '''
                docker build -t zapper0703/multi-container:client ./client
                docker build -t zapper0703/multi-container:api ./server
                docker build -t zapper0703/multi-container:worker ./worker
                docker build -t zapper0703/multi-container:nginx-route ./nginx
                '''
            }
        }
        stage('push'){
            steps {
                withDockerRegistry([credentialsId: "ad602a39-f4eb-4fc2-9a25-9c1f531c4702", url: ""]){
                    echo 'docker hub push'
                    sh '''
                    docker push 
                    '''
                }
            }
        }
    }
}
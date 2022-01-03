node {
    stage("Checkout SCM"){
        checkout([$class: 'GitSCM', branches: [[name: '*/master']], userRemoteConfigs: [[url: 'https://github.com/shahar5/wog']]])
    }
    stage("Pull staged container from DockHub repo"){
        docker.withRegistry('https://registry.hub.docker.com') {
            image = docker.image('ricksanchezz/wog-flask-stage')
            image.pull()
        }
    }
    stage("Run container"){
        image.run('--name staged -p 8777:5000')
    }
    stage("selenium"){
        try{
            bat (script: "python e2e.py", returnStdout: true).trim()
    } catch (Exception e) {
            echo 'Exception occurred: ' + e.toString()
        }
    }
    stage("Finalize"){
        withCredentials([usernameColonPassword(credentialsId: 'docker-hub', variable: 'docker-hub')]) {
        docker.withRegistry("https://registry.hub.docker.com", "docker-hub") {
            bat "docker image tag ricksanchezz/wog-flask-stage:latest ricksanchezz/wog-flask-prod:${currentBuild.number}"
            bat "docker push ricksanchezz/wog-flask-prod:${currentBuild.number}"
            bat "docker stop staged"
            bat "docker rm staged"
            }
        }
    }
}
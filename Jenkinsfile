properties([buildDiscarder(logRotator(numToKeepStr: '3'))])
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
        stdout = bat(script: "python ./tests/e2e.py", returnStdout: true).trim()
        result = stdout.readLines().drop(1).join(" ")
        if (result != "0"){
            bat "docker stop staged"
            bat "docker rm staged"
            error("Selenium test had failed")
        }
    }
    stage("Finalize"){
        withCredentials([usernameColonPassword(credentialsId: 'docker-hub', variable: 'docker-hub')]) {
        docker.withRegistry("https://registry.hub.docker.com", "docker-hub") {
            bat "docker image tag ricksanchezz/wog-flask-stage:latest ricksanchezz/wog-flask-prod:latest"
            bat "docker push ricksanchezz/wog-flask-prod:latest"
            bat "docker stop staged"
            bat "docker rm staged"
            }
        }
    }
}
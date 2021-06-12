pipeline {
  agent any
  stages {
    stage('Inicio_environment') {
      steps {
        echo 'Iniciando construcción de proyectos'
        sh 'env'
      }
    }

    stage('Docker Env') {
      parallel {
        stage('Docker Env') {
          steps {
            sh 'docker -v'
          }
        }

        stage('Images from docker') {
          steps {
            sh 'docker images'
          }
        }

      }
    }

  }
}
pipeline {
  agent any

  stages {
    stage('Build') {
      steps {
        sh 'python3 setup.py build'
      }
    }

    stage('Test') {
      steps {
        sh 'python3 setup.py test'
      }
    }

    stage('Deploy to Development') {
      when {
        branch 'development'
      }
      steps {
        sh 'python3 setup.py deploy --env development'
      }
    }

    stage('Deploy to Test') {
      when {
        branch 'test'
      }
      steps {
        sh 'python3 setup.py deploy --env test'
      }
    }

    stage('Deploy to Production') {
      when {
        branch 'master'
      }
      steps {
        sh 'python3 setup.py deploy --env production'
      }
    }
  }
}
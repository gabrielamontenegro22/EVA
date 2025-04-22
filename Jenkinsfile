pipeline {
    agent any

    stages {
        stage('Checkout SCM') {
            steps {
                checkout scm
            }
        }

        stage('Instalar Dependencias') {
            steps {
                script {
                    // Instalación de tkinter
                    sh 'sudo apt-get update'
                    sh 'sudo apt-get install -y python3-tk'
                }
            }
        }

        stage('Ejecutar Pruebas') {
            steps {
                script {
                    echo 'Ejecutando pruebas...'
                    sh 'python3 -m unittest test_contrato.py'
                }
            }
        }

        stage('Resultados') {
            steps {
                echo 'Mostrando resultados...'
            }
        }
    }
}

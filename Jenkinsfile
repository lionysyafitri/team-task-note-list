
pipeline {
    agent any

    stages {
        stage('Checkout') {
            steps {
                echo 'Mengambil source code proyek...'
            }
        }

        stage('Build Backend') {
            steps {
                echo 'Membangun Docker image backend...'
                sh 'docker build -t team-task-backend ./backend'
            }
        }

        stage('Test API') {
            steps {
                echo 'Menjalankan pengujian backend...'
                sh 'docker run --rm team-task-backend python -c "import app; print(\'Backend berhasil dimuat\')"'
            }
        }

        stage('Deploy Application') {
            steps {
                echo 'Melakukan deployment backend menggunakan Docker CLI...'
                sh '''
                    docker rm -f team-task-backend || true

                    docker run -d \
                        --name team-task-backend \
                        --restart unless-stopped \
                        -p 5000:5000 \
                        -v team-task-note-list_task-data:/data \
                        team-task-backend:latest
                '''
            }
        }

        stage('Health Check') {
            steps {
                echo 'Memeriksa kesehatan backend...'
                sh '''
                    docker exec team-task-backend python -c "import urllib.request; print(urllib.request.urlopen('http://localhost:5000/health').read().decode())"
                '''
            }
        }
    }

    post {
        success {
            echo 'Pipeline berhasil dijalankan!'
        }
        failure {
            echo 'Pipeline gagal. Periksa Console Output Jenkins.'
        }
    }
}

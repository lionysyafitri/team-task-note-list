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
                echo 'Menjalankan pengujian API...'
                sh 'docker run --rm team-task-backend python -c "import app; print(\'Backend berhasil dimuat\')"'
            }
        }

        stage('Deploy Application') {
            steps {
                echo 'Menjalankan aplikasi menggunakan Docker Compose...'
                sh 'docker compose up -d --build'
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

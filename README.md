
# Team Task & Note List

## 1. Deskripsi Proyek
Team Task & Note List merupakan aplikasi berbasis web yang digunakan untuk membantu anggota kelompok mengelola daftar tugas dan catatan pekerjaan secara terstruktur.

Aplikasi ini dibuat untuk memudahkan pembagian tanggung jawab, pemantauan status tugas, dan pencatatan informasi dalam kegiatan kerja kelompok.

## 2. Fitur Aplikasi
- Menambahkan tugas kelompok.
- Menampilkan daftar tugas.
- Menambahkan nama anggota yang bertanggung jawab.
- Menambahkan catatan atau deskripsi tugas.
- Mengubah status tugas menjadi selesai.
- Menghapus tugas.

## 3. Teknologi yang Digunakan
- Python: Backend API.
- HTML, CSS, JavaScript: Frontend.
- Docker: Containerization.
- Docker Compose: Pengelolaan beberapa container.
- Jenkins: Otomatisasi CI/CD.
- GitHub: Penyimpanan source code.

## 4. Struktur Proyek

```text
team-task-note-list/
├── backend/
│   ├── app.py
│   ├── Dockerfile
│   └── requirements.txt
├── frontend/
│   └── index.html
├── docker-compose.yml
├── Jenkinsfile
└── README.md
```

## 5. Cara Menjalankan Aplikasi

Pastikan Docker Desktop sudah berjalan.

Jalankan perintah:

```bash
docker compose up -d --build
```

Buka aplikasi melalui:

http://localhost:8080

Backend API:

http://localhost:5000

Health check:

http://localhost:5000/health

## 6. Endpoint API

| Method | Endpoint | Fungsi |
|---|---|---|
| GET | /tasks | Melihat daftar tugas |
| POST | /tasks | Menambahkan tugas |
| PUT | /tasks/{id} | Memperbarui status tugas |
| DELETE | /tasks/{id} | Menghapus tugas |
| GET | /health | Memeriksa kesehatan API |

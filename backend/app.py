
from http.server import BaseHTTPRequestHandler, HTTPServer
import json
import os

DATA_FILE = "/data/tasks.json"


def load_tasks():
    os.makedirs("/data", exist_ok=True)

    if os.path.exists(DATA_FILE):
        with open(DATA_FILE, "r", encoding="utf-8") as file:
            data = json.load(file)
            return data.get("tasks", []), data.get("next_id", 1)

    return [], 1


def save_tasks():
    os.makedirs("/data", exist_ok=True)

    with open(DATA_FILE, "w", encoding="utf-8") as file:
        json.dump(
            {"tasks": tasks, "next_id": next_id},
            file,
            indent=4
        )


tasks, next_id = load_tasks()


class TaskHandler(BaseHTTPRequestHandler):

    def send_json(self, status, data):
        self.send_response(status)
        self.send_header("Content-Type", "application/json")
        self.send_header("Access-Control-Allow-Origin", "*")
        self.send_header(
            "Access-Control-Allow-Methods",
            "GET, POST, PUT, DELETE, OPTIONS"
        )
        self.send_header(
            "Access-Control-Allow-Headers",
            "Content-Type"
        )
        self.end_headers()
        self.wfile.write(json.dumps(data).encode())

    def do_OPTIONS(self):
        self.send_json(200, {"status": "ok"})

    def do_GET(self):
        if self.path == "/tasks":
            self.send_json(200, {"tasks": tasks})

        elif self.path == "/health":
            self.send_json(200, {"status": "active"})

        else:
            self.send_json(404, {"error": "Endpoint not found"})

    def do_POST(self):
        global next_id

        if self.path == "/tasks":
            length = int(self.headers.get("Content-Length", 0))
            body = json.loads(self.rfile.read(length) or b"{}")

            title = body.get("title", "").strip()
            note = body.get("note", "").strip()
            assignee = body.get("assignee", "").strip()

            if not title:
                self.send_json(400, {"error": "Judul tugas wajib diisi"})
                return

            task = {
                "id": next_id,
                "title": title,
                "note": note,
                "assignee": assignee,
                "status": "Belum selesai"
            }

            tasks.append(task)
            next_id += 1
            save_tasks()

            self.send_json(
                201,
                {
                    "message": "Tugas berhasil ditambahkan",
                    "task": task
                }
            )

        else:
            self.send_json(404, {"error": "Endpoint not found"})

    def do_PUT(self):
        try:
            task_id = int(self.path.split("/")[-1])
        except ValueError:
            self.send_json(400, {"error": "ID tugas tidak valid"})
            return

        length = int(self.headers.get("Content-Length", 0))
        body = json.loads(self.rfile.read(length) or b"{}")

        for task in tasks:
            if task["id"] == task_id:
                task["status"] = body.get("status", task["status"])
                task["note"] = body.get("note", task["note"])

                save_tasks()

                self.send_json(
                    200,
                    {
                        "message": "Tugas berhasil diperbarui",
                        "task": task
                    }
                )
                return

        self.send_json(404, {"error": "Tugas tidak ditemukan"})

    def do_DELETE(self):
        try:
            task_id = int(self.path.split("/")[-1])
        except ValueError:
            self.send_json(400, {"error": "ID tugas tidak valid"})
            return

        for task in tasks:
            if task["id"] == task_id:
                tasks.remove(task)
                save_tasks()
                self.send_json(200, {"message": "Tugas berhasil dihapus"})
                return

        self.send_json(404, {"error": "Tugas tidak ditemukan"})


if __name__ == "__main__":
    server = HTTPServer(("0.0.0.0", 5000), TaskHandler)
    print("Team Task & Note List API berjalan di port 5000", flush=True)
    server.serve_forever()

# Dockerized Flask Hello World App

This project demonstrates a **basic Flask application containerized using Docker**.  
It is designed to showcase fundamental skills in **Python, Flask, and Docker**.

---

## 🔹 What This Project Shows

- Ability to create a simple Flask web application
- Understanding of Dockerfiles and containerization
- Running a Python application inside a Docker container
- Basic project structure and dependency management

---

## 🔹 Tech Stack

- Python 3.8
- Flask
- Docker

---

## 🔹 Project Structure

.
├── app.py
├── requirements.txt
├── Dockerfile
└── README.md
yaml


---
## 🐳 Basic Docker Commands (Used in This Project)

```bash
# Check Docker installation
docker --version
docker info

# Build the Docker image
docker build -t welcome-app .

# List Docker images
docker images

# Run the container and map port 5000
docker run -p 5000:5000 welcome-app

# Run container in detached (background) mode
docker run -d -p 5000:5000 welcome-app

# List running containers
docker ps

# List all containers (running + stopped)
docker ps -a

# Stop a running container
docker stop <container_id>

# Remove a stopped container
docker rm <container_id>

# View application logs
docker logs <container_id>

# Access container shell
docker exec -it <container_id> /bin/sh

# Remove Docker image
docker rmi welcome-app

# Clean unused Docker resources
docker system prune

---
## 🔹 How to Run

### Build the Docker Image
```bash
docker build -t welcome-app .

Run the Container
bash

docker run -p 5000:5000 welcome-app

🔹 Output

Access the application at:

http://localhost:5000

Expected response:

Hello World

🔹 Why This Project

This project highlights core DevOps and backend fundamentals such as:

    Containerization
    Environment consistency
    Simple service deployment

✅ Simple, clean, and production‑ready basics
yaml


---

If you want, I can:
✅ Tailor this for **DevOps / MLOps roles**  
✅ Add **resume‑friendly bullet points**  
✅ Add **Docker Hub badge**  

Just say the word.

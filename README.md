# MLOps Project

This repository contains the code and infrastructure for an end-to-end MLOps project. It includes data ingestion, preprocessing, model training, and deployment, all managed with tools like DVC, Docker, and Jenkins.

## Table of Contents

- [Getting Started](#getting-started)
- [DVC Commands](#dvc-commands)
- [Git Commands](#git-commands)
- [Docker Commands](#docker-commands)
- [CI/CD with GitHub Actions](#cicd-with-github-actions)
- [Jenkins Setup](#jenkins-setup)

## Getting Started

To get the project up and running, follow these steps:

1.  **Clone the repository:**

    ```bash
    git clone <repository-url>
    cd <repository-name>
    ```

2.  **Create and activate a virtual environment:**

    ```bash
    python -m venv venv
    source venv/bin/activate
    ```

3.  **Install the required dependencies:**

    ```bash
    pip install -r requirements.txt
    ```

4.  **Reproduce the DVC pipeline:**

    ```bash
    dvc repro
    ```

## DVC Commands

This project uses [DVC](https://dvc.org/) to manage the machine learning pipeline. Here are some common commands:

<details>
<summary>Click to expand</summary>

```bash
# Initialize DVC
dvc init

# Reproduce the pipeline
dvc repro

# Visualize the pipeline
dvc dag

# Show metrics
dvc metrics show
```

</details>

## Git Commands

This project uses [Git](https://git-scm.com/) for version control. Here are some common commands:

<details>
<summary>Click to expand</summary>

```bash
# Check the status of the repository
git status

# Add a file to the staging area
git add <file-name>

# Add all files to the staging area
git add .

# Remove a file from the staging area
git rm --cached <file-name>

# Commit the changes
git commit -m "Your commit message"

# Check the branches
git branch

# Create a new branch
git checkout -b <branch-name>

# Switch to a different branch
git checkout <branch-name>

# Merge a branch into the current branch
git merge <branch-name>

# Pull the latest changes from the remote repository
git pull
```

</details>

## Docker Commands

This project uses [Docker](https://www.docker.com/) to containerize the application. Here are some common commands:

<details>
<summary>Click to expand</summary>

### Basic Commands

```bash
# Pull an image from Docker Hub
docker pull <image-name>

# Run an image
docker run <image-name>

# List all running containers
docker ps

# List all containers
docker ps -a

# Remove a container
docker rm <container-id>

# Remove all containers
docker rm $(docker ps -a -q)

# List all images
docker images -a

# Remove an image
docker rmi <image-name>

# Remove all images
docker rmi $(docker images -q)
```

### Custom Image

```bash
# Build a custom image
docker build -t <image-name>:<tag> .

# Run a custom image
docker run -p 8080:8080 <image-name>:<tag>

# Run a custom image in detached mode
docker run -d -p 8080:8080 <image-name>:<tag>
```

### Push to Docker Hub

```bash
# Login to Docker Hub
docker login

# Push an image to Docker Hub
docker push <image-name>:<tag>
```

</details>

## CI/CD with GitHub Actions

This project uses GitHub Actions for CI/CD. The pipeline is configured to build a Docker image, push it to Amazon ECR, and deploy it to an EC2 instance.

### AWS Setup

1.  **Create an IAM user** with `AmazonEC2ContainerRegistryFullAccess` and `AmazonEC2FullAccess` policies.
2.  **Create an ECR repository** to store the Docker image.
3.  **Launch an EC2 instance** (Ubuntu).
4.  **Install Docker on the EC2 instance:**

    ```bash
    curl -fsSL https://get.docker.com -o get-docker.sh
    sudo sh get-docker.sh
    sudo usermod -aG docker ubuntu
    newgrp docker
    ```

5.  **Configure the EC2 instance as a self-hosted runner** by following the instructions in your repository's `Settings > Actions > Runners` section.
6.  **Add the following secrets** to your repository's `Settings > Secrets and variables > Actions` section:
    -   `AWS_ACCESS_KEY_ID`
    -   `AWS_SECRET_ACCESS_KEY`
    -   `AWS_REGION`
    -   `AWS_ECR_LOGIN_URI`
    -   `ECR_REPOSITORY_NAME`

## Jenkins Setup

This project can also be deployed using Jenkins. Here are the steps to set up Jenkins on an EC2 instance:

1.  **Install Java:**

    ```bash
    sudo apt update
    sudo apt install openjdk-8-jdk -y
    ```

2.  **Install Jenkins:**

    ```bash
    wget -q -O - https://pkg.jenkins.io/debian-stable/jenkins.io.key | sudo apt-key add -
    sudo sh -c 'echo deb http://pkg.jenkins.io/debian-stable binary/ > /etc/apt/sources.list.d/jenkins.list'
    sudo apt update
    sudo apt install jenkins -y
    ```

3.  **Start and enable Jenkins:**

    ```bash
    sudo systemctl start jenkins
    sudo systemctl enable jenkins
    sudo systemctl status jenkins
    ```

4.  **Install Docker:**

    ```bash
    curl -fsSL https://get.docker.com -o get-docker.sh
    sudo sh get-docker.sh
    sudo usermod -aG docker $USER
    sudo usermod -aG docker jenkins
    newgrp docker
    ```

5.  **Install AWS CLI:**

    ```bash
    sudo apt install awscli -y
    ```

6.  **Configure AWS CLI:**

    ```bash
    aws configure
    ```

7.  **Get the Jenkins admin password:**

    ```bash
    sudo cat /var/lib/jenkins/secrets/initialAdminPassword
    ```

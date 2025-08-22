How to run?
python -m venv venv
source venv/bin/activate

pip install -r requirements.txt
dvc repro


DVC Commands
git init

dvc init

dvc repro

dvc dag

dvc metrics show



Docker Test
docker pull hello-world

docker run hello-world

docker ps                                   # See a list of all running containers
docker ps -a                                # See a list of all containers, even the ones not running
docker rm <hash>                            # Remove the specified container from this machine
docker rm $(docker ps -a -q)                # Remove all containers from this machine
docker images -a                            # Show all images on this machine
docker rmi <imagename>                      # Remove the specified image from this machine
docker rmi $(docker images -q)              # Remove all images from this machine
Docker Custom image
docker build -t entbappy/mycalapp:latest .

docker run -p 8080:8080 entbappy/mycalapp:latest

docker run -d -p 8080:8080 entbappy/mycalapp:latest

Push to Docker Hub:
docker login
docker push entbappy/mycalapp:latest
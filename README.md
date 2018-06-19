# Docker101

\
**Clone this repo on your server, preferably Ubuntu 16.04:** \
$ git clone https://github.com/deepali-kishnani/Docker101.git \
\
**Get into the project where the Dockerfile is present:** \
$ cd Docker101 \
\
**To build the docker image, run the command below. What follows after '-t' is the name of the docker image:** \
$ docker build -t flaskimage . \
\
**To view built docker images locally:** \
$ docker image ls \
\
**Run your docker image using the following command.Here you are mapping port 80 of the container to port 5000 of VM/physical server where docker is running. You'll see a message stating that your app is running on port 80 i.e http://0.0.0.0:80:** \
$ docker run -p 4000:80 flaskimage \
\
**Duplicate your terminal session and run this command. If everything goes well, you'll see "Dell EMC Docker101" printed on your console!** \
$ curl http://localhost:4000/ \
\

**To view docker containers locally:** \
$ docker ps \
\
**To stop a docker container. You can get container ID from the above 'docker ps' command:** \
$ docker stop {$DockerContainerID} \
\
**To run a docker image as a background daemon process "-d":** \
$ docker run -d -p 4000:80 flaskImage \
\
**To get into your docker container:** \
$ docker exec -it flaskImage bash \
\
**Link to docker hub account.Sign up here to get access to docker hub public registry:** \
https://hub.docker.com \
\
**To login to your docker hub account for pushing to docker hub public registry:** \
$ docker login \
\
**To tage a docker image locally before pushing to the registry:** \
$ docker tag image-name dockerhub-username/repository-name:tag \
\
**To push the image to docker hub registry:** \
$ docker push dockerhub-username/repository-name:tag \
\
**To delete an image locally:** \
$ docker rmi image-name -f \
\
**To pull an image from your own registry:** \
$ docker pull dockerhub-username/repository-name:tag 




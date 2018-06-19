# Docker101

$ git clone https://github.com/deepali-kishnani/Docker101.git \
$ docker build -t flaskImage . \
$ docker image ls \
$ docker run -p 4000:80 flaskImage \
$ curl http://localhost:4000/ \
$ docker ps \
$ docker stop {$DockerContainerID} \
$ docker run -d -p 4000:80 flaskImage \
$ curl http://localhost:4000/ \
$ docker exec -it flaskImage bash \
$ docker login \
https://hub.docker.com \
$ docker tag image-name dockerhub-username/repository-name:tag \
$ docker push dockerhub-username/repository-name:tag \
$ docker rmi image-name \
$ docker pull dockerhub-username/repository-name:tag 




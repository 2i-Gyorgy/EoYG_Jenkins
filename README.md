resources:

https://www.jenkins.io/doc/book/installing/war-file/
https://www.youtube.com/watch?v=6YZvp2GwT0A

to Run follow these steps:

1. build docker image:
   `docker build -t jenkins .`
2. create network
   `docker network create jenkins`
3. docker run image

```
docker run --name jenkins --restart=on-failure --detach `
--network jenkins --env DOCKER_HOST=tcp://docker:2376 `
--env DOCKER_CERT_PATH=/certs/client --env DOCKER_TLS_VERIFY=1 `
--volume jenkins-data:/var/jenkins_home `
--volume jenkins-docker-certs:/certs/client:ro `
--publish 8080:8080 --publish 50000:50000 jenkins
```

4. get jenkins master password from docker container
   `docker exec jenkins cat /var/jenkins_home/secrets/initialAdminPassword`
5. visit http://localhost:8080 in a browser
6. click install suggested plugins
7. create user credentials and click through setup wizard

resources:

https://www.jenkins.io/doc/book/installing/war-file/
https://www.youtube.com/watch?v=6YZvp2GwT0A

to set up Jenkins and run it follow these steps:

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

Set up Nodes

1. navigate to Dashboard -> Manage Jenkins -> Clouds
2. install Docker extension, than restart
3. in Clouds, create new docker cloud
   but first we need a docker container:
   `docker run -d --restart=always -p 127.0.0.1:2376:2375 --network jenkins -v /var/run/docker.sock:/var/run/docker.sock alpine/socat tcp-listen:2375,fork,reuseaddr unix-connect:/var/run/docker.sock`
   and it's ip address:
   `docker inspect <container_name>`
   find and grab IP address and paste it as docker host uri: `tcp://<IPAddress>:2375`
   Select 'enabled' than test connection
4. under Dashboard -> Manage Jenkins -> Clouds -> docker -> Configure select 'Docker agent templates' and add template
   'Label': docker-agent-pyhton
   'Enabled' - Yes
   'Name': docker-agent-pyhton
   'Docker image': devopsjourney1/myjenkinsagents:python
   'Instance Capacity': 2
   'Remote File System Root': /home/jenkins
   save

Set up Pipeline

1. create a jenkins pipeline
2. under Dashboard -> my_pipeline -> Configuration
   Pipeline - Definition: select 'Pipeline script from SCM'
   SCM: Git
   Repositories - Repository URL: `https://github.com/2i-Gyorgy/EoYG_Jenkins`
   Branches to build - Branch Specifier: `*/main`
   Script Path: `JenkinsfileSh`
   Save
3. Build Now and enjoy

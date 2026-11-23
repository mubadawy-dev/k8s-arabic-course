# BUILD
docker build -t k8s-demo:v1 .
docker image ls

# RUN
docker run -d --name k8s-demo -p 8080:8080 k8s-demo:v1

# VERIFY
docker ps
curl http://localhost:8080/
curl http://localhost:8080/health
curl http://localhost:8080/version
docker logs k8s-demo

# PUSH
docker login
docker tag k8s-demo:v1 YOUR_USERNAME/k8s-demo:v1
docker push YOUR_USERNAME/k8s-demo:v1

# PULL (on another machine)
docker pull YOUR_USERNAME/k8s-demo:v1
docker run -d --name k8s-demo -p 8080:8080 YOUR_USERNAME/k8s-demo:v1

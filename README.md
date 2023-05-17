# instalation instructions

- inside project folder create docker image with the following command
- docker build -t url-shortener-api:latest .
- run docker container with command below
- docker run --name url-shortener-api -p 8080:8080 -v ./data:/app/data url-shortener-api:latest

# Client-Server Communication
This project demonstrates a basic client-server setup using Docker containers. The server runs the javajon/quoters:1.0.0 Quoters service, which provides a RESTful API for fetching quotes. The client is a Python application that makes GET requests to the Quoters service and prints the responses.

## Prerequisites
- Docker desktop and Docker compose

## Setup
The codebase consists of the following main components
- `Dockerfile`: Instructions to build the client application Docker image.
- `client.py`: The Python script that makes RESTful calls to the Quoters service.
- `docker-compose.yml`: Configuration file to orchestrate the Quoters service and client application containers.

## How to run
- clone the repositry
```
git clone https://github.com/Joachim-Chuah/Calling-a-RESTful-service.git
```
- run the docker compose file
```
docker-compose up --build
```
This command builds the client application image (if necessary) and starts both the client and Quoters service containers. The client will automatically make GET requests to the following endpoints:

- /api/random
- /api/
- /api/1
- /api/2

- to shut down run:
```
docker-compose down
```
## Client application
The client.py script performs the following actions:
- Waits for a short period to ensure the Quoters service is ready (using `time.sleep(10)`).
- Makes **GET** requests to the Quoters service's specified endpoints.
- Prints the **JSON** response or an error message based on the response status code.

## Modifying client.py
If you want to make changes to client.py, make sure to rebuild the dockerfile:
```
docker build -t client.py .
```







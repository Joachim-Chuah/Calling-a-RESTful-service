# Client-Server Communication
This project demonstrates a basic client-server setup using Docker containers. The server runs the javajon/quoters:1.0.0 Quoters service, which provides a RESTful API for fetching quotes. The client is a Python application that makes GET requests to the Quoters service and prints the responses.

## Prerequisites
- Docker desktop and Docker compose

## Setup
The codebase consists of the following main components
- 'Dockerfile': Instructions to build the client application Docker image.
- 'client.py': The Python script that makes RESTful calls to the Quoters service.
- 'docker-compose.yml': Configuration file to orchestrate the Quoters service and client application containers.

## How to run



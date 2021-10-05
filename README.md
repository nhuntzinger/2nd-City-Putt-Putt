# 2nd-City-Putt-Putt

## Issues and tasks for the current sprint (Scrum Board History) can be found here:
https://sharing.clickup.com/l/h/6-132298476-1/251510e00dbda0c

## Workspace Description
The 2nd City Putt Putt web app and documents will be stored in this repository

The documentation and resources for this project will be kept in the "docs" folder. This includes use case diagrams, the project plan, and more as the project progresses.

The app itself will be in the directory puttputt

## Usage

### Requirements

- Docker (<https://www.docker.com/products/docker-desktop>)

- docker-compose (<https://docs.docker.com/compose/install/>)

### Starting/Stopping the Application

To launch, run the following in the root directory:

```bash
docker-compose -f docker/docker-compose.yml up -d
```

The website can then be accessed in a local web browser at
<http://localhost:8000/>

To shut down the application run the following:

```bash
docker-compose -f docker/docker-compose.yml down
```

### Building the Docker Image

docker-compose will build the image automatically, but you can also
build the image without using docker-compose. To do so, run the
following in the root directory:

```bash
docker build -f docker/Dockerfile .
```

## Development

When the application is launched with docker-compose all edits you make
to code will be live updated. This means that there is no need to
restart the containers while developing the django application.

That being said, any changes to the environment (including installing
new Python modules) will require the image to be rebuilt.


# Sprint 2 README

## Version Control Procedures
The team will use GitHub to track changes to the system from start to finish. Team members must submit pull requests which must be approved by another team member. 

## Stack
Web Framework: Django
Frontend Library: Bootstrap
Database: Postgres
Continuous integration and deployment: Docker

Setup instructions can be found in the root directory's README

## Unit testing
As suggested by the django project documentation our team will perform unit tests through the unittest module which is built-in to Python.

## Testing the entire solution
Attempt to built the project using Docker
Start the unit tests. 
Actual manual testing.

## Communication Procedures
The team will communicate daily using Discord to checkup on progress and other things

## Version Control Procedures
The team will use GitHub to track changes to the system from start to finish. Team members must submit pull requests which must be approved by another team member. 

## Stack
- Web Framework: Django
- Frontend Library: Bootstrap
- Database: Postgres
- Continuous integration and deployment: Docker

Setup instructions can be found in the root directory's README

## Unit testing
As suggested by the django project documentation our team will perform unit tests through the unittest module which is built-in to Python.

## Testing the entire solution
Attempt to build the project using Docker
Start the unit tests. 
Actual manual testing.

## Code Styling

All code will follow PEP8 Guidlines (<https://pep8.org/>)

With exceptions that we will overide the following rules:

- Spacing will be tabs rather than four spaces

- methods will be named with lower camel case

- Classes will be named with upper camel case

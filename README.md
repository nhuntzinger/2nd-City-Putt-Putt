# 2nd-City-Putt-Putt

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

## Building Docker Container

docker build -t dsatileftrxtract .

### What does this do
This will build a local docker container with the TAG dsaTileFxtXtract;
all of the files in the current working directory except those I explicitly tell
it not to copy, will NOT be accessible in the docker container

## Running the container locally for testing

   docker run -it -v ${PWD}:/data dsatileftrxtract bash

This starts a docker container in interactive mode at a bash terminal

Once the container starts, at least for now, cd into the /opt/build/dermcli/largeImage.examples directory 


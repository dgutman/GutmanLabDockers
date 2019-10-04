docker run --gpus all --init --ipc=host -it -p 8888:8888  -v ${PWD}:/local fastai

## Working directory container is started from gets mounted in /local

## ipc host is needed to increase amount of shared memory container has access to
 #-v $CODE:/code -v $DATA:/data -w="/code/fastai"


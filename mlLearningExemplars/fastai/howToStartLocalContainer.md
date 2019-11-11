#docker run --gpus all --init --ipc=host -it -p 8888:8888  -v ${PWD}:/local fastai
#docker run --gpus all --rm --init --ipc=host -it -p 8888:8888  -v ${PWD}:/local -v /home/dagutman/data:/local/data -v /nvmeLocal/isicData:/nvmeLocal/isicData fastai 
docker run --gpus '"device=1"' --rm --init --ipc=host -it -p 8888:8888  -v ${PWD}:/local -v /home/dagutman/data:/local/data -v /nvmeLocal/isicData:/nvmeLocal/isicData fastai 
### This will run on the 1070
## Working directory container is started from gets mounted in /local

## ipc host is needed to increase amount of shared memory container has access to
 #-v $CODE:/code -v $DATA:/data -w="/code/fastai"


## To create the environment I am using for these notebooks 
## I am using python 2.7



## To create a new environment from scratch


conda create --name dsaCBIR jupyter pandas numpy opencv


## to use/activate the environment

source activate dsaCBIR 

## You must have anaconda installed or this won't work

# To export the current environment
conda env export > environment.yml


# to create an ENV from the repo
conda env create -f environment.yml



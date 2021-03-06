FROM nvidia/cuda:10.0-base-ubuntu16.04

# Install some basic utilities
RUN apt-get update && apt-get install -y \
    curl \
    ca-certificates \
    sudo \
    git \
    bzip2 \
    libx11-6 \
    unzip \
 && rm -rf /var/lib/apt/lists/*

# Create a working directory
RUN mkdir /app
WORKDIR /app

# Create a non-root user and switch to it
RUN adduser --disabled-password --gecos '' --shell /bin/bash user \
 && chown -R user:user /app
RUN echo "user ALL=(ALL) NOPASSWD:ALL" > /etc/sudoers.d/90-user
USER user

# All users can use /home/user as their home directory
ENV HOME=/home/user
RUN chmod 777 /home/user

# Install Miniconda
RUN curl -so ~/miniconda.sh https://repo.continuum.io/miniconda/Miniconda3-4.5.11-Linux-x86_64.sh \
 && chmod +x ~/miniconda.sh \
 && ~/miniconda.sh -b -p ~/miniconda \
 && rm ~/miniconda.sh
ENV PATH=/home/user/miniconda/bin:$PATH
ENV CONDA_AUTO_UPDATE_CONDA=false

# Create a Python 3.6 environment
RUN /home/user/miniconda/bin/conda create -y --name py36 python=3.6.9 \
 && /home/user/miniconda/bin/conda clean -ya
ENV CONDA_DEFAULT_ENV=py36
ENV CONDA_PREFIX=/home/user/miniconda/envs/$CONDA_DEFAULT_ENV
ENV PATH=$CONDA_PREFIX/bin:$PATH
RUN /home/user/miniconda/bin/conda install conda-build=3.18.9=py36_3 \
 && /home/user/miniconda/bin/conda clean -ya

# CUDA 10.0-specific steps
RUN conda install -y -c pytorch \
    cudatoolkit=10.0 \
    "pytorch=1.2.0=py3.6_cuda10.0.130_cudnn7.6.2_0" \
    "torchvision=0.4.0=py36_cu100" \
    scikit-learn \
 && conda clean -ya

# Install HDF5 Python bindings
RUN conda install -y h5py=2.8.0 \
 && conda clean -ya
RUN pip install h5py-cache==1.0

# Install Torchnet, a high-level framework for PyTorch
RUN pip install torchnet==0.0.4

# Install Requests, a Python library for making HTTP requests
RUN conda install -y requests=2.19.1 \
 && conda clean -ya

# Install Graphviz
RUN conda install -y graphviz=2.40.1 python-graphviz=0.8.4 jupyter\
 && conda clean -ya

# Install OpenCV3 Python bindings
RUN sudo apt-get update && sudo apt-get install -y --no-install-recommends \
    libgtk2.0-0 \
    libcanberra-gtk-module \
    texlive-xetex texlive-fonts-recommended texlive-generic-recommended nano \
 && sudo rm -rf /var/lib/apt/lists/*
RUN conda install -y -c menpo opencv3=3.1.0 \
 && conda clean -ya

# Install FastAI
RUN conda install -y -c fastai fastai

RUN conda install -c fastai -c stason ipyexperiments

RUN conda clean -ya


## Add in FastAI Tutorial samples
# Switch back to root user temporarily

USER root
RUN mkdir -p /data/notebooks
RUN chmod -R a+w /data


WORKDIR /data/notebooks

USER user

RUN git clone https://github.com/fastai/fastai.git /data/notebooks

#RUN curl http://files.fast.ai/data/dogscats.zip --output dogscats.zip
#RUN unzip -d . dogscats.zip
#RUN rm dogscats.zip


#RUN ln -s /data/ /notebooks/courses/dl1/
#RUN ls -la /notebooks/courses/dl1/data/

RUN jupyter notebook --generate-config --allow-root
RUN echo "c.NotebookApp.password =  u'sha1:8b1f051f33c3:2aa6861f67d30286b780bf7270bc25ce157519c8'" >> /home/user/.jupyter/jupyter_notebook_config.py	


RUN echo "c.NotebookApp.notebook_dir = '/'" >> /home/user/.jupyter/jupyter_notebook_config.py

CMD ["jupyter", "notebook", "--ip=0.0.0.0", "--no-browser", "--allow-root", "--no-browser"]

# Set the default command to python3
#CMD ["python3"]




#FROM pytorch/pytorch:latest

#RUN /opt/conda/bin/conda install -y nodejs Cython tensorflow pandas scikit-learn matplotlib seaborn jupyter jupyterlab && \
#    /opt/conda/bin/conda install -c conda-forge tensorboardx && \
#    /opt/conda/bin/conda clean -ya

#RUN jupyter labextension install jupyterlab_tensorboard

#RUN pip install jupyter_tensorboard torchvision scikit-image

# tensorboard
#EXPOSE 6006
# jupyter notebook
#EXPOSE 8888

#COPY start.sh /

#CMD ["/start.sh"]


#FROM nvidia/cuda:10.1-cudnn7-devel-ubuntu18.04

#LABEL com.nvidia.volumes.needed="nvidia_driver"



#	rm -rf /var/lib/apt/lists/*





#ENV PATH /opt/conda/envs/fastai/bin:$PATH
#ENV LD_LIBRARY_PATH /usr/local/nvidia/lib:/usr/local/nvidia/lib64
#ENV USER fastai

#CMD source activate fastai
#CMD source ~/.bashrc

#RUN /opt/conda/bin/conda install jupyterlab

#WORKDIR /data



#RUN curl https://bootstrap.pypa.io/get-pip.py -O && \     
#        python3 get-pip.py && \
#        rm get-pip.py

#    ln /usr/bin/pip3 /usr/bin/pip && \
#RUN pip install --upgrade setuptools && \
#   ln /usr/bin/pip3 /usr/bin/pip

#
#    pip install --no-cache-dir --upgrade 'git+https://github.com/cdeepakroy/ctk-cli' && \
#    git clone --depth 1 https://github.com/girder/slicer_cli_web.git && \   
#    cd $dermcli_dir && pip install -r requirements.txt


#RUN pip install torch fastai
#ENV PATH /opt/conda/bin:$PATH
#WORKDIR /notebooks

#ENV PATH /opt/conda/envs/fastai/bin:$PATH

#CMD ["jupyter", "lab", "--ip=0.0.0.0", "--no-browser", "--allow-root"]

#RUN source activate fastai

#CMD ["jupyter", "notebook", "--ip=0.0.0.0", "--no-browser", "--allow-root", "--notebook-dir='/notebooks'"]

#https://github.com/MattKleinsmith/dockerfiles/tree/master/fastai

#conda create -n fastai python=3.7 mypy pylint jupyter scikit-learn pandas
#source activate fastai
#Next, if you are planning on installing the GPU version, verify which CUDA you have installed:

#nvcc --version # Cuda compilation tools, release 10.0, V10.0.130
#You can find the corresponding conda package using:

#conda search cuda* -c pytorch
#Look for the cudaXX packages that matches your CUDA version as reported by nvcc.

#You can now install pytorch and fastai using conda.

#conda install cudatoolkit=10.0 -c pytorch -c fastai fastai

#https://towardsdatascience.com/fastai-image-classification-32d626da20
#I has this problem than use docker image - and solution was add flag “–ipc=host” for docker run
#nvidia-docker run --rm -ti --ipc=host pytorch-cudnnv6
#Full doc for docker image - https://github.com/pytorch/pytorch#docker-image 148



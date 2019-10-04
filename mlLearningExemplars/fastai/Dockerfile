FROM nvidia/cuda:10.1-cudnn7-devel-ubuntu18.04

LABEL com.nvidia.volumes.needed="nvidia_driver"

#RUN echo "deb http://developer.download.nvidia.com/compute/machine-learning/repos/ubuntu1604/x86_64 /" > /etc/apt/sources.list.d/nvidia-ml.list

RUN apt-get update && apt-get install -y --allow-downgrades --no-install-recommends \
         build-essential \
         cmake \
         git \
         curl \
         vim \
         ca-certificates \
         python-qt4 \
         libjpeg-dev \
	 zip \
	 unzip \
         libpng-dev \
	python3-dev &&\
	rm -rf /var/lib/apt/lists/*



WORKDIR /notebooks

RUN git clone https://github.com/fastai/fastai.git .

ENV PATH /opt/conda/envs/fastai/bin:$PATH
ENV LD_LIBRARY_PATH /usr/local/nvidia/lib:/usr/local/nvidia/lib64
ENV USER fastai

CMD source activate fastai
CMD source ~/.bashrc

#RUN /opt/conda/bin/conda install jupyterlab

WORKDIR /data

RUN curl http://files.fast.ai/data/dogscats.zip --output dogscats.zip
RUN unzip -d . dogscats.zip
RUN rm dogscats.zip

RUN ln -s /data/ /notebooks/courses/dl1/
RUN ls -la /notebooks/courses/dl1/data/

RUN chmod -R a+w /notebooks

RUN curl https://bootstrap.pypa.io/get-pip.py -O && \     
        python3 get-pip.py && \
        rm get-pip.py

#    ln /usr/bin/pip3 /usr/bin/pip && \
#RUN pip install --upgrade setuptools && \
#   ln /usr/bin/pip3 /usr/bin/pip

#
#    pip install --no-cache-dir --upgrade 'git+https://github.com/cdeepakroy/ctk-cli' && \
#    git clone --depth 1 https://github.com/girder/slicer_cli_web.git && \   
#    cd $dermcli_dir && pip install -r requirements.txt


RUN pip install torch fastai
ENV PATH /opt/conda/bin:$PATH
WORKDIR /notebooks

ENV PATH /opt/conda/envs/fastai/bin:$PATH

#CMD ["jupyter", "lab", "--ip=0.0.0.0", "--no-browser", "--allow-root"]

#RUN source activate fastai

CMD ["jupyter", "notebook", "--ip=0.0.0.0", "--no-browser", "--allow-root", "--notebook-dir='/notebooks'"]

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
I has this problem than use docker image - and solution was add flag “–ipc=host” for docker run
nvidia-docker run --rm -ti --ipc=host pytorch-cudnnv6
Full doc for docker image - https://github.com/pytorch/pytorch#docker-image 148



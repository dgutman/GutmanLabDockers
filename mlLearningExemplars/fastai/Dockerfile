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
         libpng-dev &&\
     rm -rf /var/lib/apt/lists/*


ENV PYTHON_VERSION=3.6
RUN curl -o ~/miniconda.sh -O  https://repo.continuum.io/miniconda/Miniconda3-latest-Linux-x86_64.sh  && \
     chmod +x ~/miniconda.sh && \
     ~/miniconda.sh -b -p /opt/conda && \
     rm ~/miniconda.sh && \
    /opt/conda/bin/conda install conda-build


WORKDIR /notebooks

RUN git clone https://github.com/fastai/fastai.git .
RUN ls && /opt/conda/bin/conda env create
RUN /opt/conda/bin/conda clean -ya

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
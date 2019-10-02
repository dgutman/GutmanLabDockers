FROM ubuntu:18.04
MAINTAINER deepak.chittajallu@kitware.com

# Install prerequisites
RUN apt-get update && \
    apt-get install -y --no-install-recommends \
    build-essential \
    libssl-dev \
    libffi-dev \
    libglib2.0-0 \
    libxrender-dev \
    libsm6 libxext6 \
    ca-certificates \
    git \
    wget curl \
    make cmake \
    python3-dev && \
    apt-get autoremove && \    
    rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*

ENV build_path=/opt/build
WORKDIR $build_path

ENV dermcli_dir=$build_path/dermcli
COPY . $dermcli_dir

### The COPY . copies everything from a working directory
### Could add a .dockerIgnore file to have it skip certain skips


RUN curl https://bootstrap.pypa.io/get-pip.py -O && \     
        python3 get-pip.py && \
        rm get-pip.py

#    ln /usr/bin/pip3 /usr/bin/pip && \
RUN pip install --upgrade setuptools && \
    pip install --no-cache-dir --upgrade 'git+https://github.com/cdeepakroy/ctk-cli' && \
    git clone --depth 1 https://github.com/girder/slicer_cli_web.git && \   
    cd $dermcli_dir && pip install -r requirements.txt

RUN ln /usr/bin/python3 /usr/bin/python && \
    pip install large-image[all] --find-links https://manthey.github.io/large_image_wheels

# use entrypoint of slicer_cli_web to expose slicer CLIS of this plugin on web
WORKDIR $dermcli_dir/slicer_clis
#ENTRYPOINT ["python", "/opt/build/slicer_cli_web/server/cli_list_entrypoint.py"]

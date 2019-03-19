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
    python3-dev python3-pip && \
    apt-get autoremove && \    
    rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*

ENV build_path=/opt/build
WORKDIR $build_path

ENV dermcli_dir=$build_path/dermcli
COPY . $dermcli_dir

RUN ln /usr/bin/python3 /usr/bin/python && \
    ln /usr/bin/pip3 /usr/bin/pip && \
    pip install --upgrade setuptools && \
    pip install --no-cache-dir --upgrade 'git+https://github.com/cdeepakroy/ctk-cli' && \
    git clone --depth 1 https://github.com/girder/slicer_cli_web.git && \   
    cd $dermcli_dir && pip install -r requirements.txt

# use entrypoint of slicer_cli_web to expose slicer CLIS of this plugin on web
WORKDIR $dermcli_dir/slicer_clis
ENTRYPOINT ["python", "/opt/build/slicer_cli_web/server/cli_list_entrypoint.py"]

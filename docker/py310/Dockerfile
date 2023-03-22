FROM python:3.10
ENV PYTHONUNBUFFERED 1
ENV PROJECT_DIR py310

RUN apt-get update \
    && apt-get install -y locales \
    && locale-gen ja_JP.UTF-8 \
    && echo "export LANG=ja_JP.UTF-8" >> ~/.bashrc

# X11の設定
RUN apt-get update -y\
 && apt-get install x11-apps -y
ENV DISPLAY host.docker.internal:0.0

# apt
RUN apt-get update -y \
 && apt-get install tree -y

# Python
WORKDIR /${PROJECT_DIR}
ADD docker/py310/etc/requirements.txt /${PROJECT_DIR}
RUN apt-get -y update && \
    apt-get -y install \
    apt-utils \
    gcc && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/* && \
    pip install --upgrade pip && \
    pip install --no-cache-dir -r requirements.txt
# Build a container with official image: python
FROM python:3.8

# Update environment and install gauge
RUN pip install --upgrade pip

# https://docs.gauge.org/howto/ci_cd/docker.html?os=macos&language=javascript&ide=vscode
RUN apt-key adv --keyserver hkp://pool.sks-keyservers.net --recv-keys 023EDB0B
RUN echo deb https://dl.bintray.com/gauge/gauge-deb stable main | tee -a /etc/apt/sources.list
RUN apt-get update
RUN apt-get install gauge

# Copy source to container
RUN mkdir api-automation
RUN cd api-automation
WORKDIR /api-automation
COPY . /api-automation

# Install required python libraries with a quiet flag
RUN pip install -r requirements.txt -q

# Set Timezone
ENV TZ 'Asia/Ho_Chi_Minh'
RUN echo $TZ > /etc/timezone && \
    apt-get update -qq && apt-get install -y -qq tzdata && \
    rm /etc/localtime && \
    ln -snf /usr/share/zoneinfo/$TZ /etc/localtime && \
    dpkg-reconfigure -f noninteractive tzdata && \
    apt-get clean -qq

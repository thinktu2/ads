# Pull base image
FROM ubuntu:18.04

# Author
LABEL author="cs.thinktu@gmail.com"

# Initialize custom image
RUN sed -i 's#archive.ubuntu.com#mirrors.ustc.edu.cn#g' /etc/apt/sources.list \
    # Update software source
    && apt-get update && apt-get upgrade -y \
    # Install softwares
    && apt-get install build-essential make python3.8 -y \
    # Establish a soft connection
    && ln -s /usr/bin/python3.8 /usr/bin/python && ln -s /usr/bin/python3.8 /usr/bin/python3

# Copy all files to root
COPY ./assignment /root/ads
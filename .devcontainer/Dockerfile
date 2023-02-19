FROM debian:11-slim

RUN apt-get update && \
    apt-get install python3 python-is-python3 python3-pip python3-venv -y && \
    apt-get install git -y && \
    apt-get install build-essential -y

RUN python3 -m pip install --user pipx && \
    python3 -m pipx ensurepath

ENV PATH=$PATH:/root/.local/bin

RUN pipx install poetry
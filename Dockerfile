FROM mcr.microsoft.com/vscode/devcontainers/anaconda:0-3

RUN conda install -y -c anaconda make

COPY requirements.txt /tmp/
RUN pip install -r /tmp/requirements.txt

# RUN mkdir -p /src
# COPY src/ /src/
# RUN pip install -e /src
# COPY tests/ /tests/

# WORKDIR /src

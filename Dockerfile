FROM openfabric/openfabric-pyenv:0.1.9-3.8

RUN mkdir cognitive-assistant
WORKDIR /cognitive-assistant
COPY . .
RUN pip install --upgrade pip
RUN export PIP_DEFAULT_TIMEOUT=100
COPY requirements.txt /tmp/requirements.txt
RUN pip install -r /tmp/requirements.txt
#RUN poetry install -vvv --no-dev
EXPOSE 5000
CMD ["sh","start.sh"]

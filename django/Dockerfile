FROM python:latest

RUN python -m venv /opt/.venv

ENV PATH=/opt/.venv/bin:$PATH

RUN pip install --upgrade pip

ENV PYTHONDONTWRITEBYTECODE=1

ENV PYTHONUNBUFFERED=1

RUN mkdir -p /code/

WORKDIR /code/

COPY requirements.txt /tmp/requirements.txt

RUN pip install -r /tmp/requirements.txt

COPY ./src/ /code/

COPY ./install.sh /code/

RUN chmod +x install.sh

COPY ./run.sh /code/

RUN chmod +x run.sh

RUN ./install.sh

RUN ./run.sh





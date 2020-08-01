FROM python:3.6
ENV PYTHONUNBUFFERED 1

ADD . /meetingroomservice
WORKDIR /meetingroomservice
RUN chmod +x wait-for-it.sh
RUN pip install -r requirements.txt

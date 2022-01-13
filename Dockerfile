FROM python:3.8
ENV PYTHONUNBUFFERED=1
WORKDIR /api
COPY requirements.txt requirements.txt
RUN pip3 install --upgrade pip
RUN pip3 install -r requirements.txt
COPY ./src /api
EXPOSE 8000

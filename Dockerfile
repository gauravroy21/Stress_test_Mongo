FROM locustio/locust
WORKDIR /mnt/locust
COPY . /mnt/locust
RUN pip install -r requirements.txt
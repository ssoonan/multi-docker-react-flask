FROM python:3.6-alpine

EXPOSE 5000

COPY requirements.txt requirements.txt
RUN pip3 install -U pip
RUN pip3 install -r requirements.txt

ENV FLASK_APP run.py
ENV FLASK_ENV production

RUN chmod +x ./boot.sh
ENTRYPOINT ["./boot.sh"]
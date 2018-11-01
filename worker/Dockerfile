FROM zapper0703/python-pipenv:0.1.1-base

RUN adduser -D worker
WORKDIR /home/worker

COPY Pipfile Pipfile
COPY Pipfile.lock Pipfile.lock
RUN pipenv install --deploy --system

COPY worker.py worker.py
RUN chmod 555 worker.py

RUN chown -R worker:worker ./
USER worker

EXPOSE 8001
ENTRYPOINT [ "python", "worker.py" ]
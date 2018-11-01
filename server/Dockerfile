FROM zapper0703/python-pipenv:0.1.1-deploy-psql

RUN adduser -D server
WORKDIR /home/server

COPY Pipfile Pipfile
COPY Pipfile.lock Pipfile.lock

RUN pipenv install --deploy --system

COPY server.py server.py
COPY boot.sh boot.sh
RUN chmod 555 boot.sh
COPY migrations migrations

RUN chown -R server:server ./
USER server

EXPOSE 8000
ENTRYPOINT ["./boot.sh"]
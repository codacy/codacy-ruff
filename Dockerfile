FROM python:3.13-alpine3.21

COPY requirements.txt requirements.txt

RUN apk add --no-cache --update bash && \
    pip3 install --no-cache-dir -r requirements.txt

COPY src/codacy_ruff.py codacy_ruff.py

COPY src/codacy_ruff_test.py codacy_ruff_test.py

COPY docs /docs

RUN adduser -u 2004 -D docker

RUN chown -R docker:docker /docs /home/docker

RUN chown -R docker:docker /home/docker

USER docker

ENTRYPOINT [ "python" ]

CMD [ "codacy_ruff.py" ]

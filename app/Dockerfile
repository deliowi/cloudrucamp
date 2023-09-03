FROM python:3.11.5

ENV AUTHOR Nastya
ENV UUID d57ceee9-fb97-42b5-9cf3-57b81bafb01a

EXPOSE 8000 8000

WORKDIR /app/
COPY app.py /app/

RUN pip install flask-restful

ENTRYPOINT python3 app.py
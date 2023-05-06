FROM python:3.10.4-slim-buster
WORKDIR /app
COPY main.py config.py url_map.py requirements.txt ./
RUN pip install -r requirements.txt
ENV FLASK_APP=main
ENV FLASK_RUN_PORT=8080
ENV FLASK_RUN_HOST=0.0.0.0

CMD ["flask", "run"]
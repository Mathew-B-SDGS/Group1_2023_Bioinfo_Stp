FROM python:3.9
WORKDIR /app
COPY ./requirements.txt /app
RUN pip install -r requirements.txt
COPY ./modules/ /app
COPY ./resources/ /app
COPY ./templates/ /app
COPY ./appblueprints /app
COPY app.py /app
EXPOSE 5000
ENV FLASK_APP=app.py
CMD ["flask", "run", "--host", "0.0.0.0"]

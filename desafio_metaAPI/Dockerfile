FROM python:latest

WORKDIR /usr/src/app

COPY desafio_metaAPI/requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

CMD [ "gunicorn", "-b", "0.0.0.0:8080", "--chdir", "/usr/src/app/desafio_metaAPI", "metaAPI.wsgi" ]

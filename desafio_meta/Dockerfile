FROM python:3

WORKDIR /usr/src/app

COPY desafio_meta/requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

CMD [ "gunicorn", "-b", "0.0.0.0:8000","--chdir", "/usr/src/app/desafio_meta", "desafio.wsgi" ]

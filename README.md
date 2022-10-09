## Sobre
- desafio Fullstack web da empresa metaIT
- um webapp de disposição e criação de insights ![image](https://user-images.githubusercontent.com/58372907/194761656-e1f676ad-7232-438c-af28-af8e159b7173.png)


## Descrição tecnica
- webapp feito em Django, django-restframework, html e css
- usando servidor Gunicorn Wsgi para servir a aplicacao
- nginx na frente como servidor web e proxy reverso para o Gunicorn e cache
- Docker e docker compose para gerenciar todos os coniners e fazerem eles se comunicarem
- e como banco sqllite3 por comodidade podendo ser substituido facilmente por um contaier de Mysql ou PostGres


## Como rodar:
- na pasta raiz da aplicacao basta rodar docker-compose build para buildar as imagens
- e logo apos docker-compose up para lavantar os serviços
- não esquecer de ter docker e docker-compose na maquina
- e acessar localhost no navegador
- para fazer a importação CSV via cli na pasta da api (desafio_metaAPI) rodar python manage.py cli_card


## TODO:
- fazer integração com user default do django e telas para usuario e login
- fazer a pesquisa funcionar
- limitar os cards e talvez paginar
- proxy cache na camada do nginx


## PORTAS:
- aplicacao porta 8000
- api 8080
- nginx 80


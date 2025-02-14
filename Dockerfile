# Imagem Usada
FROM python:alpine3.20

#Diretorio de trabalho
WORKDIR /app

#Copia o arquivo requirementes e Instala Dependências
COPY requirements.txt /app
RUN pip install --no-cache-dir -r requirements.txt

#Copia o Diretorio app
COPY app /app

#Expöe a porta 8000 (Também configurada no app)
EXPOSE 8000

#Comando que roda o aplicativo
CMD [ "python", "./main.py" ]
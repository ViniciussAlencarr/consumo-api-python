from django import db
import requests
import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="311020",
  database="db-pg"
)
mycursor = mydb.cursor()
mycursor.execute("SELECT * FROM app_consultacep;")
dbResponse = mycursor.fetchone()
def requisicao(cepValue):
  cep = cepValue
  request = requests.get('https://viacep.com.br/ws/{}/json/'.format(cep))
  return request.text

from flask import Flask, render_template
from datetime import datetime
import requests
from lxml import html
from httplib2 import Http
from json import dumps
from bs4 import BeautifulSoup

app = Flask(__name__)
#data definition
def data():
    source = 'https://www.bancodeoccidente.hn/banca-personas/internacional/divisas-personas'
    page = requests.get(source)
    #parsea pagina y extrae bloque de cambio de dolar
    soup = BeautifulSoup(page.text, 'html.parser')
    data = soup.find("div", {"id":"dollar-panel-1"})

    #soup = BeautifulSoup(data, "html.parser")
    a = []
    for span in data.select("span"):
        a.append(span.get_text())
    #Recorre lista de y extrae datos.
    for i, val in enumerate(a): 
    #print (i, ",",val)
        if (val == "Venta"):
            cambioventa = a[i+1]
        if (val == "Compra"):
            cambiocompra = a[i+1]

    now = datetime.now()
    dt_string = now.strftime("%d/%m/%Y %H:%M:%S")
    datos_list = {"Compra": cambiocompra, "Venta":cambioventa,"Fecha":dt_string}
    return datos_list

@app.route("/")
def muestracambio():

    return render_template(
        "cambio.html",
        change = data()
        )


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=80, debug=True)
    #app.run()

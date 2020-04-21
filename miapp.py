from flask import Flask, render_template
from datetime import datetime
import requests
from lxml import html
from httplib2 import Http
from json import dumps
from time import process_time 


app = Flask(__name__)
#data definition
def data():
    datos_dic={}
    source = 'https://www.bancodeoccidente.hn/banca-personas/internacional/divisas-personas'
    data = requests.get(source, verify=False)
    tree = html.fromstring(data.content)
    #data extraction
    responsecambiocompra = tree.xpath('//span[@id="usd-compra"]/text()')
    responsecambioventa = tree.xpath('//span[@id="usd-venta"]/text()')
    #list2string
    cambiocompra = ''.join(responsecambiocompra)
    cambioventa = ''.join(responsecambioventa)
    now = datetime.now()
    dt_string = now.strftime("%d/%m/%Y %H:%M:%S")
    datos_list = {"Compra": cambiocompra, "Venta":cambioventa,"Fecha":dt_string}
    t1_stop = process_time()
    return datos_list

@app.route("/")
def muestracambio():

    return render_template(
        "cambio.html",
        change = data()
        )


if __name__ == "__main__":
    app.run()

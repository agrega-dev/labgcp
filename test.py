from flask import Flask, render_template
from datetime import datetime
import requests
from lxml import html
from httplib2 import Http
from json import dumps

#import iso8601
#data definition
def main():
    datos_list={}
    source = 'https://www.bancodeoccidente.hn/banca-personas/internacional/divisas-personas'
    data = requests.get(source, verify=False)
    tree = html.fromstring(data.content)
    #data extraction
    responsecambiocompra = tree.xpath('//span[@id="usd-compra"]/text()')
    responsecambioventa = tree.xpath('//span[@id="usd-venta"]/text()')
    #list2string
    cambiocompra = ''.join(responsecambiocompra)
    cambioventa = ''.join(responsecambioventa)
    #validate
    #print (cambiocompra)
    #print (cambioventa)
    #fecha
    now = datetime.now()
    dt_string = now.strftime("%d/%m/%Y %H:%M:%S")
    datos_list = {"Compra": cambiocompra, "Venta":cambioventa,"Fecha":dt_string}
    print(datos_list)
    return datos_list 


if __name__ == "__main__":
    main()
import requests
import json
import time
import random
from bs4 import BeautifulSoup
from tqdm import tqdm
import os


def traerData():
    
    url = "https://www.promiedos.com.ar/championsleague"
    
    response = requests.get(url, verify=False)
    soup = BeautifulSoup(response.content, 'html.parser')
    table = soup.find('table', {'class': 'tablesorter1'})

        #response = requests.get(url, verify=certifi.where())
    response.raise_for_status()  # Levanta una excepción si hay un error en la solicitud
    time.sleep(random.uniform(2, 5))  # Retraso aleatorio
    """Extrae y retorna los valores de cambio de divisas del BCV en formato JSON."""
        # Constantes
    posiciones = []
    equipos = []
    puntos = []
    pjs = []
    pgs = []
    pes = []
    pps = []
    gfs = []
    gcs = []
    difs = []

    for row in tqdm(table.findAll('tr')[1:]):
        posicion = row.findAll('td')[0].text
        equipo = row.findAll('td')[1].text
        punto = row.findAll('td')[2].text
        pj = row.findAll('td')[3].text
        pg = row.findAll('td')[4].text
        pe = row.findAll('td')[5].text
        pp = row.findAll('td')[6].text
        gf = row.findAll('td')[7].text
        gc = row.findAll('td')[8].text
        dif = row.findAll('td')[9].text

        posiciones.append(posicion)
        equipos.append(equipo)
        puntos.append(punto)
        pjs.append(pj)
        pgs.append(pg)
        pes.append(pe)
        pps.append(pp)
        gfs.append(gf)
        gcs.append(gc)
        difs.append(dif)

    data = {
        "posiciones": posiciones,
        "equipos": equipos,
        "puntos": puntos,
        "pjs": pjs,
        "pgs": pgs,
        "pes": pes,
        "pps": pps,
        "gfs": gfs,
        "gcs": gcs,
        "difs": difs
    }

    with open('data/data.json', 'w') as outfile:
        json.dump(data, outfile)
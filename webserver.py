#!/usr/bin/python3

import os
import time
import psutil
from flask import Flask, render_template_string

app = Flask(__name__)

memory_process = None

HTML_TEMPLATE = """
<html>
<head>
    <meta http-equiv="refresh" content="5">
</head>
<body>
    <h1>Información de la instancia</h1>
    <p>Nombre del Host: {{ hostname }}</p>
    <p>Memoria RAM usada: {{ memory_info }} MB</p>
    <a href="/start">Consumir memoria</a><br>
    <a href="/stop">Detener proceso</a>
</body>
</html>
"""

def consume_memory():
    global memory_process
    memory_process = subprocess.Popen(["python3", "-c", "a = [0] * 10**8"])

def stop_memory():
    global memory_process
    if memory_process is not None:
        memory_process.terminate()
        memory_process = None

def memory_info():
    return psutil.virtual_memory().used / (1024 * 1024)

@app.route('/')
def index():
    hostname = os.getenv('HOSTNAME', 'No definido')
    memory = memory_info()
    return render_template_string(HTML_TEMPLATE, hostname=hostname, memory_info=memory)

@app.route('/start')
def start():
    consume_memory()
    return "Memoria en uso. <a href='/'>Regresar</a>"

@app.route('/stop')
def stop():
    stop_memory()
    return "Proceso detenido. <a href='/'>Regresar</a>"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80)

#!/usr/bin/python3

import os
import subprocess
import threading
from flask import Flask, render_template_string
import psutil

app = Flask(__name__)

memory_process = None

# HTML Template
HTML_TEMPLATE = """
<html>
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
    # Intentar consumir memoria creando una lista grande
    memory_process = subprocess.Popen(["python3", "-c", "a = [0] * 10**6"])

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

def update_html():
    while True:
        threading.Timer(5.0, update_html).start()

if __name__ == '__main__':
    update_html()
    app.run(host='0.0.0.0', port=80)

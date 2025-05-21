from flask import Flask, render_template_string
import psutil
import socket

app = Flask(__name__)

cpu_activo = False

def hacer_calculo_intensivo():
    global cpu_activo
    while cpu_activo:
        _ = 0
        for _ in range(10**7):  # Ajusta el número según la carga deseada.
            _ = _ * 2

@app.route('/')
def index():
    hostname = socket.gethostname()
    mem = psutil.virtual_memory()
    mem_disponible = mem.available / (1024**2)
    porcentaje_ocupado_mem = mem.percent
    
    # Obtener el porcentaje de utilización del CPU.
    porcentaje_ocupado_cpu = psutil.cpu_percent(interval=1)

    info = (f"Hostname: {hostname} - "
            f"Memoria Disponible: {mem_disponible:.2f} MB - "
            f"Memoria Ocupada: {porcentaje_ocupado_mem:.2f}% - "
            f"CPU Ocupado: {porcentaje_ocupado_cpu:.2f}%")
    
    html_content = f"""
    <html>
        <body>
            <h1>{info}</h1>
            <button onclick="fetch('/saturar')">Saturar Memoria</button>
            <button onclick="fetch('/detener')">Detener Memoria</button>
            <button onclick="fetch('/saturar_cpu')">Saturar CPU</button>
            <button onclick="fetch('/detener_cpu')">Detener CPU</button>
        </body>
    </html>
    """
    return render_template_string(html_content)

@app.route('/saturar')
def saturar_memoria():
    global mem_saturada
    # Incrementa la cantidad de elementos para saturar la memoria más rápidamente.
    mem_saturada = [0] * 9**8  # Por ejemplo, pasa de 10^7 a 10^8
    return 'Memoria saturada'

@app.route('/detener')
def detener_proceso():
    global mem_saturada
    mem_saturada = []
    return 'Proceso de memoria detenido'

@app.route('/saturar_cpu')
def saturar_cpu():
    global cpu_activo
    cpu_activo = True
    hacer_calculo_intensivo()
    return 'CPU saturado'

@app.route('/detener_cpu')
def detener_cpu():
    global cpu_activo
    cpu_activo = False
    return 'CPU detenido'

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80)

from flask import Flask, render_template_string
import psutil
import socket

app = Flask(__name__)

@app.route('/')
def index():
    hostname = socket.gethostname()
    mem = psutil.virtual_memory()
    mem_disponible = mem.available / (1024**2)
    porcentaje_ocupado = mem.percent

    info = (f"Hostname: {hostname} - "
            f"Memoria Disponible: {mem_disponible:.2f} MB - "
            f"Memoria Ocupada: {porcentaje_ocupado:.2f}%")
    
    html_content = f"""
    <html>
        <body>
            <h1>{info}</h1>
            <button onclick="fetch('/saturar')">Saturar Memoria</button>
            <button onclick="fetch('/detener')">Detener Proceso</button>
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
    return 'Proceso detenido'

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80)

#!/usr/bin/python
# -*- coding: utf-8 -*-
from gpiozero import LED
from flask import Flask, jsonify, render_template_string

# Configuración del LED
led = LED(17)  # Pin GPIO 17

# Inicialización de Flask
app = Flask(__name__)

# Página HTML con botones y AJAX
html_page = '''
<!doctype html>
<html lang="es">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Control de LED</title>
    <style>
        body { font-family: Arial, sans-serif; text-align: center; padding: 50px; }
        h1 { color: #333; }
        .btn { padding: 10px 30px; font-size: 30px; cursor: pointer; margin: 10px; }
        .btn-on { background-color: #4CAF60; color: white; }
        .btn-off { background-color: #f47336; color: white; }
        .status { font-size: 18px; margin-top: 20px; }
    </style>
    <script>
        function toggleLED(action) {
            fetch('/' + action)
                .then(response => response.json())
                .then(data => {
                    document.getElementById('status').innerText = "Estado: " + (data.status ? "Encendido" : "Apagado");
                });
        }
    </script>
</head>
<body>
    <h1>Control del LED</h1>
    <button class="btn btn-on" onclick="toggleLED('turn_on')">Encender LED</button>
    <button class="btn btn-off" onclick="toggleLED('turn_off')">Apagar LED</button>
    <p class="status" id="status">Estado: Apagado</p>
</body>
</html>
'''

@app.route('/')
def home():
    return render_template_string(html_page)

@app.route('/turn_on')
def turn_on():
    led.on()
    return jsonify({"status": True})

@app.route('/turn_off')
def turn_off():
    led.off()
    return jsonify({"status": False})

if __name__ == '__main__':
    app.run(host='127.0.0.1', port=8000)


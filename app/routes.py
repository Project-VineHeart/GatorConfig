from flask import render_template, request, send_file
from app import app

import json
import os


@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        config = {
            'analog_ports': {
                'port_shallow': request.form['port_shallow'],
                'port_middle': request.form['port_middle'],
                'port_deep': request.form['port_deep'],
                'port_analog': request.form['port_analog'],
            },
            'wifi_ssid': request.form['wifi_ssid'],
            'wifi_passwd': request.form['wifi_passwd'],
        }

        with open('/tmp/config.json', 'w') as f:
            json.dump(config, f)
        return send_file('/tmp/config.json', as_attachment=True)
    return render_template('index.html')

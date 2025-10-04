from flask import Flask, render_template, request, jsonify
from datetime import datetime
import random

app = Flask(__name__)

# Data contoh untuk proyek
projects = [
    {"id": 1, "name": "Sistem Analitik Data", "tech": "Python, Pandas, Matplotlib"},
    {"id": 2, "name": "Aplikasi Web Django", "tech": "Python, Django, PostgreSQL"},
    {"id": 3, "name": "API RESTful", "tech": "Python, Flask, MongoDB"},
    {"id": 4, "name": "Machine Learning Model", "tech": "Python, Scikit-learn, TensorFlow"}
]

@app.route('/')
def home():
    return render_template('index.html', projects=projects, title="Beranda")

@app.route('/about')
def about():
    return render_template('about.html', title="Tentang")

@app.route('/projects')
def project_list():
    return render_template('projects.html', projects=projects, title="Proyek")

@app.route('/api/random-fact')
def random_fact():
    facts = [
        "Python dinamai dari Monty Python, bukan ular.",
        "Python pertama kali dirilis pada tahun 1991.",
        "Python mendukung pemrograman berorientasi objek, terstruktur, dan fungsional.",
        "Python digunakan oleh perusahaan besar seperti Google, NASA, dan Netflix.",
        "Indentasi (penulisan dengan spasi) dalam Python adalah suatu keharusan."
    ]
    return jsonify({"fact": random.choice(facts)})

if __name__ == '__main__':
    app.run(debug=True)
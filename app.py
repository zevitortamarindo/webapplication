# Ao abrir o GitPod, execute:
# pip install -r requirements.txt

from flask import Flask, render_template, request
from uuid import uuid4

app = Flask(__name__)

musicas = [
    {'id':'1', 'artista':'Michel Teló', 'música':'Ai se eu te pego', 'ano':'2011', 'álbum':'Na Balada', 'reproduções':'204,7 milhões'},
    {'id':'2', 'artista':'Los Hermanos', 'música':'Anna Júlia', 'ano':'1999', 'álbum':'Los Hermanos', 'reproduções':'63,4 milhões'},
    {'id':'3', 'artista':'Anitta', 'música':'Show das Poderosas', 'ano':'2013', 'álbum':'Anitta', 'reproduções':'25,4 milhões'},
    {'id':'4', 'artista':'Turma do Pagode', 'música':'Camisa 10', 'ano':'2010', 'álbum':'Esse é o Clima', 'reproduções':'57,7 milhões'}
]

@app.route('/')
def index():
    return render_template('index.html', musicas=musicas)

@app.route('/create')
def create():
    return render_template('create.html')

@app.route('/save', methods=['POST'])
def save():
    artista = request.form['artista']
    música = request.form['música']
    ano = request.form['ano']
    álbum = request.form['álbum']
    reproduções = request.form['reproduções']
    musicas.append({"id": uuid4(), "artista": artista, "música": música, "ano": ano, "álbum": álbum, "reproduções": reproduções})
    return render_template('index.html', musicas=musicas)

app.run()
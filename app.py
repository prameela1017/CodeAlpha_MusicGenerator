from flask import Flask, render_template, request
from music21 import stream, note
import random
import os

app = Flask(__name__)

notes_list = ['C', 'D', 'E', 'F', 'G', 'A', 'B']

def generate_music():
    s = stream.Stream()
    
    for _ in range(10):
        n = random.choice(notes_list)
        s.append(note.Note(n))
    
    # ensure static folder exists
    if not os.path.exists('static'):
        os.makedirs('static')

    s.write('midi', fp='static/output.mid')

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        generate_music()
    
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
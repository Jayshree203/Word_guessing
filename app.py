from flask import Flask, render_template, request, session, redirect, url_for
import random
import os

app = Flask(__name__)
app.secret_key = 'your-secret-key-here'  # Required for session management

words = ['rainbow', 'computer', 'science', 'programming',
         'python', 'mathematics', 'player', 'condition',
         'reverse', 'water', 'board', 'geeks']

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/start_game', methods=['POST'])
def start_game():
    session['name'] = request.form['name']
    session['word'] = random.choice(words)
    session['guesses'] = ''
    session['turns'] = 12
    return redirect(url_for('game'))

@app.route('/game')
def game():
    if 'word' not in session:
        return redirect(url_for('index'))
    
    word = session['word']
    guesses = session['guesses']
    turns = session['turns']
    
    display_word = ''
    failed = 0
    for char in word:
        if char in guesses:
            display_word += char + ' '
        else:
            display_word += '_ '
            failed += 1
    
    game_won = failed == 0
    
    return render_template('game.html',
                         name=session['name'],
                         display_word=display_word,
                         guesses=', '.join(guesses),
                         turns=turns,
                         game_won=game_won,
                         game_over=turns <= 0,
                         word=word if turns <= 0 or game_won else None)

@app.route('/make_guess', methods=['POST'])
def make_guess():
    if 'word' not in session:
        return redirect(url_for('index'))
    
    guess = request.form['guess'].lower()
    if len(guess) == 1 and guess.isalpha():
        if guess not in session['guesses']:
            session['guesses'] += guess
            if guess not in session['word']:
                session['turns'] -= 1
    
    return redirect(url_for('game'))

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 10000))
    app.run(host='0.0.0.0', port=port) 
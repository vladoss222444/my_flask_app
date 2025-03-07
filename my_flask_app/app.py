from flask import Flask, render_template
import random

app = Flask(__name__)

# Список милых слов
nice_words = [
    "Вы прекрасны!",
    "Улыбнитесь, ведь вы великолепны!",
    "Ваше очарование несравнимо!",
    "Пусть ваш день будет наполнен радостью!",
    "Спасибо, что вы есть!",
    "Счастье всегда с вами!",
    "Будьте уверены в себе, вы заслуживаете всего самого лучшего!",
    "Вас любят, и это главное!",
    "Ваша красота сияет изнутри!",
    "Желаю вам чудесного дня!"
]

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/get_nice_word')
def get_nice_word():
    return random.choice(nice_words)

if __name__ == '__main__':
    app.run(debug=True)
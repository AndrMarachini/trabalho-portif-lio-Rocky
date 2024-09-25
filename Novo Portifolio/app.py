from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/about')
def about():
    return render_template('about.html')


@app.route('/languages')
def languages():
    return render_template('languages.html')

@app.route('/links')
def links():
    return render_template('links.html')

if __name__ == '__main__':
    app.run(debug=True)

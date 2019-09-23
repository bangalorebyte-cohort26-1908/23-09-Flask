from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def hello():
    return render_template('index.html')

@app.route('/about/')
def about():
    return 'About Us'

@app.route('/contact/')
def contact():
    return 'Contact Us'

@app.route('/connect/')
def connect():
    return 'connect with Us'

if __name__ == "__main__":
    app.run(debug = True)
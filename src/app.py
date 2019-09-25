from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////tmp/test.db'
db = SQLAlchemy(app)

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)

    def __repr__(self):
        return f'<User {self.username}>'

@app.route("/", methods=['GET','POST'])
def hello():

    if request.method == 'POST':
        name = request.form.get('name')
        email = request.form.get('email')
        useritem = User(username=name, email=email)
        db.session.add(useritem)
        db.session.commit()
        users = User.query.all()
        return render_template('index.html',name=name, insert=True, users=users)
    else:
        users = User.query.all()
        return render_template('index.html', name='Stranger', insert=False, users=users)

@app.route('/about/')
def about():
    return render_template('aboutus.html')

@app.route('/contact/')
def contact():
    return render_template('contactus.html')

if __name__ == "__main__":
    app.run(debug = True)
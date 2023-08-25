import sqlite3
from flask import Flask, render_template
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///app/db/forensic.db'  # SQLite database URI
db = SQLAlchemy(app)  # Create a SQLAlchemy database instance
migrate = Migrate(app, db)  # Associate the Migrate extension with app and db

def get_db():
    db = sqlite3.connect(app.config['SQLALCHEMY_DATABASE_URI'])
    db.row_factory = sqlite3.Row
    return db

@app.route('/')
def index():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)

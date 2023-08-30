import sqlite3
import os
from flask import Flask, render_template
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)

database_path = os.path.join(app.root_path, 'db', 'database.db')

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + database_path  # SQLite database URI
db = SQLAlchemy(app)  # Create a SQLAlchemy database instance
migrate = Migrate(app, db)  # Associate the Migrate extension with app and db

@app.route('/')
def index():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)

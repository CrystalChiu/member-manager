import sqlite3
import os
from flask import Flask, render_template
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

database_path = os.path.join(app.root_path, 'database', 'database.db')
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + database_path  # SQLite database URI

db = SQLAlchemy(app)  # create a SQLAlchemy database instance
migrate = Migrate(app, db, render_as_batch=True) 

if __name__ == '__main__':
    from config import SECRET_KEY, ADMIN_PASSWORD_HASH
    app.secret_key = SECRET_KEY 

    from routes import routes
    routes(app, db, ADMIN_PASSWORD_HASH)

    app.run(debug=True)

import sqlite3
import os
from flask import Flask, render_template
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy

from routes import routes

if __name__ == '__main__':

    app = Flask(__name__)

    database_path = os.path.join(app.root_path, 'database', 'database.db')
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + database_path  # SQLite database URI

    db = SQLAlchemy(app)  # Create a SQLAlchemy database instance
    migrate = Migrate(app, db) 

    print(db)

    #routes(app, db)
    routes(app, db)

    app.run(debug=True)

    import routes

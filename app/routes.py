from flask import render_template

def routes(app):
    @app.route('/')
    def index():
        return render_template('index.html')


    @app.route('/add-member')
    def add_member():
        return render_template('add-member.html')
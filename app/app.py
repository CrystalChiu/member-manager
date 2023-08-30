from app import app

@app.route('/')
def index():
    return render_template('index.html')


@app.route('/add-member')
def index():
    return render_template('add-member.html')

if __name__ == '__main__':
    app.run(debug=True)

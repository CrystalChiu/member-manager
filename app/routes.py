from flask import render_template, request
from sqlalchemy.exc import IntegrityError
from models import Member, Event, Signup

def routes(app, db):
    @app.route('/')
    def index():
        return render_template('index.html')

    @app.route('/add-member', methods=["GET"])
    def render_add_member():
        return render_template('add-member.html')
    
    @app.route('/add-member', methods=['POST'])
    def process_add_member():
        print("func reached")

        if request.method == 'POST':
            try:
                #retrieve form data
                fname = request.form.get('fname').lower()
                lname = request.form.get('lname').lower()
                netId = request.form.get('netId').lower()
                status = "free"
                print(fname + " " + lname + " " + netId)

                #create new member object & populate fields w/input data
                new_member = Member(first_name=fname, last_name=lname, net_id=netId, status=status) 

                # query insert into 'member'
                db.session.add(new_member)
                db.session.commit()

                return("Student successfully added")
            except Exception as e:
                # rollback if not successful
                db.session.rollback()
                print("Error:", repr(e))
                return("Error adding student")
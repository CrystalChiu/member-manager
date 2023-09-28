from flask import render_template, request, redirect, session, url_for
from sqlalchemy.exc import IntegrityError
from models import Member, Event, Signup
from werkzeug.security import check_password_hash
import re

def routes(app, db, ADMIN_PASSWORD_HASH):

    #----------User Facing----------

    @app.route('/')
    def index():
        return render_template('index.html')

    @app.route('/add-member', methods=["GET"])
    def render_add_member():
        return render_template('add-member.html', submit='process_add_member', page_title='Sign Up')
    
    @app.route('/add-member', methods=['POST'])
    def process_add_member():
        try:
            #retrieve form data
            fname = request.form.get('fname').lower()
            lname = request.form.get('lname').lower()
            netId = request.form.get('netId').lower()
            email = request.form.get('email').lower()

            #verify is a uci email
            pattern = r'^[a-zA-Z0-9_.+-]+@uci\.edu$'
            if not re.match(pattern, email):
                raise ValueError("Must be a UCI email")

            #create new member object & populate fields w/input data
            new_member = Member(first_name=fname, last_name=lname, net_id=netId, email=email) 

            # query insert into 'member'
            db.session.add(new_member)
            db.session.commit()

            return("Student successfully added!")
        except Exception as e:
            # rollback if not successful
            db.session.rollback()
            print("Error:", repr(e))
            return("Error adding student")
            
    @app.route('/event-signup', methods=['GET'])
    def render_event_signup():
        #today = datetime.today().date()
        avail_events = [event[0] for event in db.session.query(Event.event_name).all()]

        return render_template('event-signup.html', submit='process_event_signup', avail_events=avail_events, page_title='Event Sign Up')
    
    @app.route('/event-signup', methods=['POST'])
    def process_event_signup():
        try:
            #first try to find the student by netID
            netId = request.form.get('netId').lower()
            member_id = db.session.query(Member.id).filter(Member.net_id == netId).scalar()
            
            #then try to find the event by event name
            eventName = request.form.get('eventName').lower()
            event_id = db.session.query(Event.id).filter(Event.event_name == eventName).scalar()

            #if we can find them then try to add their row into signups table
            new_signup = Signup(member_id=member_id, event_id=event_id)

            db.session.add(new_signup)
            db.session.commit()

            return("Successfully signed up!")
        except Exception as e:
            # rollback if not successful
            db.session.rollback()
            print("Error:", repr(e))
            return("Error signing up for event")
            
    @app.route('/check-in', methods=['GET'])
    def render_check_in():
        return render_template('member-check-in.html', submit='process_check_in', page_title='Check In')
    
    @app.route('/check-in', methods=['POST'])
    def process_check_in():
        try:
            #first try to find the student by netID
            netId = request.form.get('netId').lower()
            member = db.session.query(Member).filter(Member.net_id == netId).scalar()
            
            #then increment the attendence column by 1
            member.attendance += 1

            db.session.commit()

            return("Checked in!")
        except Exception as e:
            # rollback if not successful
            db.session.rollback()
            print("Error:", repr(e))
            return("Error checking in")

    #----------Admin Facing----------
    @app.route('/authenticate', methods=['GET'])
    def authenticate():   
        return render_template('authenticate.html')
    
    @app.route('/authenticate', methods=['POST'])
    def process_authentication():
        if check_password_hash(ADMIN_PASSWORD_HASH, request.form.get('password')):
            session['authenticated'] = True
            return redirect(url_for('render_admin_tools'))  # redirect to admin page on success
        else:
            return redirect(url_for('authenticate'))

    @app.route('/admin', methods=['GET'])
    def render_admin_tools():
        if not session.get('authenticated'):
            return redirect(url_for('authenticate'))  #redirect to authentication if not authenticated
        return "Welcome to the admin page!" #return render template for admin tools
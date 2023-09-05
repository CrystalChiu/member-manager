from flask import render_template, request
from sqlalchemy.exc import IntegrityError
from models import Member, Event, Signup

def routes(app, db):
    @app.route('/')
    def index():
        return render_template('index.html')

    #----------add member feature----------
    @app.route('/add-member', methods=["GET"])
    def render_add_member():
        return render_template('add-member.html')
    
    @app.route('/add-member', methods=['POST'])
    def process_add_member():
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

                return("Student successfully added!")
            except Exception as e:
                # rollback if not successful
                db.session.rollback()
                print("Error:", repr(e))
                return("Error adding student")
            
    #----------event signup feature----------
    @app.route('/event-signup', methods=['GET'])
    def render_event_signup():
        #today = datetime.today().date()
        avail_events = [event[0] for event in db.session.query(Event.event_name).all()]

        return render_template('event-signup.html', avail_events=avail_events)
    
    @app.route('/event-signup', methods=['POST'])
    def process_event_signup():
        if request.method == 'POST':
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
    
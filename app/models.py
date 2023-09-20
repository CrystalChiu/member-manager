from app import db

class Member(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(50), nullable=False)
    last_name = db.Column(db.String(50), nullable=False)
    net_id = db.Column(db.String(20), unique=True, nullable=False)
    attendance =  db.Column(db.Integer, default=0)
    email = db.Column(db.String(50), nullable=False, unique=True)
    received_id = db.Column('received_id', db.Boolean(), default=False)
    member_status_id = db.Column(db.Integer, db.ForeignKey('member_status.id'), nullable=False, default=1)
    payment_plan_id = db.Column(db.Integer, db.ForeignKey('payment_plan.id'), nullable=True)

    signups = db.relationship('Signup', backref='member', lazy=True)

    @property
    def member_status(self):
        return self.member_status.status

    @property
    def payment_plan(self):
        return self.payment_plan.pay_period
    

    def __repr__(self):
        return f'<Member: {self.first_name} {self.last_name}, {self.net_id}>'

class Event(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    date = db.Column(db.Date, nullable=False)
    event_name = db.Column(db.String(50), unique=True, nullable=False)
    max_capacity = db.Column(db.Integer, nullable=True)
    signup_deadline = db.Column(db.Date, nullable=False)

    signups = db.relationship('Signup', backref='event', lazy=True)

    def __repr__(self):
        return f'<Event: {self.event_name})>'

class Signup(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    member_id = db.Column(db.Integer, db.ForeignKey('member.id'), nullable=False)
    event_id = db.Column(db.Integer, db.ForeignKey('event.id'), nullable=False)

    @property
    def event_name(self):
        return self.event.event_name

    @property
    def member_net_id(self):
        return self.member.net_id
    
    def __repr__(self):
        return f'<Signup of {self.member_net_id} for {self.event_name}>'

class MemberStatus(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    status = db.Column(db.String(10), unique=True, nullable=False)

    members = db.relationship('Member', backref='member_status', lazy=True)
    
    def __repr__(self):
        return f'<Status code {self.id} for {self.status}>'

class PaymentPlan(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    pay_period = db.Column('pay_period', db.String(20), nullable=False)
    price = db.Column('price', db.Float(), nullable=False)

    members = db.relationship('Member', backref='payment_plan', lazy=True)
    
    def __repr__(self):
        return f'<Pay period by {self.pay_period} for {self.price}>'
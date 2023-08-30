from app import db

class Member(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(50), nullable=False)
    last_name = db.Column(db.String(50), nullable=False)
    net_id = db.Column(db.String(20), unique=True, nullable=False)
    status = db.Column(db.String(20))

    signups = db.relationship('Signup', backref='member', lazy=True)

    def __repr__(self):
        return f'<Member {self.first_name} {self.last_name}, {self.net_id}>'

class Event(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    date = db.Column(db.Date, nullable=False)
    event_name = db.Column(db.String(50), unique=True, nullable=False)
    max_capacity = db.Column(db.Integer, nullable=True)

    def __repr__(self):
        return f'<Event {self.event_name} ({self.date} on {self.date})>'

class Signup(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    member_id = db.Column(db.Integer, db.ForeignKey('member.id'), nullable=False)
    event_id = db.Column(db.Integer, db.ForeignKey('event.id'), nullable=False)

    signups = db.relationship('Signup', backref='event', lazy=True)

    @property
    def event_name(self):
        return self.event.event_name

    @property
    def member_net_id(self):
        return self.member.net_id
    
    def __repr__(self):
        return f'<Signup of {self.member_net_id} for {self.event_name}>'


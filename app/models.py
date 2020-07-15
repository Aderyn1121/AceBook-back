from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import generate_password_hash, check_password_hash

db = SQLAlchemy()


class User(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    gender = db.Column(db.String(20), nullable=False)
    first_name = db.Column(db.String(20), nullable=False)
    last_name = db.Column(db.String(20), nullable=False)
    email = db.Column(db.String(100), nullable=False, unique=True)
    hashed_password = db.Column(db.String(128), nullable=False)
    gender_pref = db.Column(db.String(20))
    img_url = db.Column(db.String)
    spectrum = db.Column(db.String(20), nullable=False)
    likes_puns = db.Column(db.Boolean, default=True)
    favorite_pet = db.Column(db.String(20))
    spontaneous = db.Column(db.Boolean, default=True)
    into_tech = db.Column(db.Boolean, default=True)
    introvert = db.Column(db.Boolean, default=True)
    liked_users = db.Column(db.ARRAY(db.Integer), default=[])
    blocked_users = db.Column(db.ARRAY(db.Integer), default=[])
    

    @property
    def password(self):
        return self.hashed_password

    @password.setter
    def password(self, password):
        self.hashed_password = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.hashed_password, password)

    def to_dict(self):
        return {"id": self.id,
                "firstName": self.first_name,
                "lastName": self.last_name,
                "gender": self.gender,
                "genderPref": self.gender_pref,
                "imgUrl": self.img_url,
                "spectrum": self.spectrum,
                "likesPuns": self.likes_puns,
                "favPet": self.favorite_pet,
                "spontaneous": self.spontaneous,
                "intoTech": self.into_tech,
                "introvert": self.introvert,
                "liked": self.liked_users,
                "blocked": self.blocked_users
                }


class Message(db.Model):
    __tablename__ = 'messages'
    id = db.Column(db.Integer, primary_key=True)
    sender_id = db.Column(db.Integer, db.ForeignKey('users.id'),
                          nullable=False)
    recipient_id = db.Column(db.Integer, db.ForeignKey('users.id'),
                             nullable=False)
    content = db.Column(db.String, nullable=False)
    seen = db.Column(db.Boolean, default = false)

    def to_dict(self):
        return {
            "id": self.id,
            "createdAt": self.created_at,
            "sender": self.sender_id,
            "recipient": self.recipient_id,
            "content": self.content,
            "seen": self.seen
        }
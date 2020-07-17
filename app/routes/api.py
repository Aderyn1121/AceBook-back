from flask import Blueprint, request, jsonify
import jwt

from ..models import db, User, Message
from ..config import Configuration

api = Blueprint("api", __name__, url_prefix="/api")


@api.route('/users', methods=["GET", "POST"])
def signup():
    print(request.json)
    data = request.json
    user = User(
                first_name=data["firstName"],
                last_name=data["lastName"],
                email=data['email'],
                password=data['password'],
                gender=data['gender'],
                gender_pref=data['genderPref'],
                # img_url=data['imgUrl'],
                spectrum=data['spectrum'],
                likes_puns=data['likesPuns'],
                favorite_pet=data['favPet'],
                spontaneous=data['spontaneous'],
                into_tech=data['intoTech'],
                introvert=data['introvert'],
                liked_users=[],
                blocked_users=[]
                )
    db.session.add(user)
    db.session.commit()

    access_token = jwt.encode({'email': user.email}, Configuration.SECRET_KEY)
    return {'access_token': access_token.decode('UTF-8'),
            'user': user.to_dict()}


@api.route('/<int:userId>/bio', methods=["GET", "POST"])
def post_bio(userId):
    data = request.json
    bio = data['bio']
    user = User.query.filter(id == userId).first()
    user.bio = bio
    db.session.commit()


@api.route('/users/session', methods=["GET", "POST"])
def login():
    data = request.json
    user = User.query.filter(User.email == data['email']).first()
    if not user:
        return {"error": "Email not found"}, 422
    if user.check_password(data['password']):
        access_token = jwt.encode({'email': user.email},
                                  Configuration.SECRET_KEY)
        return {'access_token': access_token.decode('UTF-8'),
                'user': user.to_dict()}
    else:
        return {"error": "Incorrect password"}, 401


@api.route('/people')
def get_people():
    fetchedUsers = User.query.all()
    users = [user.to_dict() for user in fetchedUsers]
    return {"people": users}


@api.route('/messages/<int:userId>', methods=["GET"])
def get_messages(userId):
    fetched_messages = Message.query.filter(
        (Message.sender_id == userId) | (Message.recipient_id == userId)).all()
    messages = [message.to_dict() for message in fetched_messages]
    return jsonify({"messages": messages})


@api.route('/messages/<int:userId>', methods=["POST"])
def post_message():
    data = request.json
    try:
        message = Message(
            sender_id=data['sender'],
            recipient_id=data['recipient'],
            content=data['content']
        )
        db.session.add(message)
        db.session.commit()
        return jsonify({"message": message.to_dict})
    except AssertionError as err_message:
        print(str(err_message))
        return jsonify({"error": str(err_message)}), 400


@api.route('/like/<int:likedUserId>', methods=["POST"])
def like_user(likedUserId):
    data = request.json
    liker_id = data['likerId']
    user = User.query.filter_by(id=liker_id).first()
    user.liked_users = user.liked_users.append(likedUserId)
    db.session.commit()  


@api.route('/unlike/<int:unlikedId>', methods=["POST"])
def unlike(unlikedId):
    data = request.json
    unlikerId = data['unlikerId']
    user = User.query.filter_by(id=unlikerId)
    user.liked_users.remove(unlikedId)
    db.session.commit()

@api.route('/messages/<int:id>/markSeen')
def markSeen(msgId):
    data = request.json
    senderId = data['senderId']
    userId = data['userId']
    messages = Message.query.filter(Message.sender_id == senderId,
                                    Message.recipient_id == userId,
                                    id <= msgId).all()
  
    for message in messages:
        message['seen'] = True

    db.session.commit()

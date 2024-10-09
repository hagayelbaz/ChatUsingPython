from app import db
from datetime import datetime

class Conversation(db.Model):
    """"
    A conversation is a collection of messages between two users.
    """
    id = db.Column(db.Integer, primary_key=True)
    created_at = db.Column(db.DateTime, default=datetime.now())

    def to_dict(self):
        return {
            'id': self.id,
            'created_at': self.created_at.isoformat()
        }

class Message(db.Model):
    """
    A message is a text message sent by a user in a conversation.
    """
    id = db.Column(db.Integer, primary_key=True)
    conversation_id = db.Column(db.Integer, db.ForeignKey('conversation.id'), nullable=False)
    text = db.Column(db.String(4000), nullable=False)
    role = db.Column(db.String(50), nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.now())

    conversation = db.relationship('Conversation', backref=db.backref('messages', lazy=True))

    def to_dict(self):
        return {
            'id': self.id,
            'conversation_id': self.conversation_id,
            'text': self.text,
            'role': self.role,
            'created_at': self.created_at.isoformat()
        }

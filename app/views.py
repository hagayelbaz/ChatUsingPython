from app import db, socketio
from flask import Blueprint, render_template
from .utils import format_date
from .models import Message

views = Blueprint('views', __name__)

@views.route('/')
def app():
    return render_template('index.html')


@views.route('/ask')
def ask():
    all_messages = Message.query.order_by(Message.id.asc()).all()
    return render_template('chat.html', messages=all_messages, format_date=format_date)

@socketio.on('new_message')
def handle_new_message(message):
    user_msg = Message(role="user", message=message)
    bot_msg = Message(role="bot", message="I'm a bot, I don't know what to say")
    db.session.add(user_msg)
    db.session.add(bot_msg)
    db.session.commit()

    socketio.emit('new_message', {'bot_msg': bot_msg.message})

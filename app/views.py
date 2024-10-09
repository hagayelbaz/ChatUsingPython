from app import db, socketio
from flask import Blueprint, render_template
from .openai_integration import get_openai_response
from .utils import format_date
from .models import Message, Conversation


views = Blueprint('views', __name__)

# This route for the main page of the app
@views.route('/')
def app():
    return render_template('index.html')


# This route for the chat page of the app
@views.route('/ask')
def ask():
    conversation = Conversation.query.first()
    if not conversation:
        return render_template('chat.html', messages=[], format_date=format_date)

    return render_template('chat.html', messages=conversation.messages, format_date=format_date)


# When a new message is received from the client, this function is called
@socketio.on('new_message')
def handle_new_message(message):
    conversation = Conversation.query.first()

    if not conversation:
        conversation = Conversation()
        db.session.add(conversation)

    user_msg = Message(role="user", text=message, conversation=conversation)
    db.session.add(user_msg)
    response = get_openai_response(conversation)
    bot_msg = Message(role="assistant", text=response, conversation=conversation)
    db.session.add(bot_msg)
    db.session.commit()

    socketio.emit('new_message', {'bot_msg': bot_msg.text})

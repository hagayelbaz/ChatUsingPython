(() => {
    'use strict';
    const socket = io();

    /* region Socket */
    socket.on('new_message', function (data) {
        const {bot_msg} = data;
        updateUI({role: 'bot', message: bot_msg, created_at: new Date()});
    });
    /* endregion */

    /* region emit */
    const sendMessages = (message) => {
        const optimisticMessage = {message, role: 'user', created_at: new Date()};
        updateUI(optimisticMessage, true);
        socket.emit('new_message', message);
        document.getElementById('message').value = '';
    }
    /* endregion */

    /* region UI */
    const scrollToBottom = () => {
        const chatContainer = document.getElementById('chartMain');
        chatContainer.scrollTop = chatContainer.scrollHeight;
    }

    const updateUI = (message) => {
        const container = document.getElementById('chatContainer');
        const msgDiv = document.createElement('div');
        msgDiv.innerHTML = message.role === 'user' ? htmlUser(message) : htmlBot(message);
        container.appendChild(msgDiv);
        scrollToBottom();
    }

    const formatDate = (date) => {
        if (isNaN(date.getTime())) {
            return '-/-';
        }

        let day = date.getDate();
        let month = date.getMonth() + 1;
        return `${day}.${month}`;
    }
    /* endregion */

    /* region HTML */
    const htmlUser = (message) => {
        return `
        <div class="text-end mt-4 container-fluid position-relative"> 
            <div class="primary-bg-light rounded-pill p-2 d-inline-block" style="max-width: 50%;">
                <p class="m-2">${message.message}</p>
            </div>
            <p class="bubble-user primary-bg small rounded-pill mx-3 p-1 px-2"> 
                ${formatDate(new Date(message.created_at))}
            </p>
        </div>
    `;
    }

    const htmlBot = (message) => {
        return `
        <div class="position-relative mt-4">
            <div class="d-flex align-items-center ms-auto">
                <svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 32 32" class="me-2">
                    <path fill="currentColor" d="M18 10h2v2h-2zm-6 0h2v2h-2z"/>
                    <path fill="currentColor" d="M26 20h-5v-2h1a2 2 0 0 0 2-2v-4h2v-2h-2V8a2 2 0 0 0-2-2h-2V2h-2v4h-4V2h-2v4h-2a2 2 0 0 0-2 2v2H6v2h2v4a2 2 0 0 0 2 2h1v2H6a2 2 0 0 0-2 2v8h2v-8h20v8h2v-8a2 2 0 0 0-2-2M10 8h12v8H10Zm3 10h6v2h-6Z"/>
                </svg>
                <div class="primary-bg-light rounded-pill p-2">
                    <p class="m-2">${message.message}</p>
                </div>
            </div>
            <p class="bubble-bot small primary-bg rounded-pill mx-3 px-1"> 
                ${formatDate(new Date(message.created_at))}
            </p>
        </div>
    `;
    }
    /* endregion */


    document.getElementById('chatForm').addEventListener('submit', function (e) {
        e.preventDefault();
        const message = document.getElementById('message').value;
        if (message) {
            sendMessages(message);
        }
    });

})();
console.log('funciona');


const roomName = JSON.parse(document.getElementById('room-name').textContent);

const chatSocket = new WebSocket(
    'ws://'
    + window.location.host
    + '/ws/chat/'
    + roomName
    + '/'
);

chatSocket.onmessage = function (e) {
    const data = JSON.parse(e.data);
    document.querySelector('#chat-log').value += (data.message + '\n');
    var mensaje = data.message;
    var usuario = data.username
    var chat_nuevo =
        '  <div class="chat_list active_chat" id=chat_list>' +
        '  <div class="chat_people">' +
        ' <div class="chat_img"> <img' +
        ' src="https://ptetutorials.com/images/user-profile.png" alt="sunil">' +
        '</div>   <div class="chat_ib">' +
        ' <h5>' + usuario + ' <span class="chat_date">Dec 25</span>' +
        ' <p> ' + mensaje + '  </h5>' +
        ' </div></div></div>'



    $('#chat_nuevo').append(chat_nuevo);




};

chatSocket.onclose = function (e) {
    console.error('Chat socket closed unexpectedly');

};

document.querySelector('#chat-message-input').focus();
document.querySelector('#chat-message-input').onkeyup = function (e) {
    if (e.keyCode === 13) {  // enter, return
        document.querySelector('#chat-message-submit').click();
    }
};

document.querySelector('#chat-message-submit').onclick = function (e) {
    const messageInputDom = document.querySelector('#chat-message-input');
    const message = messageInputDom.value;
    chatSocket.send(JSON.stringify({
        'message': message
    }));
    messageInputDom.value = '';
};




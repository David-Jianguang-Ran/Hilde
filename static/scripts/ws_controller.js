// this module handles the ws connection

var webSocketConnection = new WebSocket("ws://127.0.0.1:8000/ws/live/");

export var incomingMessage = {
    "flag": false,
    "content": null
};

export var outgoingMessage = {
    "flag": false,
    "content": null
};

const send_message = function(message){
    webSocketConnection.send(JSON.stringify(message.content));
    message.flag = false;
};
outgoingMessage.watch("flag",send_message(outgoingMessage))

// send custom handshake msg on open
webSocketConnection.onopen = function (event) {
    const subProtocolHandShake = {
        "type":"custom.protocol.handshake",
    };
    webSocketConnection.send(JSON.stringify(subProtocolHandShake))
};

// on message, data is decoded and stored in exported var incomingMsg
webSocketConnection.onmessage = function (event) {
    let textData = JSON.parse(event.data);
    incomingMessage = textData
};
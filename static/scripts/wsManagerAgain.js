
class WebSocketManager {
    // this obj is to be init and passed to the top level component as a prop in entry point
    // any child component can call this.prop.wsManager.sendJSON to send data
    // for an component to receive data, it must:
    // 1) write method used to handle incoming message in the class based component
    // 2) in component did mount or constructor (I haven't decided/tested constructor)
    // call addMessageListener with the string key and the message handler (don't call it with ())
    constructor(url) {
        this.outstandingMessage = false
        this.messageRoutingTable = {
            "messageKey":"messageHandler"
        }
        this.sendJSON = this.sendJSON.bind(this)
        this.messageSwitcher = this.messageSwitcher.bind(this)
        this.addMessageListener = this.addMessageListener.bind(this)
        this.ws = new WebSocket(url)
        this.ws.addEventListener('message', this.messageSwitcher)
        console.log("ws connection initialized")
    }
    sendJSON(obj) {
        let data = JSON.stringify(obj)
        this.ws.send(data)
        console.log("ws message sent")
    }
    messageSwitcher(event) {
        let obj = JSON.parse(event.data)
        console.log(obj.key)
        for (let key in this.messageRoutingTable) {
            console.log(key)
            if (key == obj.key) {
                this.messageRoutingTable[key](obj)
            }
        }
        console.log("ws received with key" + obj.key)
        console.log(event)
    }
    addMessageListener(key, method) {
        this.messageRoutingTable[key] = method
        console.log("ws message listener added wit key" + key)
        console.log(this.messageRoutingTable)
    }
}

export default WebSocketManager




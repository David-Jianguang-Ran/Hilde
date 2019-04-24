export default class WebSocketManager {
    // this obj is to be init and passed to the top level component as a prop in entry point
    // any child component can call this.prop.wsManager.sendJSON to send data
    // for an component to receive data, it must:
    // 1) write method used to handle incoming message in the class based component
    // 2) in component did mount or constructor (I haven't decided/tested constructor)
    // call addMessageListener with the string key and the message handler (don't call it with ())
    constructor(path,token = null) {
        this.outstandingMessage   = false
        this.messageRoutingTable  = {
            "messageKey":"messageHandler"
        }
        this.sendJSON             = this.sendJSON.bind(this)
        this.messageSwitcher      = this.messageSwitcher.bind(this)
        this.addMessageListener   = this.addMessageListener.bind(this)

        let target_url            = window.location.hostname + path + token
        this.ws                   = new WebSocket(target_url)
        this.ws.addEventListener('message', this.messageSwitcher)
    }

    addMessageListener (key, method) {
        this.messageRoutingTable[key] = method
        console.log("ws message listener added wit key" + key)
        console.log(this.messageRoutingTable)
    }

    sendJSON (message,replyHandler) {
        /*
        New feature in type19:
        Now components can call sendJSON and give it an callback to handle returned data
         */
        if (replyHandler !== null) {
            let reply_key         =
            message.reply_key     = reply_key
            this.addMessageListener(reply_key,function (event) {
                // remove message listener
                delete this.messageRoutingTable[reply_key]
                // pass event along to replyhandler
                replyHandler(event)
            })
        }

        let data                  = JSON.stringify(message)
        this.ws.send(data)
    }

    messageSwitcher (event) {
        let obj                   = JSON.parse(event.data)
        for (let key in this.messageRoutingTable) {
            console.log(key)
            if (key             === obj.key) {
                this.messageRoutingTable[key](obj)
            }
        }
    }

}
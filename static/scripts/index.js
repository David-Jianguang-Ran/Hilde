import React from 'react'
import ReactDOM from 'react-dom'

import TestApp from './app'
import WebSocketManager from './wsManagerAgain'

// this is the entry point of the app
const url = "ws://127.0.0.1:8000/ws/live/"
// initialize a ws connection and pass it to your top level app as a prop
let ws = new WebSocketManager(url)

const rootContainer = document.getElementById('react_container')

ReactDOM.render(
    <TestApp wsManager={ws}/>,
    rootContainer
)
import React from 'react'
import ReactDOM from 'react-dom'

import TestApp from './app'

const rootContainer = document.getElementById('react_container')

let wsConnection = new WebSocket("ws://127.0.0.1:8000/ws/live/")

ReactDOM.render(
    <TestApp wsConnection={wsConnection}/>,
    rootContainer
)
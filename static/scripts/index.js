import React from 'react'
import ReactDOM from 'react-dom'
import DataComponent from './app'

const rootContainer = document.getElementById('reactContainer')
var element = DataComponent()

ReactDOM.render(
    element,
    rootContainer
)
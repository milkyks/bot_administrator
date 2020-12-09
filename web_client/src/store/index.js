import {applyMiddleware, combineReducers, compose, createStore} from 'redux'
import thunk from 'redux-thunk'
import commands from '../slices/commandsSlice'

const reducers = combineReducers({commands})

export default createStore(reducers, applyMiddleware(thunk))


// https://github.com/zalmoxisus/redux-devtools-extension

// const composeEnhancers = window.__REDUX_DEVTOOLS_EXTENSION_COMPOSE__ || compose
// export default createStore(reducers, composeEnhancers(applyMiddleware(thunk)))
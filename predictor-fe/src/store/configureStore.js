import {createStore,combineReducers} from 'redux'
import {classifiersReducer} from './reducers/classifiersReducer'


const configureStore=()=>{
    const store = createStore(combineReducers(
        {
            classifiers:classifiersReducer
        }
    ))

    return store
}

export default configureStore
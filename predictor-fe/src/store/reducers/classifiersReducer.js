const initialState = {knn:'',nb:'',lrc:''}
export const classifiersReducer=(state=initialState,action)=>{
    switch(action.type){
        case 'KNN_CLASSIFIER':state['knn'] = action.payload 
                                return state 
        case 'NAIVE_BAYES_CLASSIFER': state['nb'] = action.payload 
                                    return state
        case 'LOGISTIC_CLASSIFIER': state['logistic'] = action.payload
                                return state
        default:return state
    }
}
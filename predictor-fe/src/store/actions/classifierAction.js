import axios from 'axios'

export const setPrediction=(type, data)=>{
    return {type:type, payload:data}
}
export const startGetPrediction=()=>{
    Promise.all([axios.get('/knn').then((response)=>{
        return(dispatch)=>{
            dispatch(setPrediction('knn', response.data))
        }
    }).catch((err)=>{
        console.log("Error in getting the knn prediction")
    }),
    axios.get('/logistic').then((response)=>{
        return(dispatch)=>{
            dispatch(setPrediction('logistic', response.data))
        }
    }).catch((err)=>{
        console.log("Error in getting the knn prediction")
    }),
    axios.get('/nb').then((response)=>{
        return(dispatch)=>{
            dispatch(setPrediction('nb', response.data))
        }
    }).catch((err)=>{
        console.log("Error in getting the knn prediction")
    })
])
}
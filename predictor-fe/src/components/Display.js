import React from 'react'
//import {connect} from 'react-redux'
//import startGetPrediction from '../store/actions/classifierAction'
import axios from 'axios'
import "./Display.css"

class Display extends React.Component{
    constructor(){
        super()
        this.state={
            statement:'', 
            knn:'',
            logistic:'',
            nb:'',
            knnAccuracy:0,
            logisticAccuracy:0,
            nbAccuraccy:0
        }
    }

    handleChange=(e)=>{
        this.setState({statement:e.target.value})
    }

    handlePredictor(){
        //this.props.dispatch(startGetPrediction)
        Promise.all([axios.get('localhost:3055/knn').then((response)=>{
            this.setState({knn:response.data.knnVal, knnAccuracy:response.data.knnAccuracy})
        }).catch((err)=>{
            console.log("Error in getting the knn prediction")
        }),
        axios.get('localhost:3055/logistic').then((response)=>{
            this.setState({logistic:response.data.logVal, logisticAccuracy:response.data.logisticAccuracy})
        }).catch((err)=>{
            console.log("Error in getting the logistic prediction")
        }),
        axios.get('localhost:3055/nb').then((response)=>{
            this.setState({nb:response.data.nbVal, nbAccuraccy:response.data.nbAccuraccy})
            }).catch((err)=>{
            console.log("Error in getting the naive bayes prediction")
        })
    ])
    }
    render()
    {
        return(
            <div class="centered">
                <label for="exampleFormControlTextarea4">Enter the Statement</label><br/>
                <textarea  id = "exampleFormControlTextarea4" class="form-control" rows="3" name="statement" value={this.state.statement} onChange={this.handleChange}/>
                <br/><button type="button" class="btn btn-primary" onChange={this.handlePredictor}>Predict Mood</button><br/>
                <p class="text-success"> Knn predicted the sentence given sentence belongs to {this.state.knn} with accuracy {this.state.knnAccuracy} </p>
                <p class="text-danger"> logistic regression predicted the  given sentence  belongs to {this.state.logistic} with accuracy {this.state.logisticAccuracy} </p>
                <p class="text-warning">Knn predicted the sentence given sentence belongs to {this.state.nb} with accuracy {this.state.nbAccuraccy}</p>
            </div>
        )
    }
}

export default Display
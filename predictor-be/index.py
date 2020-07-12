from flask import Flask
import predict from "./model" 

app = flask(__name__)

@app.route("/")
def home():
    return "Welcome to predictor"

def executeClassifier(request, classifier):
    if request.method == 'POST':
        try:
            data = request.get_json()
            statement = data["statement"]

            result = classifier(statement)
        except:
            return jsonify("Please enter the sentence")
        return jsonify(result)

@app.route("/nb", methods=['POST'])
def naiveBayes():
    executeClassifier(request, naiveBayseClassifier)
    
@app.route("/knn", methods=['POST'])
def knn():
    executeClassifier(request, knnClassifier)

@app.route("/logistic", methods=['POST'])
def logistic():
    executeClassifier(request, logisticClassfier)

if __name__ == "__main__":
    app.run(debug=True)




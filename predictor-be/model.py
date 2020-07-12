import pandas as pd

stopwords= set(['br', 'the', 'i', 'me', 'my', 'myself', 'we', 'our', 'ours', 'ourselves', 'you', "you're", "you've",\
            "you'll", "you'd", 'your', 'yours', 'yourself', 'yourselves', 'he', 'him', 'his', 'himself', \
            'she', "she's", 'her', 'hers', 'herself', 'it', "it's", 'its', 'itself', 'they', 'them', 'their',\
            'theirs', 'themselves', 'what', 'which', 'who', 'whom', 'this', 'that', "that'll", 'these', 'those', \
            'am', 'is', 'are', 'was', 'were', 'be', 'been', 'being', 'have', 'has', 'had', 'having', 'do', 'does', \
            'did', 'doing', 'a', 'an', 'the', 'and', 'but', 'if', 'or', 'because', 'as', 'until', 'while', 'of', \
            'at', 'by', 'for', 'with', 'about', 'against', 'between', 'into', 'through', 'during', 'before', 'after',\
            'above', 'below', 'to', 'from', 'up', 'down', 'in', 'out', 'on', 'off', 'over', 'under', 'again', 'further',\
            'then', 'once', 'here', 'there', 'when', 'where', 'why', 'how', 'all', 'any', 'both', 'each', 'few', 'more',\
            'most', 'other', 'some', 'such', 'only', 'own', 'same', 'so', 'than', 'too', 'very', \
            's', 't', 'can', 'will', 'just', 'don', "don't", 'should', "should've", 'now', 'd', 'll', 'm', 'o', 're', \
            've', 'y', 'ain', 'aren', "aren't", 'couldn', "couldn't", 'didn', "didn't", 'doesn', "doesn't", 'hadn',\
            "hadn't", 'hasn', "hasn't", 'haven', "haven't", 'isn', "isn't", 'ma', 'mightn', "mightn't", 'mustn',\
            "mustn't", 'needn', "needn't", 'shan', "shan't", 'shouldn', "shouldn't", 'wasn', "wasn't", 'weren', "weren't", \
            'won', "won't", 'wouldn', "wouldn't"])

def decontracted(line):
    line = re.sub(r"won't", "will not", line)
    line = re.sub(r"can\'t", "can not", line)
    line = re.sub(r"n\'t", " not", line)
    line = re.sub(r"\'re", " are", line)
    line = re.sub(r"\'s", " is", line)
    line= re.sub(r"\'d", " would", line)
    line= re.sub(r"\'ll", " will", line)
    line= re.sub(r"\'t", " not", line)
    line = re.sub(r"\'ve", " have", line)
    line = re.sub(r"\'m", " am", line)
    return line

def text_preprocessing(sentance):
    sentance = re.sub(r"http\S+", "", sentance)
    sentance = BeautifulSoup(sentance, 'lxml').get_text()
    sentance = decontracted(sentance)
    sentance = re.sub("\S*\d\S*", "", sentance).strip()
    sentance = re.sub('[^A-Za-z]+', ' ', sentance)
    sentance = ' '.join(e.lower() for e in sentance.split() if e.lower() not in stopwords)
    return sentance.strip()

def predict(string):
    #clf = joblib.load('model.pkl')
    #count_vect = joblib.load('count_vect.pkl')
    classification = model()
    statement = clean_text(string)
    test_vect = count_vect.transform(([statement]))
    pred = clf.predict(test_vect)
    print(pred[0])
    if pred[0]:
        prediction = "happy"
    elif pred[1]:
        prediction = "sad"
    elif pred[2]:
        prediction = "angry"
    return prediction

con = sqlite3.connect('database.sqlite')
filtered_data = pd.read_sql_query(""" SELECT * FROM moods""", con)

preprocessed_statements = []
for sentence in filtered_data['sentence'].values:
    preprocessed_statements.append(clean_text(sentence))

def model():
    count_vect = CountVectorizer()
    count_vect.fit(preprocessed_statement)
    #joblib.dump(count_vect, 'count_vect.pkl')
    X = count_vect.transform(preprocessed_statement)
    print(X.shape)
    #classification = change model to naive bayes 
    classification.fit(X, Y)
    joblib.dump(classification, 'model.pkl')
    return classification

def logisticClassifier():
    pass

def knnClassifier():
    pass

def naiveBayseClassifier():
    pass


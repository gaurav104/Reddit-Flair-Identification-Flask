import pandas as pd
from joblib import load
from .preprocessor import normalizeString
import praw
import json 

label_to_id = {"Business/Finance" : 0,
"Policy/Economy" : 1,
"[R]eddiquette" : 2,
"Food" : 3,
"Science/Technology" : 4,
"Sports" : 5,
"Photography" : 6,
"Politics" : 7,
"AskIndia" : 8,
'CAA-NRC' : 9,
'Coronavirus' : 10,                         
}

id_to_label = {v: k for k, v in label_to_id.items()}

def js_r(filename):
    with open(filename) as f_in:
        return(json.load(f_in))


def predict_flair(inp_url):

    model = load('./model/model_svc.joblib')
    credentials = js_r("./support/config.json")
    reddit = praw.Reddit(client_id=credentials['client_id'], client_secret=credentials['client_secret'], password=credentials["password"], user_agent=credentials["user_agent"], username=credentials["username"])

    try:
        post = reddit.submission(url=inp_url)
    except:
        return {'text':"Please Check the URL Entered"}

    X = {"title": [], "selftext": []}
    X['title'].append(post.title)
    X['selftext'].append(post.selftext)
    X['title_selftext'] = " ".join(X['title'] + X['selftext'])

    #preprocessing
    X_input = normalizeString(X['title_selftext'])

    pred = model.predict([X_input])[0]
    class_id = int(pred)
    label = id_to_label[class_id]

    return {'text': 'Predicted Flair is : {}'.format(label), 'label': label}
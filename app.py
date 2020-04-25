# this will provide the bridge between front end and the model

import numpy as np
from flask import Flask, request, jsonify, render_template
import pickle
import pandas as pd
import praw #PRAW is the API being used to scrap data from Reddit
from bs4 import BeautifulSoup as bs
import re
import nltk
from nltk.corpus import stopwords
nltk.download('stopwords')


app = Flask(__name__)
model = pickle.load(open('model.pkl', 'rb'))

@app.route('/')
def home():
	return render_template('index.html')


def transformText(rawText):
    """
    This function takes a raw string review as input, and applies the following steps to return a refined string review as output:
    1. removing HTML tags
    2. removing punctuation marks
    3. converting the text to lower case
    4. splitting the string into words
    5. removing stop words
    """
    # remove HTML tags
    noHtml = bs(rawText, "lxml").get_text()
    
    #remove punctuation marks
    letters_only = re.sub("[^a-zA-Z ]", "", noHtml)
    
    #convert to lower case
    tolower = letters_only.lower()
    
    #split
    words = tolower.split()
    
    #convert stopwords list to set for fast searching
    stopwordsSet = set(stopwords.words("english"))
    
    #remove stop words
    RefinedWords = [w for w in words if w not in stopwordsSet]
    
    #form new review
    return(" ".join(RefinedWords) )



@app.route('/predict', methods=['POST'])
def predict():
	reddit = praw.Reddit(client_id='', client_secret=' ', user_agent=' ', password=' ', username=' ')

	extractedUrl = dict(request.form)

	extractedUrl = str(extractedUrl['url'])


	submission = reddit.submission(url=extractedUrl) 

	# extract title which is our current feature

	feature = submission.title 
	
	feature = [transformText(feature)]

	prediction = model.predict(feature)

	# pass this to the predict page (which is our index page only)
	return render_template('index.html', prediction_text="Post Flair predicted: {}".format(prediction))


if __name__ == "__main__":
	app.run(debug=True)
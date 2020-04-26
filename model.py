#!/usr/bin/env python
# coding: utf-8

# ## This notebook pre-processed data and trains different machine learning models

# In[1]:


import numpy as np
import pandas as pd
import nltk
import pickle

# In[2]:


dataset = pd.read_csv('refinedmorefeaturesDataset.csv')
dataset.head()


# ## Building Model Functions

# In[6]:


from sklearn.pipeline import Pipeline
from sklearn.feature_extraction.text import TfidfTransformer
from sklearn.metrics import classification_report
from sklearn.feature_extraction.text import CountVectorizer, TfidfVectorizer
from sklearn.metrics import accuracy_score, confusion_matrix


def random_forests(X_train, X_test, y_train, y_test):
    from sklearn.ensemble import RandomForestClassifier
    
    rf = Pipeline([('vect', CountVectorizer()),
                 ('tfidf', TfidfTransformer()),
                 ('clf', RandomForestClassifier()),
                ], verbose=True)
    rf.fit(X_train, y_train)
    
    y_pred = rf.predict(X_test)
    
    print('accuracy %s' % accuracy_score(y_pred, y_test))
    print(classification_report(y_test, y_pred))

    return rf


from sklearn.model_selection import train_test_split


# In[14]:


X = dataset.Title
y = dataset.Flair

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.33, random_state=42)

print("Original dataset size: ", X.shape)
print("Training dataset size: ", X_train.shape)



model = random_forests(X_train, X_test, y_train, y_test)

# Saving model to disk
pickle.dump(model, open('model.pkl','wb'))

model = pickle.load(open('model.pkl', 'rb'))
print(model.predict(["delhi deputy chief minister manish sisodia decided ban activity people gather huge numbers like ipl social distancing important curb breakout"]))




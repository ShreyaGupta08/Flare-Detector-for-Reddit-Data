# Flare-Detector-for-Reddit-Data

Flair detector is a web application, deployed using Heroku. The application can be seen [here](https://flair-detector-for-reddit.herokuapp.com). It scrapes post's using the URL and then uses an SVC model to predict the flair of that post

This repository contains the code which performs the following functionalities:
1. Scrapping posts from Indian Subreddit according to two methods: hottest posts and distributed posts in accordance with flairs
2. Exploratory Data Analysis: contains bar graphs and pie-charts to analyse data distributions for the attributes collected in step 1.
3. Textual Pre-Processing: pre-processes textual data for attributes like Title of the post and Content of the posts.
4. Building and contrasting different models: Builds, trains and validates four ML models, Naive Bayes, Random Forest, Logistic Regression and Multi-layer Perceptron using different features and then selects the feature-model pair performing the best.
5. Building Web Application: Contains the code to build a basic web application that takes as input a post url and displays the predicted flair of the post.
6. Hosts the app on Heroku.


## Organisation of the Repository:

- [Jupyter Notebooks](https://github.com/ShreyaGupta08/Flare-Detector-for-Reddit-Data/tree/master/Jupyter%20Notebooks): contains data extraction, exploration, pre-processing and model building ipynb (or Jupyter) notebooks.
- [Dataset](https://github.com/ShreyaGupta08/Flare-Detector-for-Reddit-Data/tree/master/Dataset): contains different datasets obtained by following different extraction methods. dataset.csv was the first draft created by extracting hottest posts. newdataset.csv was the second draft created by distributed flairs method. morefeaturesDataset.csv was the third draft which contains comments as well. refinedmorefeaturesDataset.csv is the dataset obtained after pre-processing morefeaturesDataset.csv and is used for training.
- [templates](https://github.com/ShreyaGupta08/Flare-Detector-for-Reddit-Data/tree/master/templates): contains the front end of the web app in index.html file
- Procfile: contains the command which are required to run the flask based app on Heroku.
- app.py: The Main Python file for Flask Based Web App.
- model.py: final model that uses title of the post and random forest to predict its flair.
- model.pkl: pickled-version of the model which is used to make predictions.
- requirments.txt: txt file for Heroku to download the required requirements to run the web application.
- Experimental log.ipynb: Documents everything that worked or failed on a day per day basis. (for personal use) 

## How to run this code in your local machine

1. Go to the directory in which you want to download the repository using:

```bash
cd ~/target directory
```

2. Clone this repository in your local machine using the following command:

```bash
git clone https://github.com/ShreyaGupta08/Flare-Detector-for-Reddit-Data.git
```

3. Enter this directory using the following command:

```bash
cd Flare-Detector-for-Reddit-Data
```

4. - (Optional) Create Virtual environment (good coding practice):
```bash
virtualenv env
```
- If you want your virtualenv to also inherit globally installed packages run:
```bash
virtualenv venv --system-site-packages
```
- Activate your virtual env

```bash
source venv/bin/activate 
```
4. (If you're a first-time user) Download the requirements from requirements.txt:

For Python 2:
```bash
pip install -r requirements.txt
```
For Python 3:
```bash
pip3 install -r requirements.txt
```

5. Copy paste the jupyter notebooks from Jupyter Notebooks folder in the Dataset folder using the following command:

```bash
cp -r Jupyter\ Notebooks/ Dataset/
```

6. run the main flask API file, app.py using the following command:

```bash
python app.py
```
7. Copy Paste the server address (generally http://127.0.0.1:5000/)

Voila!

(If you face any errors, feel free to issue a pull request)

P.S. I've also added my experiment log to document everything that worked or failed. 





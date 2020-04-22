# Reddit Flair Identification

A flask app for flair Identification for [r/india](https://www.reddit.com/r/india/) subreddit, which takes a r/india posts' URL and predicts the flair of the post.
 The web-application is hosted on Heroku at [https://redditflairid.herokuapp.com/)](https://redditflairid.herokuapp.com/).
 
 Python packages used
- PRAW
- Scikit-learn
- NLTK
- Numpy
- Pandas
- Flask
 ```
The requirements.txt file contains all the dependencies used in the notebook and for developing the flask app. 
```
## Directory Structure

- [model](link): Contains the trained ML model which makes the prediction
-  [notebooks](link): containes jupyter notebooks of data scrapping, preprocessing, EDA and classification
- [static](link): Contains the [main.css](link) file, used as for frontend.
- [support](link): Contains the scripts for prediction and preprocessing of the text data and config.json.
- [templates](link): Contains HTML files for the web-application
- [app.py](link): File to run to start the web application
- [requirements.txt](link): dependendancies
 ```
Edit "config.json" and add in your PRAW credentials
```

## Usage
Posts in r/india can be corresponding to multiple topics. Each post is tagged for filtering purposes. These tags are called a flares in the reddit world. r/india has flairs like Politics, AskIndia, Science/Technology etc.
The web-application allows the user to enter a r/india URL and displays the predicted flair for the submitted post. 

To run on a local server:
1. Clone the repository
```
git clone https://github.com/gaurav104/Reddit-Flair-Identification-Flask.git
```
2. Create a virtual environment
```
python3 -m venv flair_detector
source flair_detector/bin/activate
cd Reddit-Flair-Identification-Flask/
```
3. Install the project dependencies
```
pip3 install -r requirements.txt
```
4. To run the server locally, execute the following command
```
python3 app.py
```

## Approach 
In the notebook folder

 - [Data Scraping.pynb](link%20dalna%20hai): Depicts the data scrapping process using Pushshift and praw API.
 
 - [Text Preprocessing.ipynb](link): This notebook describes the data cleaing and preprocessing process, which include steps such as punctuation removals, stopword removal, lemmatization, tokenization, etc.
 
 - [EDA.ipynb](link): In this notebook, Exploratory Data Analysis is performed on the cleaned data, we look for average post lengths and words present, perform topic modelling using LDA(Latent Dirichlet Allocation) and NMF(Non-negative Matrix Factorization).
 
 - [Classification.ipynb](link): Performing classification on the pre-processes data and performing model evaluation and analysis on the predicted and actual labels
 
 notebooks to be added soon



## Future Additions
1. Improving the prediction by automatic model parameter update, by training on post from r/india.
2. Incorporating DL models, LSTMs/GRUs, Bert.


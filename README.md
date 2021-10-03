# ec602_Project_2
# Phase2 - Google NLP
In this task, I use Google NLP API to score the sentiment of the tweets I searched with tweepy in phase 1.  
## Setting up authentication
To begin with, you need to login in Google Cloud Platform, and create a project: https://cloud.google.com/natural-language  
  
Next, create a service account key for the project with the following steps:  
In the Cloud Console, click the email address for the service account that you created.  
1.Click Keys.  
2.Click Add key, then click Create new key.  
3.Click Create. A JSON key file is downloaded to your computer.  
  
Provide authentication credentials to your application code by setting the environment variable GOOGLE_APPLICATION_CREDENTIALS. This variable only applies to your current shell session, so if you open a new session, set the variable again.
```
export GOOGLE_APPLICATION_CREDENTIALS="KEY_PATH"
```
Replace KEY_PATH with the path of the JSON file that contains your service account key.  
## GoogleAPI.py
In my code, I analyze the sentiment of Taylor Swift's last 10 tweets searched by tweepy.  
To run program, firstly you may need to impport the module 'google.cloud' with the command below:
```
python3 -m pip install google.cloud --user
```
Then run the analysis program with:
```
py GoogleNLP.py
```
A json file output(taylor.py) will be automatically generated to show each tweets' sentiment score and magnitude in the format below:
``` json
{
    "name": "Taylor Swift",
    "moment": "Fri Sep 17 13:18:53",
    "text": "Hi! Saw you guys got Wildest Dreams trending on tiktok, thought you should have my version \ud83d\ude18\ud83d\ude18\ud83d\ude18\ud83d\ude18\u2026 https://t.co/LtkfAItbUp",
    "sentiment.score": 0.5,
    "sentiment.magnitude": 1.5
}
```
  

# ec602_Project_2
# Phase1 - Twitter API
Phase1's readme is in the file 'project2-phase1-readme.docx'.  
# Phase2 - Google NLP
In phase2, I use Google Cloud Language API to score the sentiment of the tweets I searched with tweepy in phase 1.  
## Requirements
To begin with, you need to login in Google Cloud Platform, and create a project: https://cloud.google.com/natural-language  
  
Next, create a service account key for the project with the following steps:  
In the Cloud Console, click the email address for the service account that you created.  
1.Click Keys.  
2.Click Add key, then click Create new key.  
3.Click Create. A JSON key file is downloaded to your computer.  
  
Provide authentication credentials to your application code by setting the environment variable GOOGLE_APPLICATION_CREDENTIALS. This variable only applies to your current shell session, so if you open a new session, set the variable again.
```
$env:GOOGLE_APPLICATION_CREDENTIALS="KEY_PATH""
```
Replace KEY_PATH with the path of the JSON file that contains your service account key.  
## Google.cloud.language_v1
In my code, I analyze the sentiment of President Biden's last 10 tweets searched by tweepy.  
To run program, firstly you may need to impport the module 'google.cloud' with the command below:
```
pip install google-cloud-language
```
Then run the analysis program in terminal:
```
py GoogleNLP.py
```
A json file output(biden.py) will be automatically generated to show each tweets' sentiment score and magnitude in the format below:
``` json
{
    "name": "President Biden",
    "moment": "Sun Oct 03 19:00:00",
    "text": "A historic tax cut for the middle class. \nLower everyday costs for hardworking Americans.\nAn economy that gives eve\u2026 https://t.co/cqIagpbwS3",
    "sentiment.score": 0.30000001192092896,
    "sentiment.magnitude": 1.0
}
```
  

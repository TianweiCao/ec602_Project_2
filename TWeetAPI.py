import tweepy
import Keys  # .py file that store all necessary keys
import sys
import json  # To write file as json format


def Authorization_Setup():
    auth = tweepy.OAuthHandler(Keys.consumer_key, Keys.consumer_secret) #pass customer keys
    auth.set_access_token(Keys.access_token, Keys.access_token_secret) #pass access_token and access_token_secret
    api = tweepy.API(auth, wait_on_rate_limit=True)
    return api #generate the api

# Print out tweets' text.!!!
def Display_tweets(Input_list):
    tweet_text_list = []
    for status in Input_list:
        tweet_text_list.append(status.text)
        print(status.text, end="\n\n")
    return tweet_text_list


# Write tweets information to file as json format.!!!
def Write_tweets_to_File(Input_list, target_filename):
    data = []
    filename = "%s.json" % target_filename
    Tweets_text = open(filename, 'w')
    for status in Input_list:
        data.append(status._json)
    json.dump(data, Tweets_text)
    Tweets_text.close


# return tweets sent by author(me),use api.home_timeline() from tweepy!
def GET_My_Home_tweets(api):
    My_Home_tweets = api.home_timeline()
    # store result in a jason file called 'my_tweets'
    Write_tweets_to_File(My_Home_tweets, 'my_tweets')
    return My_Home_tweets

#return all supported languages of tweet
def GET_Help_languages(api):
    support_languages=api.supported_languages()
    return support_languages

#set sleeptime for users
def Sleep_time_define(api,start_time, end_time):
    Sleep_time=api.set_settings(sleep_time_enabled=True,start_sleep_time=start_time,end_sleep_time=end_time)
    return Sleep_time

# get several numbers of tweets from a certain user, use api.user_timeline() from tweepy!
def GET_User_Timeline(api, User_ID, Count_Number):
    user_tweets_list = api.user_timeline(id=User_ID, count=Count_Number)#user_id is user name
    # store result into a jason file
    Write_tweets_to_File(user_tweets_list, 'user_tweets')
    return user_tweets_list
def GET_Followers(api,User_ID,Count_Number):
    user_followers=api.get_follower_ids(user_id=User_ID,count=Count_Number)
    return user_followers


# search tweets according to content, use api.search_tweets from tweepy
def GET_Search_Tweets(api, Target_content, search_type, Count_Number, Time):
    Result_Tweets = api.search_tweets(q=Target_content, result_type=search_type, count=Count_Number, until=Time)
    Display_tweets(Result_Tweets)
    Write_tweets_to_File(Result_Tweets, 'Search_tweets')
    return Result_Tweets


if __name__ == "__main__":
    API = Authorization_Setup()
    #Home_Tweets = GET_My_Home_tweets(API)
    #User_Tweets = GET_User_Timeline(API,'@JoeBiden',10)
    #print(User_Tweets)
    #Use Boston University ECE department twitter as example.
    #Result_Tweets = GET_Search_Tweets(API, "Joe Biden", "recent", 1, "2021-09-20")
    #print(Result_Tweets)
    #sleeptime=Sleep_time_define(API,10, 11)
    #print(sleeptime)
    #print(GET_Help_languages(API))
    print(GET_Followers(API,'JoeBiden',1))
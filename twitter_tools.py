#It groups a few useful twitter-scrapping functions

import json

#it return FALSE if screen name not correct OR twitter rate limit is exceeded
def correct_screen_name(screenname, twitter_auth):
    name= screenname
    url=f'https://api.twitter.com/1.1/users/lookup.json?&screen_name={name}'
    query = twitter_auth.get(url)
    Person = json.loads(query.content)
    if not'errors' in Person: 
        return True
    else: return False
    

def t_followers(screenname,twitter_auth):
    name= screenname
    url=f'https://api.twitter.com/1.1/users/lookup.json?&screen_name={name}'
    query = twitter_auth.get(url)
    Person = json.loads(query.content)
    if not'errors' in Person: 
        result=Person[0]['followers_count']
        result= (f'{result:,}')
        return result
   
 
def t_description(screenname,twitter_auth):
    name= screenname
    url=f'https://api.twitter.com/1.1/users/lookup.json?&screen_name={name}'
    query = twitter_auth.get(url)
    Person = json.loads(query.content)
    result=Person[0]['description']
    return result


def t_name(screenname,twitter_auth):
    name= screenname
    url=f'https://api.twitter.com/1.1/users/lookup.json?&screen_name={name}'
    query = twitter_auth.get(url)
    Person = json.loads(query.content)
    result=Person[0]['name']
    return result


def t_id(screenname,twitter_auth):
    name= screenname
    url=f'https://api.twitter.com/1.1/users/lookup.json?&screen_name={name}'
    query = twitter_auth.get(url)
    Person = json.loads(query.content)
    result=Person[0]['id']
    return result


def t_location(screenname,twitter_auth):
    name= screenname
    url=f'https://api.twitter.com/1.1/users/lookup.json?&screen_name={name}'
    query = twitter_auth.get(url)
    Person = json.loads(query.content)
    result=Person[0]['location']
    return result



#recommended to unpacked as following:  name, id_, description, location, followers=t_account_data()
def t_account_data(screenname,twitter_auth):
    name=t_name(screenname,twitter_auth)
    id_= str(t_id(screenname,twitter_auth))
    description=t_description(screenname,twitter_auth)
    location= t_location(screenname,twitter_auth)
    followers= str(t_followers(screenname,twitter_auth))
    result =(name, id_, description, location, followers)
    return result
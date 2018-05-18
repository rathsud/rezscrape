'''  Copyright Sudhanshu Rath, 2018
     All rights reserved.

     This software scrapes publically shared
     resume links from Reddit and consolidates
     them in an easy to find place.
'''
from __future__ import print_function
try:
    import praw
    import re
except ImportError as ie:
    print('ErrorImportingModules')
try:
    from ResConfig import usr, pwd, sec, clid, \
        postUrl, debugFlag as DEBUG
except ImportError as configError:
    print('UnableToImportConfig')

def connectToReddit():
    global CONN
    CONN = praw.Reddit(user_agent='RezScrape', \
                           client_id=clid, client_secret=sec, \
                           username=usr, password=pwd)

def getTopComments(url):
    top = []
    submission = CONN.submission(url=url)
    submission.comments.replace_more(limit=None)
    for top_level_comment in submission.comments:
        if DEBUG:
            print('-' * 50,) 
            print(top_level_comment.body)
            print('-' * 50,)
        top.append(top_level_comment.body)
    return top

def filter(aList):
    filtered = []
    for _ in aList:
        filtered.append(re.findall(SCRAPE_REGEX, _))
    return filtered


def post(link):
    return

SCRAPE_REGEX = "http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\), ]" \
               + "|(?:%[0-9a-fA-F][0-9a-fA-F]))+"

if __name__=='__main__':
    if DEBUG:
        print('user: ' + usr)
        print('pwd: ' + pwd)
        print('sec: ' + sec)
        print('app: ' + clid)

    link = 'https://www.reddit.com/r/cscareerquestions/comments/8eijwl/resume_advice_thread_april_24_2018/?st=jhbh4jk2&sh=18f6ba08'
    connectToReddit()
    resumes = filter(getTopComments(link))
    print(resumes)

'''    unableToPost = []
    for _ in resumes:
        if post(_) and DEBUG:
            print('Success! Posted: ' + _)
        elif DEBUG:
            print('Failed! Couldn\'t post: ' + _)
            unableToPost.append(_)
        else:
            unableToPost.append(_)'''
        

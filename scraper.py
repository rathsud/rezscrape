'''  Copyright Sudhanshu Rath, 2018
     All rights reserved.

     This software scrapes publically shared
     resume links from Reddit and consolidates
     them in an easy to find place.
'''
from __future__ import print_function
try:
    import praw
except ImportError as ie:
    print('ErrorImportingModules')
try:
    from ResConfig import user, pwd, sec, app
except ImportError as configError:
    print('UnableToImportConfig')

DEBUG = True

if __name__=='__main__':
    if DEBUG:
        print('user: ' + user)
        print('pwd: ' + pwd)
        print('sec: ' + sec)
        print('app: ' + app)
    
    # Setup connection to Reddit with Praw
    connectToReddit()
    # Obtain list of top comments in page


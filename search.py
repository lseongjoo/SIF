#!/usr/bin/env python

import urllib
import urllib2
import simplejson
import sys

class Entry(object):
    def __init__(self, name):
        self.name = name
        self.urls=[]
        self.desc=[]
        

def searchweb(phrase, engine='google'):
    """
    Get google search results for the phrase
    """
    
    # loop through each term in the phrase and
    #   return the highest ranking result    
    # Define the query to pass to Google Search API
    query = urllib.urlencode({'q': phrase})
    if engine == 'google':
        url = "http://ajax.googleapis.com/ajax/services/search/web?v=1.0&%s" % (query)
    
    # Fetch the results and create JSON structure
    search_results = urllib2.urlopen(url)
    json = simplejson.loads(search_results.read())
    
    # Process the results by pulling the first record, which has the best match
    results = json['responseData']['results']
    
    target = Entry(phrase)
    for r in results[:5]:
        target.urls.append(r['url'])
        # TODO: remove html tags from the description before store it
        desc = r['content'].encode('utf-8','replace')
        target.desc.append(desc)
        #url=r['url']
        #desc=r['content'].encode('utf-8', 'replace')
        
    # print the result to stdout. Use redirect to capture the output    
    #print "%s\t%s\t%s" % (phrase, url, desc)
    for desc in target.desc:
        print desc



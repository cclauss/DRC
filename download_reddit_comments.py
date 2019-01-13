#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# TODO: use utf-8 instead of ascii;
# DownloadRedditComments by GoDzM4TT3O & cclauss
# I worked really hard on this, unicode errors and that stuff.
# The program would throw an error because of unicode characters.
# In my case I had \u2019 in my comments, now problem is fixed.
# THANK GOD.

from __future__ import print_function, absolute_import
import re, requests, time, unicodedata

print("\n     DRC by GoDzM4TT3O . Contribute:")
print("    https://github.com/GoDzM4TT3O/DRC")

freq = None
while freq not in ('DAY', 'WEEK', 'MONTH', 'YEAR'):
	freq = input("\nPlease enter a comment frequency: [DAY/WEEK/MONTH/YEAR]\n> ").strip().upper()
	
isnum = 0
while not isnum:
        limit = input("\nHow many comments would you like to download? [>=10]\n> ")
        nums = re.compile("^[\-]?[1-9][0-9]*\.?[0-9]+$")
        isnum = re.match(nums, limit)
	
rawu = input("\nPlease enter a valid Reddit username of your choice\n"
             "to download their " + limit + " comments with this frequency: " + freq +
             "\n> /u/")
user = rawu.replace(" ", "")

# fun fact!
# if below line is commented,
# the program will fetch random usernames!

if not user:
	user = input("\nPlease enter a valid username:  ")
	
subreddit = input("\n[OPTIONAL] Enter subreddit you'd like to download comments from."
                  "\nIf no subreddit is defined, you'll download\n        "
                  + limit + " comments\nmade by\n        /u/"
                  + user + "\nwith this frequency:\n           "
                  + freq + "\nin every subreddit they have commented."
                  "\nAlternatively, you'll download /u/"
                  + user + " comments in the provided subreddit\nif the username and subreddit are valid.\n"
                  "> /r/")

apiurl = "https://api.pushshift.io/reddit/comment/search?author=" + user + "&frequency=" + freq + "&limit=" + limit
if subreddit:
	apiurl += "&subreddit=" + subreddit
	
data = requests.get(apiurl).json()
if not data.get('data'):
	print("\n\nERROR: Cannot collect any data! Please make sure the specified values like\n"
              "        /u/" + user + "\nand [OPTIONAL]\n        /r/" + subreddit + "\nare valid.\n"
              "If they are - we just have not obtained any comments; are there any?\n")
else:
        print("\n\nDownloading...\n"
              "NOTE: If you'll get \"KeyError: 'permalink'\",\n"
              "      most likely " + limit + " comments number is too high\n"
              "      - more than this user has ever posted! Try lowering it, or just use\n"
              "https://atomiks.github.io/reddit-user-analyser/\n"
              "      to find out how many comments this user has\n"
              "      and specify this number to get them all;\n"
              "      although in my case I can't get > 346/367\n")
	
## Made  by  GoDzM4TT3O & cclauss
outname = user + '.DRC.txt'
for element in data['data']:

	author = element['author']
	contentold = element[u'body']
	content = unicodedata.normalize('NFKD',
	contentold).encode('ascii', 'ignore').decode()
	permalink = element['permalink']
	upvotes = element['score']
	issticky = element['stickied']
	sub = element['subreddit']
	unix_date = element['retrieved_on']
	date = time.strftime('%d-%m-%Y %H:%M:%S', time.localtime(unix_date))
	
	print("\nAuthor:\n",
	author, "\n\nComment content:\n",
	content, "\n\nPermalink:\n",
	permalink, "\n\nUpvotes:\n",
	upvotes, "\n\nIs sticky post:\n",
	issticky, "\nSubreddit:\n",
	sub, "\n\nPosted on:\nUnix date:\n",
	unix_date, "\nDate (DD/MM/YYYY):\n",
	date, "\n\n--------------------\n\n",
	file=open(outname, "a"))
# Made by GoDzM4TT3O & cclauss

print("\n      COMPLETED! This is wonderful")
print("     DRC by GoDzM4TT3O . Contribute:")
print("    https://github.com/GoDzM4TT3O/DRC\n")

#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# DownloadRedditComments by GoDzM4TT3O
# I worked really hard on this, unicode errors and that stuff. The program would throw an error because of unicode characters. in my case I had \u2019 in my comments, now problem is fixed. THANK GOD.
# You can try it yourself - if you comment out 'content' and rename 'contentold' to 'content', and put my username (when you run the script), you will get an error with \u2019

import console, json, urllib.request, time, re, unicodedata

freq = console.input_alert("DRC by GoDzM4TT3O", "Please enter a comment frequency. Choose one of these:\n\nday\nweek\nmonth\nyear")

if freq == 'day':
	freq = 'day'
elif freq == 'week':
	freq = 'week'
elif freq == 'month':
	freq = 'month'
elif freq == 'year':
	freq = 'year'
else:
	console.alert("DRC by GoDzM4TT3O", "Choose a valid comment frequency.\nList of valid post frequencies:\n\nday\n\nweek\n\nmonth\n\nyear")
	
limit = console.input_alert("DRC by GoDzM4TT3O", "How many comments would you like to download? [Example: 50]\nMUST BE 10 or more.")

nums = re.compile("^[\-]?[1-9][0-9]*\.?[0-9]+$")
isnum = re.match(nums, limit)
if isnum:
	limit == limit
else:
	console.alert("DRC by GoDzM4TT3O", "Please enter a numeric comment limit. For example, if I want to download my last 10 comments this week, I will choose 'week' as comment frequency, and 10 as comment limit.")

if not limit:
	console.alert("DRC by GoDzM4TT3O", "Please enter a numeric comment limit. For example, if I want to download my last 10 comments this week, I will choose 'week' as comment frequency, and 10 as comment limit.")

rawu = console.input_alert("DRC by GoDzM4TT3O", "Please enter a valid Reddit username of your choice to download their " + limit + " comments with the frequency: " + freq)
user = rawu
if ' ' in user:
	user = user.replace(" ", "")

# fun fact! if below line is commented, the program will fetch random usernames!

if not user:
	console.alert("DRC by GoDzM4TT3O", "Please enter a valid username.")

subreddit = console.input_alert("DRC by GoDzM4TT3O", "[OPTIONAL] Enter a subreddit you'd like to download comments from.\nIf no subreddit is defined, you'll only download " + limit + " comments made by " + user + " with this frequency: " + freq + " in every subreddit they commented.\nIn alternative, if a subreddit is provided, you'll download " + user + "'s comments in the provided subreddit, if the user and the subreddit are valid.")

if not subreddit:
	apiurl = "https://api.pushshift.io/reddit/comment/search?author=" + user + "&frequency=" + freq + "&limit=" + limit
else:
	apiurl = "https://api.pushshift.io/reddit/comment/search?author=" + user + "&frequency=" + freq + "&limit=" + limit + "&subreddit=" + subreddit

with urllib.request.urlopen(apiurl) as url:
	data = json.loads(url.read().decode())
	if not data['data']:
		print(("\nDRC by GoDzM4TT3O\n\nERROR: The specified user", user, "doesn't exist."))
		
## Made  by  GoDzM4TT3O
outname = user + '-log.DRC.txt'
for element in data['data']:

	author = element['author']
	contentold = element[u'body']
	content = unicodedata.normalize('NFKD', contentold).encode('ascii','ignore')
	permalink = element['permalink']
	upvotes = element['score']
	issticky = element['stickied']
	sub = element['subreddit']
	unix_date = element['retrieved_on']
	date = time.strftime('%d-%m-%Y %H:%M:%S', time.localtime(unix_date))

	print("\nAuthor:\n", author, "\n\nComment content:\n", content, "\n\nPermalink:\n", permalink, "\n\nUpvotes:\n", upvotes, "\n\nIs sticky post:\n", issticky, "\nSubreddit:\n", sub, "\n\nPosted on:\nUnix date:\n", unix_date, "\nDate (DD/MM/YYYY):\n", date, "\n\n--------------------\n\n", file=open(outname, "a"))

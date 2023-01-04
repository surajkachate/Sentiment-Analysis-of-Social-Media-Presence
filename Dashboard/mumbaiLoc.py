import time
import multiprocessing
from datetime import datetime
import json
from re import T
from tkinter import Scrollbar
import pandas as pd
import snscrape.modules.twitter as sntwitter
import itertools
import time
import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="scraper"
)

mycursor = mydb.cursor()
#search = ["nagpur",'Amravati','Jalgaon','Mukbai','Pune','Banglore','Bhopal','Nashik','Akola','Bandra']
counter = 0


def func1(loc):
    scrapped_tweets = sntwitter.TwitterSearchScraper(
        '  geocode:"{}"'.format(loc))
# # process
    while True:
        for i, t in enumerate(scrapped_tweets.get_items()):
            mul = ''

            if (t.mentionedUsers == None):
                # for mu in t.mentionedUsers :

                mentioneduserlist = []
            else:
                mentioneduserlist = []
                for mu in t.mentionedUsers:
                    mentioneduserlist.append(mu.id)

                mul = json.dumps(mentioneduserlist)
                # print(mul)

            # search for user in db
            uid = t.user.id
            query = ("SELECT * FROM users where user_id = '%s'")
            mycursor.execute(query, (uid,))
            #print("Found",mycursor.rowcount,"row(s) of data.")
            myresult = mycursor.fetchall()
            #print (mycursor.rowcount)
            # do entry if not found
            if (mycursor.rowcount == 0):
                created = datetime.timestamp(t.user.created)
                outlink = json.dumps(t.outlinks)
                tcooutlinks = json.dumps(t.tcooutlinks)
                descriptionUrls = repr(t.user.descriptionUrls)
                media = repr(t.media)
                sql = "INSERT INTO users (user_id, username, displayname, description, descriptionUrls, verified, created, followersCount, friendsCount, statusesCount, favouritesCount, listedCount, mediaCount, location, protected, linkUrl, profileImageUrl, profileBannerUrl) VALUES (%s, %s, %s, %s,%s, %s, %s, %s, %s,%s, %s, %s, %s, %s,%s, %s, %s, %s)"
                val = (t.user.id, t.user.username, t.user.displayname, t.user.description, descriptionUrls, t.user.verified, created, t.user.followersCount, t.user.friendsCount, t.user.statusesCount,
                       t.user.favouritesCount, t.user.listedCount, t.user.mediaCount, t.user.location, t.user.protected, t.user.linkUrl, t.user.profileImageUrl, t.user.profileBannerUrl)
                mycursor.execute(sql, val)
                mydb.commit()
                print(mycursor.rowcount, "User inserted_Process1.")
            else:
                continue
            # search db for the same tweet
            ################################################################################
            # find dummy entry to db for tweet
            id = t.id
            query = ("SELECT * FROM tweets where tweet_id = '%s'")
            mycursor.execute(query, (id,))
            #print("Found",mycursor.rowcount,"row(s) of data.")
            myresult = mycursor.fetchall()
            #print (mycursor.rowcount)
            ##############################################################################
            # do entry if not found
            if (mycursor.rowcount == 0):
                date = datetime.timestamp(t.date)
                outlink = json.dumps(t.outlinks)
                tcooutlinks = json.dumps(t.tcooutlinks)
                quotedTweet = repr(t.quotedTweet)
                media = repr(t.media)
                sql = "INSERT INTO tweets (tweet_id, url, date, content, renderedContent, user_id, outlinks, tcooutlinks, replyCount, retweetCount, likeCount, quoteCount, conversationId, lang, source, media, retweetedTweet, quotedTweet, mentionedUsers) VALUES (%s, %s, %s, %s, %s,%s, %s, %s, %s, %s,%s, %s, %s, %s, %s,%s, %s, %s, %s)"
                val = (t.id, t.url, date, t.content, t.renderedContent, t.user.id, outlink, tcooutlinks, t.replyCount, t.retweetCount,
                       t.likeCount, t.quoteCount, t.conversationId, t.lang, t.source, media, t.retweetedTweet, quotedTweet, mul)
                mycursor.execute(sql, val)
                mydb.commit()
                print(mycursor.rowcount, "Tweet inserted_Process2.")


def func2(loc):
    scrapped_tweets = sntwitter.TwitterSearchScraper(
        '  geocode:"{}"'.format(loc))
# # process
    while True:
        for i, t in enumerate(scrapped_tweets.get_items()):
            mul = ''

            if (t.mentionedUsers == None):
                # for mu in t.mentionedUsers :

                mentioneduserlist = []
            else:
                mentioneduserlist = []
                for mu in t.mentionedUsers:
                    mentioneduserlist.append(mu.id)

                mul = json.dumps(mentioneduserlist)
                # print(mul)

            # search for user in db
            uid = t.user.id
            query = ("SELECT * FROM users where user_id = '%s'")
            mycursor.execute(query, (uid,))
            #print("Found",mycursor.rowcount,"row(s) of data.")
            myresult = mycursor.fetchall()
            #print (mycursor.rowcount)
            # do entry if not found
            if (mycursor.rowcount == 0):
                created = datetime.timestamp(t.user.created)
                outlink = json.dumps(t.outlinks)
                tcooutlinks = json.dumps(t.tcooutlinks)
                descriptionUrls = repr(t.user.descriptionUrls)
                media = repr(t.media)
                sql = "INSERT INTO users (user_id, username, displayname, description, descriptionUrls, verified, created, followersCount, friendsCount, statusesCount, favouritesCount, listedCount, mediaCount, location, protected, linkUrl, profileImageUrl, profileBannerUrl) VALUES (%s, %s, %s, %s,%s, %s, %s, %s, %s,%s, %s, %s, %s, %s,%s, %s, %s, %s)"
                val = (t.user.id, t.user.username, t.user.displayname, t.user.description, descriptionUrls, t.user.verified, created, t.user.followersCount, t.user.friendsCount, t.user.statusesCount,
                       t.user.favouritesCount, t.user.listedCount, t.user.mediaCount, t.user.location, t.user.protected, t.user.linkUrl, t.user.profileImageUrl, t.user.profileBannerUrl)
                mycursor.execute(sql, val)
                mydb.commit()
                print(mycursor.rowcount, "User inserted_Process2.")
            else:
                continue
            # search db for the same tweet
            ################################################################################
            # find dummy entry to db for tweet
            id = t.id
            query = ("SELECT * FROM tweets where tweet_id = '%s'")
            mycursor.execute(query, (id,))
            #print("Found",mycursor.rowcount,"row(s) of data.")
            myresult = mycursor.fetchall()
            #print (mycursor.rowcount)
            ##############################################################################
            # do entry if not found
            if (mycursor.rowcount == 0):
                date = datetime.timestamp(t.date)
                outlink = json.dumps(t.outlinks)
                tcooutlinks = json.dumps(t.tcooutlinks)
                quotedTweet = repr(t.quotedTweet)
                media = repr(t.media)
                sql = "INSERT INTO tweets (tweet_id, url, date, content, renderedContent, user_id, outlinks, tcooutlinks, replyCount, retweetCount, likeCount, quoteCount, conversationId, lang, source, media, retweetedTweet, quotedTweet, mentionedUsers) VALUES (%s, %s, %s, %s, %s,%s, %s, %s, %s, %s,%s, %s, %s, %s, %s,%s, %s, %s, %s)"
                val = (t.id, t.url, date, t.content, t.renderedContent, t.user.id, outlink, tcooutlinks, t.replyCount, t.retweetCount,
                       t.likeCount, t.quoteCount, t.conversationId, t.lang, t.source, media, t.retweetedTweet, quotedTweet, mul)
                mycursor.execute(sql, val)
                mydb.commit()
                print(mycursor.rowcount, "Tweet inserted_Process2.")


def func3(loc):
    scrapped_tweets = sntwitter.TwitterSearchScraper(
        '  geocode:"{}"'.format(loc))
# # process
    while True:
        for i, t in enumerate(scrapped_tweets.get_items()):
            mul = ''

            if (t.mentionedUsers == None):
                # for mu in t.mentionedUsers :

                mentioneduserlist = []
            else:
                mentioneduserlist = []
                for mu in t.mentionedUsers:
                    mentioneduserlist.append(mu.id)

                mul = json.dumps(mentioneduserlist)
                # print(mul)

            # search for user in db
            uid = t.user.id
            query = ("SELECT * FROM users where user_id = '%s'")
            mycursor.execute(query, (uid,))
            #print("Found",mycursor.rowcount,"row(s) of data.")
            myresult = mycursor.fetchall()
            #print (mycursor.rowcount)
            # do entry if not found
            if (mycursor.rowcount == 0):
                created = datetime.timestamp(t.user.created)
                outlink = json.dumps(t.outlinks)
                tcooutlinks = json.dumps(t.tcooutlinks)
                descriptionUrls = repr(t.user.descriptionUrls)
                media = repr(t.media)
                sql = "INSERT INTO users (user_id, username, displayname, description, descriptionUrls, verified, created, followersCount, friendsCount, statusesCount, favouritesCount, listedCount, mediaCount, location, protected, linkUrl, profileImageUrl, profileBannerUrl) VALUES (%s, %s, %s, %s,%s, %s, %s, %s, %s,%s, %s, %s, %s, %s,%s, %s, %s, %s)"
                val = (t.user.id, t.user.username, t.user.displayname, t.user.description, descriptionUrls, t.user.verified, created, t.user.followersCount, t.user.friendsCount, t.user.statusesCount,
                       t.user.favouritesCount, t.user.listedCount, t.user.mediaCount, t.user.location, t.user.protected, t.user.linkUrl, t.user.profileImageUrl, t.user.profileBannerUrl)
                mycursor.execute(sql, val)
                mydb.commit()
                print(mycursor.rowcount, "User inserted_Process3.")
            else:
                continue
            # search db for the same tweet
            ################################################################################
            # find dummy entry to db for tweet
            id = t.id
            query = ("SELECT * FROM tweets where tweet_id = '%s'")
            mycursor.execute(query, (id,))
            #print("Found",mycursor.rowcount,"row(s) of data.")
            myresult = mycursor.fetchall()
            #print (mycursor.rowcount)
            ##############################################################################
            # do entry if not found
            if (mycursor.rowcount == 0):
                date = datetime.timestamp(t.date)
                outlink = json.dumps(t.outlinks)
                tcooutlinks = json.dumps(t.tcooutlinks)
                quotedTweet = repr(t.quotedTweet)
                media = repr(t.media)
                sql = "INSERT INTO tweets (tweet_id, url, date, content, renderedContent, user_id, outlinks, tcooutlinks, replyCount, retweetCount, likeCount, quoteCount, conversationId, lang, source, media, retweetedTweet, quotedTweet, mentionedUsers) VALUES (%s, %s, %s, %s, %s,%s, %s, %s, %s, %s,%s, %s, %s, %s, %s,%s, %s, %s, %s)"
                val = (t.id, t.url, date, t.content, t.renderedContent, t.user.id, outlink, tcooutlinks, t.replyCount, t.retweetCount,
                       t.likeCount, t.quoteCount, t.conversationId, t.lang, t.source, media, t.retweetedTweet, quotedTweet, mul)
                mycursor.execute(sql, val)
                mydb.commit()
                print(mycursor.rowcount, "Tweet inserted_Process3.")
                

# MultiProcessing-----------------------

if __name__ == '__main__':
    starttime = time.time()
    processes = []
    loc = ['19.103293, 72.852277, 10km', '19.116781, 72.837857, 1km']
    for i in loc:
        print(i)
        p1 = multiprocessing.Process(target=func1, args=(i,))
        processes.append(p1)
        p2 = multiprocessing.Process(target=func2, args=(i,))
        processes.append(p2)
        p3 = multiprocessing.Process(target=func3, args=(i,))
        processes.append(p3)
        p1.start()
        print("Process_1 Started")
        p2.start()
        print("Process_2 Started")
        p3.start()
        print("Process_3 Started")
        p1.join()
        p2.join()
        p3.join()

    for process in processes:
        print('joinging all')
        process.join()

    print('That took {} seconds'.format(time.time() - starttime))

# Parallel loop--------------------
    #  for i,j,k in zip(['19.117884, 72.908641, 1km'],['19.11167336461392, 72.91548015094064, 1km'],['19.112316, 72.891863, 1km']):
    #     print(i,j,k)
    #     p1 = multiprocessing.Process(target=func1, args=(i,))
    #     processes.append(p1)
    #     p2 = multiprocessing.Process(target=func2, args=(j,))
    #     processes.append(p2)
    #     p3 = multiprocessing.Process(target=func3, args=(k,))
    #     processes.append(p3)
    #     p1.start()
    #     p2.start()
    #     p3.start()

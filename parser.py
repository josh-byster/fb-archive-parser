#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Oct  2 02:13:32 2017

@author: joshbyster
"""
from dateutil.parser import parse
from bs4 import BeautifulSoup
from operator import attrgetter
import pickle
from datetime import datetime
from message import Message
#do something


def load_messages_from_file():
    startTime = datetime.now()
    elements_parsed=0
    with open("messages.htm",encoding="utf-8") as f:
        filesoup = BeautifulSoup(f,"lxml")#make soup that is parse-able by bs
        
        threads = filesoup.find_all("div","thread")
        msgarray=[[] for x in range(len(threads))]              
        for t in range(len(threads)):
            threadnames = str(threads[t]).split("<div")[1][16:]
            msgarray[t].append(threadnames)
            soup=BeautifulSoup(str(threads[t]),"lxml")
            a=soup.find_all("div","message")
      
            k=soup.find_all("p")
            
            for i in range(min(len(a),len(k))):
                msgcontents=k[i].string
                msgdata=a[i]
                username=msgdata.contents[0].contents[0].string            
                date=parse(msgdata.contents[0].contents[1].string)
                if(msgcontents is not None and username is not None and date is not None):
                    msg = Message(str(username),date,str(msgcontents))
                    msgarray[t].append(msg)
                    elements_parsed=elements_parsed+1
                    if(elements_parsed%1000==0):
                        print("Parsed:",elements_parsed)
        with open('archive.pkl', 'wb') as f:
             pickle.dump(msgarray, f)
        
    print("Messages parsed: ", elements_parsed)


def split_individual(archive_name):
    msg = pickle.load( open(archive_name, "rb" ) )
    authors=[]
    dates=[]
    contents=[]
    msglist=[]
    for thread in msg:
        for message in thread:
            if(isinstance(message,str)==False):
               authors.append(message.name)
               dates.append(message.date)
               contents.append(message.contents)
               msglist.append(message)
    bigstring=""
    for k in contents:
        bigstring+=k+" "
    
    return authors,dates,contents,msg,msglist,bigstring
    
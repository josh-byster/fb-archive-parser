#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Oct  6 17:22:44 2017

@author: joshbyster
"""
from parser import load_messages_from_file,split_individual
from wcloud import make_cloud
from operator import attrgetter
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
from collections import Counter
import numpy as np
from datetime import datetime
from message import Message
import pickle
startTime=datetime.now()
if('authors' not in locals()):
    option = input("Would you like to load from pickle archive or load from file [a/f]? ")
    
    startTime=datetime.now()
    if(option== "a"):
        authors,dates,contents,rawmsg_by_thread,msglist,bigstring=split_individual("archive.pkl")
    else:
        load_messages_from_file()
        authors,dates,contents,rawmsg_by_thread,msglist,bigstring=split_individual("archive.pkl")
    
def get_date_distribution():
    global hour
    hour = [dates[i].hour for i in range(len(dates))]
    labels, values = zip(*sorted(Counter(hour).items()))
    indexes = np.arange(len(labels))
    width = 1
    plt.title("Hours vs. # of Messages Sent / Received")
    plt.bar(indexes, values, width)
    plt.xticks(indexes + width * 0.5, labels)
    plt.show()


def letters():
    alphabet_counter=Counter(list(bigstring.lower())).most_common(50)
    print("Counter for letters ",alphabet_counter)
    labels, values = zip(*alphabet_counter)
    values = [value / sum(values) * 100 for value in values]
    values = values[1:]
    labels = labels[1:]
    indexes = np.arange(len(labels))
    print(labels)
    width = 1
    plt.title("Letters vs. % Frequency")
    plt.bar(indexes, values, width)
    plt.xticks(indexes + width*.5, labels)
    plt.show()

def get_messages_by_name(name,r):
    n=0
    for i in range(len(authors)):
        if(authors[i] == name and n<r):
            n=n+1
            print(dates[i],":",contents[i])     
        if(n>r):
            break
        

def sort_chron():
    try:
        global indices
        indices=pickle.load( open("sorted_indices.pkl", "rb" ) )
    except:
        print("Currently sorting...")
        indices=np.argsort(dates)
    print("Sorted")
    global contents_sorted,dates_sorted,authors_sorted
    contents_sorted=[contents[i] for i in indices]
    dates_sorted=[dates[i] for i in indices]
    authors_sorted=[authors[i] for i in indices]
    
    
def plot_cumulative():
    plt.gca().xaxis.set_major_formatter(mdates.DateFormatter('%Y'))
    plt.gca().xaxis.set_major_locator(mdates.YearLocator())
    y_vals = [i / 193977 for i in range(193977)]
    plt.plot(dates_sorted[0::25],y_vals[0::25],'.')
get_date_distribution() 
letters()
#make_cloud()
sort_chron()
plot_cumulative()
endTime=datetime.now()
print("\n\nTotal Program Runtime:",str((endTime - startTime).seconds)+ "s")
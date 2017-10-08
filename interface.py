#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Oct  6 17:22:44 2017

@author: joshbyster
"""
from parser import load_messages_from_file,split_individual
from wcloud import make_cloud
import matplotlib.pyplot as plt
from collections import Counter
import numpy as np
from datetime import datetime

startTime=datetime.now()
if('authors' not in locals()):
    option = input("Would you like to load from pickle archive or load from file [a/f]? ")
    
    startTime=datetime.now()
    if(option== "a"):
        authors,dates,contents,bigstring=split_individual("archive.pkl")
    else:
        load_messages_from_file()
        authors,dates,contents,bigstring=split_individual("archive.pkl")
    
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

        
get_date_distribution() 
letters()
make_cloud()
endTime=datetime.now()
print("\n\nTotal Program Runtime:",str((endTime - startTime).seconds)+ "s")
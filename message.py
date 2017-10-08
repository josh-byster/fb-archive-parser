#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Oct  6 17:33:45 2017

@author: joshbyster
"""

class Message:
    def __init__(self, name, date, contents):
        self.contents = contents
        self.name=name
        self.date=date
         
    def toString(self):
        print("Name:",username)
        print("Date:",date.strftime('%m/%d/%Y %H:%M'))
        print("Message:",msgcontents)

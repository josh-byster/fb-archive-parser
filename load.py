import pickle


def split_individual(archive_name):
    msg = pickle.load( open(archive_name, "rb" ) )
    authors=[]
    dates=[]
    contents=[]
    for thread in msg:
        for message in thread:
            if(isinstance(message,str)==False):
               authors.append(message.name)
               dates.append(message.date)
               contents.append(message.contents)
    bigstring=""
    for k in contents:
        bigstring+=k+" "
    
    return authors,dates,contents,bigstring
    
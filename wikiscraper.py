#This program will get names from file and read it into a list.

#It will then start a for loop that goes through that list in groups of 20.
#This keeps everyone's birthdays the same

#It will add their names to the end of the web address:
# https://en.wikipedia.org/wiki/

# It will go to that site and check that the birthday matches up
# with the current batch by checking if it's inside of text in a child of
# class infobox biography vcard

#Lastly it will pull out text elements in p elements.
# I may also have it collect movie names, but uncertain.

# One possible use is to just check the frequency words get used in both groups.# a list of the most frequently used words, and the words with the biggest differences could be interesting.

#First lets start with an easier one. Go to a site, collect all of the links and put them in a list, then go to each link and create a list of the most commonly used words, then do the same for the other site.
from bs4 import BeautifulSoup
import urllib2
import time
import re

# setting variables we want to go through everything
menWordFrequency ={}
womenWordFrequency ={}
manCount =0
manWordCount =0
womanCount=0
womanWordCount=0
failSiteList =[]
with open('actorNames.txt') as f:
    actor_list = [line.rstrip('\n') for line in f]
count =0
countDay=1
month =1
# this is our loop that loops through things. Right now it loops through all of the names
for name in actor_list:
    count+=1
    if count ==21:
        count =1
        countDay +=1
    if countDay >28:
        countDay = 1
        month +=1
    print name
    print count
    print month
    print countDay
    wikiUrl = 'https://en.wikipedia.org/wiki/'+name
#These should be done many times, but here we're accessing the website so we'll need to slow things down
    if month ==1:
        time.sleep(3)
        wordFrequency = {}
        try:
            wikiPage = urllib2.urlopen(wikiUrl)
            wikiHtml =wikiPage.read()
            wikiPage.close()
            wikiSoup = BeautifulSoup(wikiHtml,'lxml')
            actorPar = wikiSoup.find_all('p')
            for p in actorPar:
                wordList = p.get_text().split()
                for word in wordList:
                    #gets rid of the characters in the string from our word
                    word = re.sub('[0-9]','',word)
                    word = str(re.sub('\W+','',word).lower())
                    print word
                    if word in wordFrequency.keys():
                        wordFrequency[word]+=1
                    else:
                        wordFrequency[word]=1
            print wordFrequency
            try:
                print ("he: " +str(wordFrequency["he"]))
                heCount = wordFrequency["he"]
            except:
                heCount=0
                
            try:
                print "she: "+str(wordFrequency["she"])
                sheCount =wordFrequency["she"]
            except:
                sheCount=0
            # based on whether it talks about he, or she more often, add the dictionary to the men's dictionary, or the women's dictionary.
            if sheCount > heCount:
                womanCount+=1
                for word in wordFrequency.keys():
                    womanWordCount+=1
                    if word in womenWordFrequency.keys():
                        womenWordFrequency[word]+=wordFrequency[word]
                    else:
                        womenWordFrequency[word] = wordFrequency[word]
            else:
                manCount+=1
                for word in wordFrequency.keys():
                    manWordCount+=1
                    if word in menWordFrequency.keys():
                        menWordFrequency[word]+=wordFrequency[word]
                    else:
                        menWordFrequency[word] = wordFrequency[word]
            print "men: " + str(menWordFrequency)
            print "women: " + str(womenWordFrequency)
            print "man word count " + str(manWordCount)
            print "man count " + str(manCount)
            print "woman word count " +str(womanWordCount)
            print  "woman count "+str(womanCount)
        except:
            failSiteList.append(wikiUrl)

print failSiteList
print "man: " + str(menWordFrequency)
print "woman: " + str(womenWordFrequency)
print "Man Word Count: " + str(manWordCount)
print "Woman Word Count: " + str(womanWordCount)
print "men: " + str(manCount)
print "women: " + str(womanCount)
actorWordDoc = open("testactorWords.txt", "wb")
actressWordDoc = open("testactressWords.txt","wb")
actingDataDoc = open("testactingData.txt", "wb")
actorWordDoc.write(str(menWordFrequency))
actressWordDoc.write(str(womenWordFrequency))
actingDataDoc.write(str([manCount,womanCount,manWordCount,womanWordCount,manWordCount/manCount,womanWordCount/womanCount])+ "\nnumber of men " + str(manCount) + "\nnumber of women " + str(womanCount) + "\nnumber of words used for men " + str(manWordCount) + "\nnumber of words for women " + str(womanWordCount) + "\nwords per man "+ str(manWordCount/manCount) + "\n words per woman " + str(womanWordCount/womanCount))
#The next thing I want to do is make it so that it gets added to a general men's dictionary, or a general women's dictionary.
actorWordDoc.close()
actressWordDoc.close()
actingDataDoc.close()

from bs4 import BeautifulSoup
import urllib2
import time
import re
from actressWords import actressWordList
from actorWords import actorWordList
from actingData import genderData
# setting variables we want to go through everything
menWordFrequency = actorWordList
womenWordFrequency =actressWordList
manCount =genderData[0]
manWordCount =genderData[2]
womanCount=genderData[1]
womanWordCount=genderData[3]
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
    
    #print name
    #print count
    #print month
    #print countDay
    wikiUrl = 'https://en.wikipedia.org/wiki/'+name
#These should be done many times, but here we're accessing the website so we'll need to slow things down
    if month ==10:
        time.sleep(3)
        wordFrequency = {}
        if len(str(month))<2:
            strMonth = "0"+str(month)
        else:
            strMonth = str(month)
        if len(str(countDay))<2:
            strDay = "0"+str(countDay)
        else:
            strDay = str(countDay)
        date = strMonth+"-"+strDay
        months =["January","February","March","April","May","June","July", "August","September","October","November","December"]
        wordDate =months[month-1]+ " "+ str(countDay)
        #print date
        print wordDate
        try:
            wikiPage = urllib2.urlopen(wikiUrl)
            wikiHtml =wikiPage.read()
            wikiPage.close()
            wikiSoup = BeautifulSoup(wikiHtml,'lxml')
            actorBDayText = wikiSoup.find(class_="infobox").get_text()
            if (date) not in actorBDayText:
                if(wordDate) not in actorBDayText:
                    failSiteList.append("noBD"+ wikiUrl)
                   # print actorBDayText
                    continue
           # print "Bday text " +  actorBDayText
            actorPar = wikiSoup.find_all('p')
            for p in actorPar:
                wordList = p.get_text().split()
                for word in wordList:
                    #gets rid of the characters in the string from our word
                    word = re.sub('[0-9]','',word)
                    word = str(re.sub('\W+','',word).lower())
                    #print word
                    if word in wordFrequency.keys():
                        wordFrequency[word]+=1
                    else:
                        wordFrequency[word]=1
            #print wordFrequency
            try:
                #print ("he: " +str(wordFrequency["he"]))
                heCount = wordFrequency["he"]
            except:
                heCount=0
                
            try:
                #print "she: "+str(wordFrequency["she"])
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
            #print "men: " + str(menWordFrequency)
            #print "women: " + str(womenWordFrequency)
           # print "man word count " + str(manWordCount)
           # print "man count " + str(manCount)
           # print "woman word count " +str(womanWordCount)
           # print  "woman count "+str(womanCount)
        except:
            failSiteList.append(wikiUrl)

print failSiteList
#print "man: " + str(menWordFrequency)
#print "woman: " + str(womenWordFrequency)
print "Man Word Count: " + str(manWordCount)
print "Woman Word Count: " + str(womanWordCount)
print "men: " + str(manCount)
print "women: " + str(womanCount)
actorWordDoc = open("testActorWords.txt", "wb")
actressWordDoc = open("testActressWords.txt","wb")
actingDataDoc = open("testActingData.txt", "wb")
actorWordDoc.write("actorWordList = " + str(menWordFrequency))
actressWordDoc.write("actressWordList = " + str(womenWordFrequency))
actingDataDoc.write("genderData = "+str([manCount,womanCount,manWordCount,womanWordCount,manWordCount/manCount,womanWordCount/womanCount])+ "\n#number of men " + str(manCount) + "\n#number of women " + str(womanCount) + "\n#number of words used for men " + str(manWordCount) + "\n#number of words for women " + str(womanWordCount) + "\n#words per man "+ str(manWordCount/manCount) + "\n #words per woman " + str(womanWordCount/womanCount))
#The next thing I want to do is make it so that it gets added to a general men's dictionary, or a general women's dictionary.
actorWordDoc.close()
actressWordDoc.close()
actingDataDoc.close()

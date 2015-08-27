from bs4 import BeautifulSoup
import urllib2
import time
urlList = []
for imonth in range(1,13):
    for iday in range(1,29):
        if imonth<10 and iday <10:
            urlList.append('http://www.imdb.com/search/name?birth_monthday=%s-%s&refine=birth_monthday&start=1' % ('0'+str(imonth),'0'+str(iday)))
        elif imonth >9 and iday>9:
            urlList.append('http://www.imdb.com/search/name?birth_monthday=%s-%s&refine=birth_monthday&start=1' % (imonth,iday))
        elif imonth>9:
            urlList.append('http://www.imdb.com/search/name?birth_monthday=0%s-0%s&refine=birth_monthday&start=1' % (imonth,'0'+str(iday)))
        else:
            urlList.append('http://www.imdb.com/search/name?birth_monthday=0%s-0%s&refine=birth_monthday&start=1' % ('0'+str(imonth),iday))
for link in urlList:    
    actorSite = urllib2.urlopen(link)
    actorHtml = actorSite.read()
    actorSite.close()
    soup = BeautifulSoup(actorHtml,'lxml')
    actorAll = soup.select('.name > a')
    actorNames = open('actorNames.txt','ab')
    actorList = []
    counter =0
    for actor in actorAll:
        counter+=1
        if counter>20:
            break
        name = actor.get_text().encode('utf8')
        actorList.append(name)
        try:
            actorNames.write(name+'\n')
        except:
            print actor.get_text()

    #actorNames.writelines(actorList)
    actorNames.close()
    time.sleep(2)
    #print actorList
    #print actorAll
    #print urlList


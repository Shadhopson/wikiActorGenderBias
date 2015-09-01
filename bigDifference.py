from testActorWords import actorWordList
from testActressWords import actressWordList

for word in actorWordList:
    try:
        normalizedActorWords =(actorWordList[word]*100000)/135014
        normalizedActressWords =(actressWordList[word]*100000)/85365
        difference =abs(normalizedActorWords - (actressWordList[word]*100000)/85365)
    except:
         normalizedActorWords =(actorWordList[word]*100000)/135014
         normalizedActressWords =1

         difference = abs((actorWordList[word]*100000)/135014 -0)
    menRatio = (normalizedActorWords+1)/(normalizedActressWords+1)
    womenRatio =  (normalizedActressWords+1)/(normalizedActorWords+1)
    if difference > 50 and (menRatio >1.5 or womenRatio>1.5):
        print word + " women: " + str(normalizedActressWords) + " men: " + str(normalizedActorWords)

print actorWordList["he"]
print actressWordList["he"]

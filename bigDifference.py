from actorWords import actorWordList
from actressWords import actressWordList
from actingData import genderData
for word in actorWordList:
    try:
        normalizedActorWords =(actorWordList[word]*100000)/genderData[2]
        normalizedActressWords =(actressWordList[word]*100000)/genderData[3]
        difference =abs(normalizedActorWords - (actressWordList[word]*100000)/genderData[3])
    except:
         normalizedActorWords =(actorWordList[word]*100000)/genderData[2]
         normalizedActressWords =1

         difference = abs((actorWordList[word]*100000)/genderData[2] -0)
    menRatio = (normalizedActorWords+1)/(normalizedActressWords+1)
    womenRatio =  (normalizedActressWords+1)/(normalizedActorWords+1)
    if difference > 20 and (menRatio >1.2 or womenRatio>1.2):
        print word + " women: " + str(normalizedActressWords) + " men: " + str(normalizedActorWords)
print actorWordList["he"]
print actressWordList["he"]

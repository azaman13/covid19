import nltk
from nltk import word_tokenize
import re
import spacy
nlp = spacy.load("en_core_web_sm")
getTogether = open('/Users/miriamblumenthal/Desktop/Desktop/ASLproject/getTogether.txt', 'r').readlines()
happyBirthday = open('/Users/miriamblumenthal/Desktop/Desktop/ASLproject/happyBirthday.txt', 'r').readlines()
ifYourHappy = open('/Users/miriamblumenthal/Desktop/Desktop/ASLproject/ifYourHappy.txt', 'r').readlines()
itsybitsy = open('/Users/miriamblumenthal/Desktop/Desktop/ASLproject/itsybitsy.txt', 'r').readlines()
jingleBells = open('/Users/miriamblumenthal/Desktop/Desktop/ASLproject/jingleBells.txt', 'r').readlines()
littleLamb = open('/Users/miriamblumenthal/Desktop/Desktop/ASLproject/littleLamb.txt', 'r').readlines()
rowYourBoat = open('/Users/miriamblumenthal/Desktop/Desktop/ASLproject/rowYourBoat.txt', 'r').readlines()
twinkleTwinkle = open('/Users/miriamblumenthal/Desktop/Desktop/ASLproject/twinkleTwinkle.txt', 'r').readlines()
wheelsOnBus = open('/Users/miriamblumenthal/Desktop/Desktop/ASLproject/wheelsOnBus.txt', 'r').readlines()
youAreMySunshine = open('/Users/miriamblumenthal/Desktop/Desktop/ASLproject/youAreMySunshine.txt', 'r').readlines()

getTogetherTagged = open('/Users/miriamblumenthal/Desktop/Desktop/ASLproject/getTogetherTagged.txt', 'w')
happyBirthdayTagged = open('/Users/miriamblumenthal/Desktop/Desktop/ASLproject/happyBirthdayTagged.txt', 'w')
ifYourHappyTagged = open('/Users/miriamblumenthal/Desktop/Desktop/ASLproject/ifYourHappyTagged.txt', 'w')
itsyBitsyTagged = open('/Users/miriamblumenthal/Desktop/Desktop/ASLproject/itsyBitsyTagged.txt', 'w')
jingleBellsTagged = open('/Users/miriamblumenthal/Desktop/Desktop/ASLproject/jingleBellsTagged.txt', 'w')
littleLambTagged = open('/Users/miriamblumenthal/Desktop/Desktop/ASLproject/littleLambTagged.txt', 'w')
rowYourBoatTagged = open('/Users/miriamblumenthal/Desktop/Desktop/ASLproject/rowYourBoatTagged.txt', 'w')
twinkleTagged = open('/Users/miriamblumenthal/Desktop/Desktop/ASLproject/twinkleTagged.txt', 'w')
wheelsOnBusTagged = open('/Users/miriamblumenthal/Desktop/Desktop/ASLproject/wheelsOnBusTagged.txt', 'w')
YouAreMySunshineTagged = open('/Users/miriamblumenthal/Desktop/Desktop/ASLproject/YouAreMySunshineTagged.txt', 'w')

def tag(file_read, file_write):
    text =''
    for line in file_read:
        text+=line
    text = word_tokenize(text)
    L = nltk.pos_tag(text)
    for t in L:
        file_write.write(' '.join(str(s) for s in t) + '\n')
    file_write.close()
    return L

tag(getTogether, getTogetherTagged)
tag(happyBirthday, happyBirthdayTagged)
tag(ifYourHappy, ifYourHappyTagged)
tag(itsybitsy, itsyBitsyTagged)
tag(jingleBells, jingleBellsTagged)
tag(littleLamb, littleLambTagged)
tag(rowYourBoat, rowYourBoatTagged)
tag(twinkleTwinkle, twinkleTagged)
tag(wheelsOnBus, wheelsOnBusTagged)
tag(youAreMySunshine, YouAreMySunshineTagged)
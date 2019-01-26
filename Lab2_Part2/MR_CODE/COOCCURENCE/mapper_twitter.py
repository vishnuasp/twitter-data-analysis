#!/usr/bin/env python
import sys
import string
import nltk 
import re
from itertools import izip
import sys  


list1=[]
nltk.download('stopwords')
nltk.download('wordnet')
STOPWORDS = nltk.corpus.stopwords.words('english')
lemma=nltk.wordnet.WordNetLemmatizer()

def change(words):
	words2=[]	
	topwords=['creepy','spooky','love','invest','paranormal','negative','watch','ghost','scary','spirit']
	for word in words:
		word=re.sub('[^A-Za-z]+', '', word)
		word=re.sub(r'[^\w]', '', word)
		word=word.lower() 
		word=lemma.lemmatize(word)	
		if (word in topwords and word != ''):
			words2.append(word)
	
	return (words2)

for line in sys.stdin:
    line = line.strip()
    words = line.split()
    wordsnew=change(words)  
    print (wordsnew)
    for i in range(0,len(wordsnew)):
	for j in range(i+1, len(wordsnew)):
		if (wordsnew[i]!=wordsnew[j]):	
			pair=wordsnew[i]+' '+wordsnew[j]
			print '%s,%s' % (pair,1)   

print ("-------mapper ends here-------")




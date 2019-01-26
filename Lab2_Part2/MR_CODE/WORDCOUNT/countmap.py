#!/usr/bin/env python
import sys
import string
import nltk 
import re
list1=[]
f1=open("/home/hadoop/hduser/output1.txt","r")
list1=f1.read()
print (list1)
nltk.download('stopwords')
nltk.download('wordnet')
STOPWORDS = nltk.corpus.stopwords.words('english')
lemma=nltk.wordnet.WordNetLemmatizer()

for line in sys.stdin:
    line = line.strip()
    words = line.split()
    for word in words:
	d=re.sub('[^A-Za-z]+', '', word)
	d=d.lower() 
	d=lemma.lemmatize(d)	
	#d=unicode(d,"utf-8")
	if (d not in STOPWORDS):
		print '%s %s' % (d, 1)
print ("-------mapper ends here-------")

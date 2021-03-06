import sys
import re
import json

def hw(sent_file,tweet_file):
    	f = sent_file
	scores = {} # initialize an empty dictionary
	for line in f:
	  term, score  = line.split("\t")  
	  # The file is tab-	delimited. "\t" means "tab character"
	  scores[term] = int(score)  # Convert the score to an integer.
	#loading of first round scores complete.
	
	tweets = tweetparse(tweet_file)
	tuplist = preptweets(tweets,scores)
	dynascores = {}	
	for tup in tuplist:
		for word in tup[0]:
		 if(tup[1]!=0):			
			if (word not in scores.keys()):
			 if (word not in dynascores.keys()):
				dynascores[word]=0
			 if tup[1]>0:
				dynascores[word] +=1
			 elif tup[1]<0:
				dynascores[word] -=1
	#print "scores:",scores.keys()
	#print "dynascores:", dynascores	
	for key in dynascores.keys():
		if len(key)!=0:
		 print key, dynascores[key]
		
	return dynascores

def preptweets(tweets,scores):
	newlist = []
	for tweet in tweets:
		#nonalpha = re.compile(r'[^a-z]+')
		#tokens = nonalpha.split(tweet.lower())
		tokens = tweet.split()		
		ssum = 0
		for word in tokens:
			try:
			 ssum = ssum + scores[word]
			except:
			 pass
		newlist.append((tokens,ssum))
		#print ssum
	#print newlist
	return newlist 	 

def tweetparse(tweet_file):
	data = []
	tweetlist = []
	for line in tweet_file:
		data.append(json.loads(line))
	for elem in data:
		try:
		 string= elem["text"]
		 #print type(string)
		 string=string.encode('utf-8')
		 tweetlist.append (string)
		except:
		 pass
	return tweetlist

def lines(fp):
    print str(len(fp.readlines()))

def main():
    sent_file = open(sys.argv[1])
    tweet_file = open(sys.argv[2])
    hw(sent_file, tweet_file)
    #lines(sent_file)
    #lines(tweet_file)

if __name__ == '__main__':
    main()

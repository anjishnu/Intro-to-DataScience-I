import sys
import json
import re

def hw(sent_file,tweets):
	
	f = sent_file
	scores = {} # initialize an empty dictionary
	for line in f:
	  term, score  = line.split("\t")  
	  # The file is tab-	delimited. "\t" means "tab character"
	  scores[term] = int(score)  # Convert the score to an integer.

	for tweet in tweets:
		nonalpha = re.compile(r'[^a-z]+')
		tokens = nonalpha.split(tweet.lower())
		#print "tokens", tokens
		ssum = 0
		for word in tokens:
			try:
			 ssum = ssum + scores[word]
			except:
			 pass
		print ssum	 

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
	tweets = tweetparse(tweet_file)	
	hw(sent_file,tweets)
    	#lines(sent_file)
    	#lines(tweet_file)

if __name__ == '__main__':
    main()

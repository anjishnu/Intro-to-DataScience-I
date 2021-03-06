import sys
import re
import json

def main():
    tweet_file = open(sys.argv[1])
    tweetlist = tweetparse(tweet_file)
    word_dict = {}
    Sum = 0
    for tweet in tweetlist:
	tweet = tweet.strip();	
	nonalpha = re.compile(r'[^a-z]+')
	tokens = nonalpha.split(tweet.lower())
	for word in tokens:
	   if len(word)>0:		
		Sum +=1		
		try:
		 word_dict[word]+=1
		except:
		 word_dict[word]=1
    for key in word_dict.keys():
	if (len(key)>0):
		print key, float(word_dict[key])/Sum



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

if __name__ == '__main__':
    main()

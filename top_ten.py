import sys
import re
import json

def main():
    tweet_file = open(sys.argv[1])
    hashes = tweetparse(tweet_file)
    hashitems = hashes.items()
    count = 0
    hashitems = sorted(hashitems, key = lambda item : -item[1])
    #print hashitems
    #print ("running")
    for item in hashitems:
	
	count +=1;
	if count>10:
		break
	try:	
		print item[0], item[1]
	except:
		count-=1
		pass

def tweetparse(tweet_file):
	#count = 0	
	data = []
	hashes = {}
	for line in tweet_file:
		#count+=1
		#if count>5000:
			#break
		data.append(json.loads(line))
	
	for elem in data:		
		try:
		 hashlist= elem["entities"]["hashtags"]
		 for hashtag in hashlist:
			temptext = hashtag["text"]
			if temptext in hashes.keys():
				hashes[temptext]+=1
			else:
				hashes[temptext]=1
		except:
		 pass
	return hashes

if __name__ == '__main__':
    main()

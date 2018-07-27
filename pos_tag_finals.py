# Tagging Features Set Matrix by Vikash Kumar | @00288822

from __future__ import division
import nltk
from nltk import word_tokenize, sent_tokenize
from nltk.tokenize import RegexpTokenizer
import urllib2
import bs4
from bs4 import BeautifulSoup

from nltk.corpus import stopwords
 #0-4 by Carey Rockwell              # 5-9 by Eleanor Hallowell Abbott
url = ['http://www.gutenberg.org/files/19709/19709-8.txt','http://www.gutenberg.org/files/21092/21092-8.txt','http://www.gutenberg.org/files/19027/19027-8.txt','http://www.gutenberg.org/files/18520/18520.txt','http://www.gutenberg.org/files/18753/18753.txt',
'http://www.gutenberg.org/files/26399/26399-8.txt','http://www.gutenberg.org/files/15728/15728.txt','http://www.gutenberg.org/files/22982/22982-readme.txt','http://www.gutenberg.org/files/18665/18665.txt','http://www.gutenberg.org/files/20213/20213-8.txt']

fil = open('pos_tag_finals_data.dat','w+')      
#11 features name
features_name = ['total_alphabets','count_words','count_words_w/o_Punctuation','total_Vocabularies','percent_punctuation','Density','Verbs_Count','Nouns_count','Pronouns_count','Adjectives_count','Adverbs_count']


def features(url):
	feature_set = []
	html = urllib2.urlopen(url).read()
	soup = BeautifulSoup(html, 'lxml')							#opens the url and filters the html's
	text = soup.get_text()
	
	total_alphas = len(text)  #1								#counts total alphabets

	tokenized_text	= nltk.wordpunct_tokenize(text)				#tokenizes the text
	count_words = len(tokenized_text)	#2						#total words
	
	words = [w.lower for w in tokenized_text if w.isalpha()]	#removes punctuations
	count_words_wo_punct = len(words)	#3						#counts the words without punctuations

	count_vocabs =  len(sorted(set(words)))		#4				#gets unique vocabulary and sort them
	percent_punct = (1- (count_words_wo_punct/count_words))*100	#5 gives the percent punctuation
	density = count_vocabs/count_words_wo_punct			#6		#counts the density
	pos_tokens = nltk.pos_tag(tokenized_text)					#gets all the POS tags
	verbs = [words for word,pos in pos_tokens if (pos == 'VB' or pos == 'VBD' or pos == 'VBG' or pos == 'VBN' or pos == 'VBP' or pos == 'VBZ')]
	verbs_count = len(verbs)		#7							#gets all the verbs and counts it
	nouns = [words for word,pos in pos_tokens if (pos == 'NN' or pos == 'NNS' or pos == 'NNP' or pos == 'NNPS')]
	nouns_count = len(nouns)		#8							#gets all the nouns and counts it
	pronouns = [words for word,pos in pos_tokens if (pos =='PRP' or pos == 'PRP$')]
	pronouns_count = len(pronouns)		#9						#gets all the pronouns and counts it
	adjectives = [words for word, pos in pos_tokens if(pos == 'JJ' or pos =='JJR' or pos =='JJS' )]
	adjectives_count = len(adjectives)		#10					#gets all the adjectives and counts it	
	adverbs = [words for word, pos in pos_tokens if (pos == 'RB' or pos == 'RBR' or pos =='RBS')]
	adverbs_count = len(adverbs)		#11						#gets all the Adverbs and counts them	
	feature_set.append(total_alphas)		#<-1				#appends the features into the list
	feature_set.append(count_words)			#<-2
	feature_set.append(count_words_wo_punct)#<-3
	feature_set.append(count_vocabs)		#<-4
	feature_set.append(percent_punct)		#<-5
	feature_set.append(density)				#<-6
	feature_set.append(verbs_count)			#<-7
	feature_set.append(nouns_count)			#<-8
	feature_set.append(pronouns_count)		#<-9
	feature_set.append(adjectives_count)	#<-10
	feature_set.append(adverbs_count)		#<-11	
	return feature_set
	
book_features = []
for i in range(10):
	book_features.append(features(url[i]))						#gets all the features by calling the function and appending them into the list    					

for i in range(11):
	fil.write("%-27s		"%(features_name[i]))				#appends the feature into the
	for j in range(10):
		fil.write("%-14s		"%(book_features[j][i]))		#appends the different book's features into the file		

	fil.write("\n")

fil.close()														#closing the file


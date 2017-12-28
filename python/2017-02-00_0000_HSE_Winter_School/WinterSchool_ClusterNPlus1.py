import requests
import re
from bs4 import BeautifulSoup
import pymorphy2
from tqdm import tqdm
import numpy as np
from sklearn.cluster import DBSCAN
from sklearn.cluster import KMeans
import time
import math

# Download a page from nplus1.ru by adress adr.
def getArticleTextNPlus1(adr):
 r = requests.get(adr)
 time.sleep(1) # We are ethical hackers.

 # Extract information from the page. Using regular expressions for it easier than consider the Dom structure of the page.
 tables=re.split("</div>",re.split('="tables"', r.text)[1])[0]
 t1=re.split("</time>", re.split("<time", tables)[1])[0]
 n_time=re.split("</span>", re.split("<span>", t1)[1])[0]
 n_date=re.split("</span>", re.split("<span>", t1)[2])[0]
 n_rubr=re.split(">", re.split("</a>", re.split("<a href", tables)[1])[0])[1]
 n_diff=re.split("</span>", re.split('"difficult-value">', tables)[1])[0]
 n_head=re.split("</h1>",re.split('<h1>', r.text)[1])[0]
 n_author=re.split('" />',re.split('<meta name="author" content="', r.text)[1])[0]
 n_text=re.split("</div>", re.split("</figure>", re.split('</article>',re.split('<article', r.text)[1])[0])[1])[1]    
 n_text=re.sub("<br>|<br\/>|<p>|<\/p>", " ", str.lower(n_text))

 # We need BeautifulSoup to cut of all the tags from the extracted text.
 beaux_text=BeautifulSoup(n_text, "lxml")
 n_text=beaux_text.get_text() 

 return [n_time, n_date, n_rubr, n_diff, n_author, n_head, n_text]

# Download all news for a day from nplus1.ru 
def getNPlus1Day(adr, day):
 # Requesting page using the Requests library.
 r = requests.get(adr)
 # All addresses are bordered by this tag.
 refs=re.split('<article class="item item-news item-news', r.text)
 database=[]

 # Downloading news if any.
 if len(refs)>0: 
  for t in tqdm(refs[1:], desc='day '+day):
   href=re.split('"', t)[6]
   database.append(getArticleTextNPlus1("https://nplus1.ru"+href))
 return database
#def getNPlus1Day(adr, day):

# We are interested in words of this parts of speech only.
POSes=set(['NOUN', 'VERB', 'ADJF', 'PRTF', 'GRND', 'ADJS', 'PRED', 'PRCL', 'INFN'])

# Creating the vector of words frequencies.
def getFreqVector(text, morph):
 # Let a Russian word be a sequence of Russian characters.
 words=re.findall("[А-Яа-я]+\-[А-Яа-я]+|[А-Яа-я]+", text)

 pwords=[]
 for w in words[:-1]:
  # Gathering initial forms of the given word usin Pymorphy2.
  prsd=morph.parse(w) 
  # Берем только значимые части речи. Так как вариантов анализа очень много, просто берем самый вероятный.
  if prsd[0].tag.POS in POSes:
   pwords.append(prsd[0].normal_form)

 # Строим словарь из начальных форм текста.
 uwords=set(pwords)
 dwords={w:0 for w in uwords}

 # Считаем частоты встречаемости начальных форм.
 for w in words[:-1]:
  prsd=morph.parse(w) 
  if prsd[0].normal_form in pwords:
   dwords[prsd[0].normal_form]+=1

 # Возвращаем все слова, которые встретились чаще, чем 1 раз. 
 dwords2={w:dwords[w] for w in dwords.keys() if dwords[w]>1}
 return dwords2
#def getFreqVector(text, morph):

# Calculating cosine similarity (distance) between vectors. 
# 1 - text are the same, 0 - texts are sharing no any word.
# Form formula consult https://en.wikipedia.org/wiki/Cosine_similarity
def cosineSimilarity(words1, words2):
 cntr=0
 for w in words1:
  if w in words2:
    cntr+=words1[w]*words2[w]
 cntr1=0
 for w in words1:
  cntr1+=words1[w]*words1[w]
 cntr2=0
 for w in words2:
  cntr2+=words2[w]*words2[w]
 if cntr1*cntr2==0:
  return 0;
 return cntr/(math.sqrt(cntr1*cntr2))
#def cosineSimilarity(words1, words2):

# main
# Downloading news for 30 days of the November 2016.
all_days=[]
for i in range(1, 30): 
 a_day = getNPlus1Day('https://nplus1.ru/news/2016/01/'+str(i)+'/', str(i))
 all_days+=a_day

# Create an PyMorphy2 object for grammatical analysis.
morph = pymorphy2.MorphAnalyzer()

# Creating frequency vectors for news.
words=[]
for t in tqdm(all_days, desc='morph-ing'):
 words.append(getFreqVector(t[6], morph))

# Calculating matrix of distances for new. Comparing any news with any.
similarity=[[0 for r in words] for r2 in words]
for i in tqdm(range(len(words)), desc='making everything similar'):
 for j in range(i+1, len(words)):
   sim=cosineSimilarity(words[i], words[j])
   similarity[i][j]=1-sim # 1-sim because we need distance but not similarity. If cosine measure is equal to 1 then distance is equal to 0.
   similarity[j][i]=1-sim

# Clustering using SciPy.sklearn using k-means algorithm. 
# https://ru.wikipedia.org/wiki/K-means
# http://scikit-learn.org/stable/modules/clustering.html
# http://scikit-learn.org/stable/modules/generated/sklearn.cluster.KMeans.html
clusters=KMeans(n_clusters=32, precompute_distances = False).fit_predict(similarity)

# Just output.
for i in range(max(clusters)):
 print("+++ "+str(i)+" +++")
 for l in range(len(words)):
  if clusters[l]==i:
   print(all_days[l][5])

# Clustering using DBSCAN.
# https://en.wikipedia.org/wiki/DBSCAN
clusters = DBSCAN(eps=0.7, min_samples=2, metric='precomputed').fit(similarity)

print(clusters.labels_)

for i in range(max(clusters.labels_)):
 print("+++"+str(i)+"+++")
 for l in range(len(words)):
  if clusters.labels_[l]==i:
   print(all_days[l][5])

print("---None---")
for l in range(len(words)):
 if clusters.labels_[l]==-1:
  print(all_days[l][5])


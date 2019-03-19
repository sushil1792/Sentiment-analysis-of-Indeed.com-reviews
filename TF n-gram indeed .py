import nltk
import pandas as pd
import os
os.chdir('C:\\Users\\rahul.g\\Downloads\\study\\project-Indeed reviews')

df = pd.read_csv("delta.csv")
reviews = list(df[df['sentiment']>0.5]['Review_Text'])
len(reviews)

#Ans 1 - TOKENIZE
token_d1 =[]
for i in range(0,len(reviews)):
    token_d1.append(nltk.word_tokenize(reviews[i].lower()))
print(token_d1)

#Ans 2- LEMMATIZE
# lemmatizer = nltk.stem.WordNetLemmatizer()
# lemm_token_d2 = []
# for i in range(0,len(token_d1)):
#     lemm_token_d2.append([lemmatizer.lemmatize(token) for token in
#                           token_d1[i] if token.isalpha()])
# print(lemm_token_d2)
# print(len(lemm_token_d2))
#
#Ans 4 - TF
from sklearn.feature_extraction.text import CountVectorizer
tf_input = []
vectorizer3 = CountVectorizer(ngram_range=(4, 6), min_df=3)
for i in range(0,len(token_d1)):
    temp = ''
    for j in range(0,len(token_d1[i])):
        temp += token_d1[i][j]+' '
    tf_input.append(temp[:-1])

vectorizer3.fit(tf_input)
v3 = vectorizer3.transform(tf_input)
print(v3.toarray())
print(vectorizer3.vocabulary_)
x=vectorizer3.vocabulary_

df = pd.DataFrame(v3.toarray())
df.to_csv('tf.csv', index=False)

import csv
with open('vocab.csv', 'w') as f:
    for key in x.keys():
        f.write("%s,%s\n"%(key,x[key]))
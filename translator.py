from googletrans import Translator
import streamlit as st


st.title('Hinglish Summarizer')
translator = Translator()

st.subheader('Enter a Sentence')
word = st.text_input('')
result = translator.translate(word, dest ='en')
output = result.text
st.subheader('After Translating')
st.write(output)


import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize, sent_tokenize
   
stopWords = set(stopwords.words("english"))
words = word_tokenize(output)
   

freqTable = dict()
for word in words:
    word = word.lower()
    if word in stopWords:
        continue
    if word in freqTable:
        freqTable[word] += 1
    else:
        freqTable[word] = 1

sentences = sent_tokenize(output)
sentenceValue = dict()
   
for sentence in sentences:
    for word, freq in freqTable.items():
        if word in sentence.lower():
            if sentence in sentenceValue:
                sentenceValue[sentence] += freq
            else:
                sentenceValue[sentence] = freq
   
   
   
sumValues = 0
for sentence in sentenceValue:
    sumValues += sentenceValue[sentence]
   
   
average = int(sumValues / len(sentenceValue))
   
st.subheader('After Summarize')
summary = ''
for sentence in sentences:
    if (sentence in sentenceValue) and (sentenceValue[sentence] > (1.2 * average)):
        summary += " " + sentence
st.write(summary)

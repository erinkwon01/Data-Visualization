
import json
from textblob import TextBlob
from wordcloud import WordCloud

import matplotlib
matplotlib.use('TkAgg')
import matplotlib.pyplot as plt

tweetFile = open("TWEETS.json", "r")
tweetData = json.load(tweetFile)
tweetFile.close()

polarity = []
subjectivity = []

# Continue your program below!
for each in tweetData:
    tb = TextBlob(each["text"])
    polarity.append(tb.polarity)
    # sump=sum(polarity)
    averagep= sum(polarity)/len(polarity)
    subjectivity.append(tb.subjectivity)
    # sums=sum(subjectivity)
    averages= sum(subjectivity)/len(subjectivity)
print("Average of polarity=", averagep)
print("Average of subjectivity=", averages)

num_bins = 5
n, bins, patches = plt.hist(polarity, num_bins, facecolor = 'pink', alpha = 0.75)
plt.show()

n, bins, patches = plt.hist(subjectivity, num_bins, facecolor = 'green', alpha = 0.5)
plt.show()

twt_str = ""
word_count = {}
for each in tweetData:
    twt_str += (each["text"])
twt_str = twt_str.lower()
twtblob = TextBlob(twt_str)
tweet_list = twtblob.words
for each in tweet_list:
    if len(each) > 3 and each.isalpha() == True and each != "https":
        if each not in word_count:
            word_count[each] = 1
        else:
            word_count[each]+=1
print(word_count)

wc = WordCloud(background_color = "white", width=900, height=500,
relative_scaling=1).generate_from_frequencies(word_count)

plt.imshow(wc, interpolation = 'bilinear')
plt.show()


# coding: utf-8

# In[1]:


import os 
import nltk 
import syllables 
import numpy as np
import random
import re
import string 
from collections import defaultdict



# In[60]:


def walk_graph(graph, distance, start_node=None):
    #returns word list from randomly weighted walk
    if distance <= 0:
        return []
    if not start_node:
        start_node = random.choice(list(graph.keys()))
        
     
        
    weights = np.array(
    list(markov_graph[start_node].values()),
    dtype=np.float64)
    weights /= weights.sum()
    
    choices = list(markov_graph[start_node].keys())
    chosen_word = np.random.choice(choices,None,p=weights)
    #determine the syllables of the chosen word
    syl = syllables.estimate(chosen_word)
    
    
    
    #return word, recusively calling function, subtract based on number of syllables in chosen word
    return [chosen_word] + walk_graph(graph, distance = distance-syl, start_node = chosen_word)


words = (walk_graph(markov_graph, distance = 5))
poem.append(words)
print('  '.join(words))

words = (walk_graph(markov_graph, distance = 7))
poem.append(words)
print('  '.join(words))


words = (walk_graph(markov_graph, distance = 5))
poem.append(words)
print('  '.join(words))



    


# In[58]:


#open file containing Basho poems
with open('basho.txt', encoding="utf-8") as file:
    text = file.read()
  
file.close()
#separate text into words
words = text.split()
#remove punctuation 
table = str.maketrans('','',  string.punctuation)
tokenized_text = [ 
    w.translate(table) 
    for w in words
    if w != (' ', "translated","translation,","–")
    
    
]
  

markov_graph = defaultdict(lambda: defaultdict(int))

last_word = tokenized_text[0].lower()
for word in tokenized_text[1:]:
    word = word.lower()
    markov_graph[last_word][word]+= 1
    last_word = word


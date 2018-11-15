import enchant
import nltk,sys
from word_recognition import *
from nltk.corpus import brown
from heapq import heappush, heappop


def correct_text(text_list) :
    final_list = []
    for i in text_list :
        if not i in word_list :
            print(i)
            heap = []
            for j in word_list :
                d = lv_distance(i,j)
                if d<0 :
                    d = abs(d)
                heappush(heap, (d,j))
            final_list.append(heappop(heap)[1])
        else :
            final_list.append(i)
    return final_list



def lv_distance(a, b):
    string1 = a
    string2 = b
    distance = 0
    n1 = len(string1)
    n2 = len(string2)
    
    if n1 >= n2:
        for i in range(n1):
            if i < n2:
                if string1[i] != string2[i]:
                    distance += 1
            else:
                distance += 1
    else:
        for i in range(n2):
            if i < n1:
                if string2[i] != string1[i]:
                    distance -= 1
            else:
                distance -= 1
    
    
        
    return distance


word_list = brown.words()

rec = get_recognized_words_list(sys.argv[1])
print (" ".join(rec))
rec = correct_text(rec)
print (" ".join(rec))
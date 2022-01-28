import numpy as np
from context import Context
import multiprocessing
import pdb


def minfunc(lengths):
   return(max(lengths))
#   return -1*np.mean([1./l for l in lengths])
#   return -1*sum([i==1 for i in lengths])
   

def read_wordlist(fname):
    words=[i.strip(" \n")  for i in open(fname)]
    return words

    
possible_answers=read_wordlist("wordle-answers-alphabetical.txt")
possible_guesses=read_wordlist("wordle-allowed-guesses.txt")+possible_answers
alphabet='abcdefghijklmnopqrstuvwxyz'
a_lookup= {v:i for i,v in enumerate(alphabet)}


min_max_l = multiprocessing.Value('d', 999999)
def get_allowed_set_len(guess,context,verbose=False):
    global min_max_l
    _l=[]
    
#    if min_max_l.value==1:return 99999

    allowed_answers=allowed_list(possible_answers,context.copy())
    for pa in allowed_answers:
        _con,win=evaluate(guess,pa)
        new_context=context.copy()
        new_context.add_context(_con)
        #print('guess c',_con)
        #print('guess new_c',new_context)
        #print('guess orig c',context)
#        pdb.set_trace()
        wl=allowed_list(allowed_answers,new_context)
        setl=len(wl)
        _l.append(setl)
        if minfunc(_l) > min_max_l.value:
            break


#    rval=max(_l)
    rval=minfunc(_l) 
    rarg=np.argmax(_l)
    if rval <= min_max_l.value:
        if rval > 10 and verbose:
           print('mml',rval,min_max_l.value,guess,allowed_answers[rarg], np.mean(_l))
        min_max_l.value=rval
#    if rval==1: print("one word",_l)
    return rval


def evaluate(test_word,answer):
    exact={}
    included={}
    not_included={}
    for ci,v in enumerate(test_word):
        if v==answer[ci]:
            if not v in exact:
                exact[v]=[]
            exact[v].append(ci)
        elif v in answer:
            if not v in included:
                included[v]=[]
            included[v].append(ci)
        else:
            if v not in not_included:
                not_included[v]=[1]
        win=test_word==answer
    new_context=Context(exact,included,not_included)
    #print('eval',new_context)
    return new_context,win


def allowed(word,context):
    for v in context.excluded:
        if v in word: return False
    for v,exact_i in context.exact.items():
        for i in exact_i:
            if word[i]!=v: return False
    for v,not_p in context.included.items():
        if v not in word:return False
        for i in not_p:
            if word[i]==v: return False
    return True

def allowed_list(word_list,context):
    return [w for w in word_list if allowed(w,context)]

        
def build_freq_table(allowed_list):    
    freq_table=np.zeros((5,26))
    for word in allowed_list:
        for wi,c in enumerate(word):
            ci=a_lookup[c]
            freq_table[wi,ci]+=1

    freq_table=freq_table/np.sum(freq_table[0,:])
    return freq_table        



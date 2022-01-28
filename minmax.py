import utils
import numpy as np
from context import Context
from multiprocessing import Pool,Value
import atexit
from itertools import repeat
import pdb
import sys






class MinMax():
    def __init__(self,start_guess=None):
        self.start_guess=start_guess
        self.start=True
        self.context=Context({},{},{})
        
        
    def guess(self,allowed_answers,allowed_guesses):
        utils.min_max_l.value=99999
        pool=Pool(13)
#        atexit.register(pool.close)
      
        if self.start and self.start_guess != None:
            self.start=False
            pool.close()
            return self.start_guess

        lengths=[]
        test=len(allowed_guesses)
        if test==0:
            print("Some Thing has gone wrong, no possible answers remain")
            sys.exit()
#        for g in allowed_guesses:
#            lengths.append(utils.get_allowed_set_len(g,self.context.copy()))
#            assert(len(allowed_guesses) ==test)
        #print(self.context)
        lengths=pool.starmap(utils.get_allowed_set_len, zip(allowed_guesses,repeat(self.context,len(allowed_guesses))) )

        mval=min(lengths)
        m_options=[i for i,v in enumerate(lengths) if v==mval]
        w_ans=[i for i in m_options if allowed_guesses[i] in allowed_answers]
        if len(w_ans)!=0:
            wi=w_ans[0]
        else:
           # print('no options',[allowed_guesses[i] for i in m_options])
            wi=m_options[0]
#        pool.kill()
        pool.close() 
#        pool.terminate()
        return allowed_guesses[wi]
    
    def reset(self):
        self.context=Context({},{},{})
        self.start=True
    #first guess in serai

    def trail(self,answer,verbose=False):
        if verbose: print("Answer:",answer)
        allowed_words=list(utils.possible_guesses)
        allowed_answers=list(utils.possible_answers)
        itr=0
        while True:
            if len(allowed_answers) ==1:
                guess=allowed_answers[0]
            else:
                guess=self.guess(allowed_answers,utils.possible_guesses)
#            print(guess)
#            print('ag',self.context)
            
            _con,win=utils.evaluate(guess,answer)
            self.context.add_context(_con)
            #print(self.context)
            allowed_answers= utils.allowed_list(utils.possible_answers,self.context)
            #print(allowed_answers)
            itr+=1
#            pdb.set_trace()
            if verbose:
                print('minmax:',guess,len(allowed_answers))
                if len(allowed_answers) < 10: print('Possible Ans: ',allowed_answers)
            if win:
                print('Win!',itr)
                break
        self.reset()
        return itr


    def play(self,verbose=False):
        allowed_words=list(utils.possible_guesses)
        allowed_answers=list(utils.possible_answers)
        itr=0
        while True:
            if len(allowed_answers) ==1:
                guess=allowed_answers[0]
            else:
                guess=self.guess(allowed_answers,utils.possible_guesses)
            print("Enter: ", guess," ")

            _con=input('Enter Worlde Output String 5x(x/y/g): ')
            win=False
            if _con=='ggggg':win=True
#            _con,win=utils.evaluate(guess,answer)
            
            self.context.add_context_from_pattern(guess,_con)
            #print(self.context)
            allowed_answers= utils.allowed_list(utils.possible_answers,self.context)
            if verbose: print('Possible words left:',allowed_answers)
            itr+=1
            if len(allowed_answers) < 10: print(allowed_answers)
            if win:
                print('Win!',itr)
                break
        self.reset()
        return itr



    

if __name__=="__main__": 
    player=MinMax('arise')#arise #trace most likley to win
    player.play()
#    player.trail('serai',verbose=True)
    if False:
        player.trail('fishy',verbose=True)
        player.trail('whack',verbose=True)

        player.trail('begun',verbose=True)
        itrs=[]
        for i in range(1000):
            word=np.random.choice(utils.possible_answers)
            itrs.append(player.trail(word,verbose=True))
            hist=np.zeros(7)
            for i in itrs:
                if i > 6: i=6
                hist[i]+=1
            print('score',np.mean(itrs),hist)
        
#itrs=[]

#for i in tqdm(possible_answers):
#    try:itrs.append(trail(i))
#    except: print(i)

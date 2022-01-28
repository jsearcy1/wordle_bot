from copy import deepcopy

class Context():
    # A class to define the world context
    # exact is a dictionary for each know letter and a list of it's locations in a word
    # inclued is a diction for each letter in the guess and a list of the locations it does not contain
    # excluded is a dictionary with all the letters that did not match with a dummy value i.e. {'a':1}
    
    def __init__(self,exact,included,excluded):
        self.included=included
        self.excluded=excluded
        self.exact=exact

    def combine_dict(self,dict1,dict2):
        for v,indexs in dict2.items():
            if v in dict1:
                dict1[v]+=dict2[v]
                dict1[v]=list(set(dict1[v]))
            else:
                dict1[v]=list(set(dict2[v].copy()))
        return dict1
    def copy(self):
        return Context(deepcopy(self.exact),deepcopy(self.included),deepcopy(self.excluded.copy()))
                
    def add_context_from_pattern(self,word,pattern):
        for ci,p in enumerate(pattern):
            if p =='y':
                indict={word[ci]:[ci]}
                self.combine_dict(self.included,indict)
            elif p =='g':
                indict={word[ci]:[ci]}
                self.combine_dict(self.exact,indict)
            else:
                indict={word[ci]:[1]}
                self.combine_dict(self.excluded,indict)

    def add_context(self,context):
        self.included= self.combine_dict(self.included,context.included)
        self.exact=self.combine_dict(self.exact,context.exact)
        self.excluded=self.combine_dict(self.excluded,context.excluded)
 
    def __str__(self):
        ilist=['?','?','?','?','?']
        for v,ind in self.exact.items():
            for i in ind:
                ilist[i]=v
        estring="".join(ilist)
        istring="w/" + "".join(list(self.included.keys()))
        xstring="!"+"".join(list(self.excluded.keys()))
#        print(self.exact,self.included,self.excluded)
        return ":".join([estring,istring,xstring])
        

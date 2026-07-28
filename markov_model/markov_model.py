from symboltable import SymbolTable
import stdio
import stdrandom


class MarkovModel(object):
    # Creates a Markov model of order k from the given text.
    def __init__(self, text, k):
        self._text=text
        self._order=k
        self._length=len(self._text)

        _st=SymbolTable()
        self._text_array=[]
        for i in text:
            self._text_array.append(i)
        
        for i in range(0,self._length):
            
            k_string=""
            for j in range(0,k):
               
                if i!=0:
                    k_string+=str(self._text_array[(i+j)%self._length])

                else:
                    k_string+=str(self._text_array[i+j])
               
                if k_string in _st and len(k_string)==k:
                    continue
                elif k_string not  in _st and len(k_string)==k:
                    _st[k_string]=SymbolTable()
                
            if i+k==0:
                char=self._text_array[i+k]
            else:
                char=self._text_array[(i+k)%self._length]
            
            if char not in _st[k_string]:
                _st[k_string][char]=0
                

            _st[k_string][char]+=1
            self._st=_st
       
    # Returns the order this Markov model.
    def order(self):
        
        return(self._order)
        

    # Returns the number of occurrences of kgram in this Markov model; and 0 if kgram is nonexistent. Raises an error 
    # if kgram is not of length k.
    def kgram_freq(self, kgram):
        if kgram not in self._st:
            return(0)
        frequency=0
        #stdio.writeln(kgram)
        
        for w in self._st[kgram].keys():
            #stdio.writeln(w)
            frequency+=self._st[kgram][w]
            #frequency=self._st.keys[kgram]
        return(frequency)


    # Returns number of times character c follows kgram in this Markov model; and 0 if kgram is nonexistent or if it 
    # is not followed by c. Raises an error if kgram is not of length k.
    def char_freq(self, kgram, c):
        if kgram not in self._st:
            return(0)
        if c not in self._st[kgram]:
            return(0)
        char_frequency=self._st[kgram][c]
        return(char_frequency)


    # Returns a random character following kgram in this Markov model. Raises an error if kgram is not of length k or 
    # if kgram is nonexistent.
    def rand(self, kgram):
        rand_list=[]
        sum_all=0
        x_holder=[]
        probs_list=[]
        for i in self._st[kgram].keys():
            x=self.char_freq(kgram,i)
            sum_all+=x
            rand_list.append(i)
            x_holder.append(x)
            probs_list.append(0)
            #stdio.writeln(x_holder)
        for j in range(len(x_holder)):
            #stdio.writeln(j)
            #stdio.writeln(sum_all)
            probs_list[j]=x_holder[j]/sum_all
            
        #stdio.writeln(rand_list)
        y=stdrandom.discrete(probs_list)
        #stdio.writeln(probs_list)
        #stdio.writeln(rand_list)
        #stdio.writeln(y)
        return(rand_list[y])


    # Generates and returns a string of length n from this Markov model, the first k characters of which is kgram.
    def gen(self, kgram, n):
        #new_text=kgram
        #kgram_list=""
        #j=0
        #while j<n-self.order:
        #    char=self.rand(kgram)
        #    new_text+=char
        #    kgram+=char
        #    kgram=kgram[1:]
        #    j+=1
        #return(new_text)
            # Generates and returns a string of length n from this Markov model, the first k characters of which is kgram.
    
        new_text = kgram
        j = 0
        while j < n - self._order:
            char = self.rand(kgram)
            new_text += char
            kgram = new_text[-self._order:]
            j += 1
        return new_text

    # Replaces unknown characters (~) in corrupted with most probable characters from this Markov model, and returns 
    # that string.
    def replace_unknown(self, corrupted):
        original = ""
        
        for i in range(len(corrupted)):
            if corrupted[i] == "~":
                j=1
                prev_chars=""
                while j<=self.order():
                    if i-self._order+j-1>0:
                        prev_chars+=corrupted[i-self._order+j-1]
                    j+=1
                next_char=corrupted[i+1]
                word_max=self.__getlikelyletter__(prev_chars,next_char)
                #stdio.writeln(word_max)

                original+=str(word_max)
            else:
                original += corrupted[i]
        return original
    
    def __getlikelyletter__(self,kgram,nextchar):
       
        table=self._st[kgram]
        max_char_freq=[]

        char_list=[]
        for word in table.keys():
            #if self.char_freq(kgram,word)>max_char_freq:
            max_char_freq.append(self.char_freq(kgram, word))
            
            char_list.append(word)
        best_guess=""
        valid_answers=[]
        for i in range(len(max_char_freq)):
            max=_argmax(max_char_freq)
            if len(best_guess)==0:
                best_guess=char_list[max]
            
            new_kgram=kgram[1:]+char_list[max]
            if self.kgram_freq(new_kgram)==0:
                max_char_freq[max]=0
                continue
            else:
                if self.char_freq(new_kgram,nextchar)!=0:
                    
                    #valid_answers.append(new_kgram)
                    
                    

                    return(char_list[max])
                else:
                    max_char_freq[max]=0
        #max_freq=0
        #for answer in valid_answers:
            #stdio.writeln(answer)
            #if self.char_freq(answer,nextchar)>max_freq:
                #max_freq=self.char_freq(answer,nextchar)
                #best_guess=answer[-1]
                #stdio.writeln(best_guess)
                #stdio.writeln(max_freq)




        return(best_guess)
                
                
        
# Given a list a, _argmax returns the index of the maximum value in a.
def _argmax(a):
    return a.index(max(a))

# Unit tests the data type [DO NOT EDIT].
def _main():
    model = MarkovModel("gagggagaggcgagaaa", 2)
    stdio.writeln("model       = MarkoveModel(\"gagggagaggcgagaaa\", k = 2)")
    stdio.writef("freq(ag)    = %d\n", model.kgram_freq("ag"))
    stdio.writef("freq(cg)    = %d\n", model.kgram_freq("cg"))
    stdio.writef("freq(gc)    = %d\n", model.kgram_freq("gc"))
    stdio.writef("freq(xx)    = %d\n", model.kgram_freq("xx"))
    stdio.writef("freq(aa, a) = %d\n", model.char_freq("aa", "a"))
    stdio.writef("freq(ga, g) = %d\n", model.char_freq("ga", "g"))
    stdio.writef("freq(gg, c) = %d\n", model.char_freq("gg", "c"))
    stdio.writef("freq(xx, x) = %d\n", model.char_freq("xx", "x"))
    stdio.writef("freq(gg, x) = %d\n", model.char_freq("gg", "x"))
    stdio.writeln(model.replace_unknown('acg~ga'))

if __name__ == "__main__":
    _main()

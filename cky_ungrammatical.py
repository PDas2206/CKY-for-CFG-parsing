# -*- coding: utf-8 -*-

"""
This is a program for the CKY Recognizer to test some ungrammatical sentences. 
It reads the grammar from "atis-grammar-cnf.cfg" which is already in CNF, and uses it to 
recognize the test sentences in the "test-sentences-ungrammatical.txt" file.

The output of this program is another file, "recognizer_ungrammatical_output.txt",
containing the test sentences and their corresponding results i.e. a statement 
stating whether the sentence is in the language of the grammar or not.

To store the CKY matrix, a dictionary of sets has been used wherein the dictionary 
keys are the cell numbers (row,column) of the CKY and their corresponding values 
are the set of Non Terminals/Terminals that need to be stored in that particular cell.

The CKY matrix that is being created and used in this program logically looks like this:
    
      ___j=0________j=1________j=2_______j=3____
  i=0 |____what_|____is___|____the___|___fare__|
  i=1 |SIGMA,...|pt_VERB,.|__..._____|__...____|
  i=2 |__...____|___...___|__..._____|
  i=3 |__...____|___...___|
  i=4 |__SIGMA__|
"""


import nltk
from nltk import CFG
from nltk import grammar
from collections import defaultdict
import timeit



grammar_cnf= ''.join(open("../data/atis-grammar-cnf.cfg",'r').readlines()) # load grammar in cnf form
g_cnf=CFG.fromstring(grammar_cnf)


start_symbol=g_cnf.start()



cky_dict=defaultdict(set) # The dictionary that will store the CKY matrix
            
cky=[] # This list will only store the words of the test sentence (or the terminals)

# Some other data structures required in the program            
left_nt_set=[]
right_nt_set=[]
grammar_list=[]


with open("../data/test-sentences-ungrammatical.txt", "r", encoding="utf-8") as test_file:
    with open("recognizer_ungrammatical_output.txt", "w", encoding="utf-8") as file_output:
        
        
        tag_start=timeit.default_timer()
        test_sentence=[]
        for line in test_file:
            print(f'{str(line)}',end="", file=file_output)
            line=line.split()
            test_sentence=line
           
            cky_dict.clear()
            cky.clear()
            left_nt_set.clear()
            right_nt_set.clear()
            grammar_list[:]=[]
            
            # Apending the words of the sentence (terminals) into the CKY List
            cky.append(test_sentence)
            
            # Filling up the first row of the CKY matrix               
            for j in range(len(test_sentence)):
                    
                grammar_list[:]=[]
                   
                for rules in g_cnf.productions():
                    
                    # Checking for rules in the grammar wherin the words from the test sentence are the RHS of a rule
                    if cky[0][j] in rules.rhs():
                        grammar_list.append(rules.lhs()) # appending the LHS of those rules into the list, to store them in the CKY dictionary
                # Updating the CKY dict with the LHS of the rules                
                cky_dict[(1,j)].update(grammar_list) 
                    
                  
            grammar_list[:]=[]            
            for i in range(2,len(test_sentence)+1,1):  
               
                for j in range(len(test_sentence)-i+1):
                    
                                       
                    for k in range(1,i,1):
                        grammar_list[:]=[]
                            
                        left_nt_set=cky_dict[(k,j)] # The "Left" non terminals are being stored
                        right_nt_set=cky_dict[(i-k,k+j)] # The "Right" non terminals are being stored
                        
                        # Looking for rules in the grammar wherein any of the 
                        #"Left" non terminals are the first position nonterminal of the 2-nonterminal CNF grammar;
                        #if so then checking if that rule has the "Right" nonterminals as the second.
                        # If such a rule exists, store the LHS of that rule 
                        for nt in left_nt_set:
                            productions_this=g_cnf.productions(rhs=nt)
                            for production in productions_this:
                                if production.rhs()[1] in right_nt_set:
                                    lhs_this=production.lhs()
                                    grammar_list.append(lhs_this)
                                        
                            
                        cky_dict[(i,j)].update(grammar_list)
                            
               
       
                      
            # Checking whether the sentence is in the grammar or not
            # To do so the start symbol needs to be in the last leftmost cell of the final CKY matrix
            if start_symbol in cky_dict[(len(test_sentence),0)]:
                
                print(f'{"Result: The sentence is IN the language of the CFG"}\n', file=file_output)
                
            else:
                
                print(f'{"Result: The sentence is NOT in the language of the CFG"}\n', file=file_output)
            
tag_end=timeit.default_timer()
print("Total time to execute the Recognizer: ",tag_end-tag_start)    
        
            
            
    
             
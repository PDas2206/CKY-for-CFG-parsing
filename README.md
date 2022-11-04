# CKY for CFG parsing
In this project we use the Cocke-Kasami-Younger (CKY) algorithm for bottom-up large-scale context-free grammar (CFG) parsing using Python and NLTK, applying it to the word and the parsing problem of English. The ingredients are: the grammar, the test sentences, and the parser; using NLTK only to represent grammars and trees. The grammar stems from a project dealing with implementing spoken language processing systems in the airline industry ( the Airline Travel Information System (ATIS)). The ATIS CFG is available in the NLTK data package, along with 98 test sentences.
## Recognizer
The CKY algorithm is implemented to be used a recognizer. When an input sentence is given the program decides whether the sentence is in the language of the CFG or not. The recognizer is tested on the ATIS test sentences (but also by feeding it other sentences to see whether it properly rejects ungrammatical sentences). 
## Parser
The CKY recognizer is then extended into a parser by adding backpointers. A function is implemented that extracts the set of all parse trees from the backpointers in the chart. 

## Getting Started:
	The program in this assignment have been done using Python 3. To run the files one has to have Python 3 or  above installed in their systems. Additionally you need the following packages to be installed: \
		nltk		To use its methods "CFG" and "grammar" \
		collections	To work with defaultdict \
		timeit		To record the time needed for the program to perform its various tasks \

	The statements required to import these are included in the programs, and so one does'nt have to explicitly write them while executing the program.

## Pre-requisite:
	You need to have a folder named "data" in which you need to have the grammar file "atis-grammar-cnf.cfg", the file containing the test sentences "atis-test-sentences.txt" and the file containing some more ungrammatical sentences "test-sentences-ungrammatical.txt".
	

## Running the program:
	To execute the programs from the command shell, do the following steps: \
		1. Change the directory to this folder (named "data") in your system. \
		2. To execute the program and generate the .tt file containing the words of the test corpus along with their respective tags, type the following after the prompt appears: \
			python <filename>.py \
			where <filename> is either cky or cky_ungrammatical. \
			*cky.py* will generate the file named "recognizer_output.txt" that has the test sentences along with a statement stating whether they are or not in the grammar. Along with that it would also display the time taken to recognize all the sentences. Same goes for *cky_ungrammatical.py* which produces the output file "recognizer_ungrammatical_output.txt".

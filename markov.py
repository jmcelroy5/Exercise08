#!/usr/bin/env python

import sys

def make_chains(corpus):
    """Takes an input text as a string and returns a dictionary of
    markov chains."""
    chains = {}

    read_text = corpus.read().replace("--"," ")       # store corpus in one long string
    word_list = read_text.split()

    #Loop through giant list and assign keys and values to empty dict
    for i in range(len(word_list)-2):
        key = (word_list[i], word_list[i+1])
        value = word_list[i+2]
        #add values to multiple occurances of pair word keys
        if key not in chains:       # If word pair is not already in dictionary
            chains[key] = [value]
        else:                       # If word pair is in dictionary (append to value list)
            chains[key].append(value)
            
    return chains

def make_text(chains):

    """Takes a dictionary of markov chains and returns random text
    based off an original text."""
    return "Here's some random text."

def main():
    args = sys.argv

    script, input_file = args

    # Change this to read input_text from a file
    input_text = open(input_file)

    chain_dict = make_chains(input_text)
    random_text = make_text(chain_dict)
    print random_text

if __name__ == "__main__":
    main()
#!/usr/bin/env python

import sys
import random
import string

def make_chains(corpus):
    """Takes an input text as a string and returns a dictionary of
    markov chains."""
    chains = {}

    input_text = corpus.read()
    clean_text = input_text.replace("--"," ").replace("_"," ")      # store corpus in one long string
    word_list = clean_text.split()

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

    keys_list = chains.keys()

    # While loop tests random keys until a value with capital letter is found
    not_found = True    
    while not_found:
        option = random.choice(keys_list)       # randomly selects a key from dictionary (key is a tuple)
        if chains[option][0][0] in string.ascii_uppercase:
            seed_key = option
            new_word = chains[seed_key]
            not_found = False
    
    sentence = ""

    while "." not in new_word:
        second_word = seed_key[1] # saving second word of key to form next tuple

        # Get new word (value of key)
        new_word = chains[seed_key] # values list
        # chooses value from value list if there is more than one option
        new_word = new_word[random.randrange(len(new_word))] 
        
        sentence = sentence + " " + new_word 
        
        seed_key = (second_word, new_word)

    return sentence

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
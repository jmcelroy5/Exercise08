#!/usr/bin/env python

import sys
import random
import string

def make_chains(corpus1,corpus2):
    """Takes an input text as a string and returns a dictionary of
    markov chains."""
    chains = {}

    input_text1 = corpus1.read() # one long string
    input_text2 = corpus2.read() # another long string

    mashup = input_text1 + input_text2

    clean_text = mashup.replace("--"," ").replace("_"," ")      # store corpus in one long string
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

    #assign key_list to key/tuple pair
    keys_list = chains.keys()

    # While loop tests random keys until a value with capital letter is found
    not_found = True    
    while not_found:
        option = random.choice(keys_list)       # randomly selects a key from dictionary (key is a tuple)
        if chains[option][0][0] in string.ascii_uppercase:
            seed_key = option
            new_word = chains[seed_key] #value
            not_found = False
    
    sentence = ""

    while new_word[-1] not in ".?!":

        # Get new word (value of key)
        new_word = chains[seed_key] # values list
        # chooses value from value list if there is more than one option
        new_word = new_word[random.randrange(len(new_word))] 
        
        #update sentence string
        sentence = sentence + " " + new_word

        second_word = seed_key[1] # saving second word of key to form next tuple 
        #update seed_key
        seed_key = (second_word, new_word)

    return sentence

def main():
    args = sys.argv

    script, input_file1, input_file2 = args

    # Change this to read input_text from a file
    corpus1 = open(input_file1)
    corpus2 = open(input_file2)

    chain_dict = make_chains(corpus1,corpus2)
    random_text = make_text(chain_dict)
    print random_text

if __name__ == "__main__":
    main()
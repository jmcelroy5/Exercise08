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
    for i in range(20):

        value_list = chains.values()
        rand_num = random.randrange(len(value_list)) # Generate a random number within the length of dictionary
        if value_list[rand_num][0][0] in string.ascii_uppercase: # If the first letter of the first word is a capital letter
            print value_list[rand_num][0]

        # first_word =       # randomly select a word pair that begins with capital letter
        # for key, value
        #     print value

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
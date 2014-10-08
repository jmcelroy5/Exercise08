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

    # Generates first word of sentence by finding a value with capital letter
    # value_list = chains.values()
    # def get_first_letter(x):
    #     if x[0][0] in string.ascii_uppercase:
    #         return True
    #     else:
    #         return False
    # capital_words_list = filter(get_first_letter, value_list)    # create value list for words that begin with capital letters

    # for i in range(20):
    #     rand_num = random.randrange(len(capital_words_list)) # Generate a random number within the length of capital word list
    #     first_word = capital_words_list[rand_num][0]

        # print first_word + chains[first_word][0]

    keys_list = chains.keys()
    print "keys list: ", keys_list
    
    # for key, value in chains.iteritems():
    seed_key = keys_list[2] #tuple with 2 strings

    first_word = seed_key[0] #string
    second_word = seed_key[1] #string
    third_word = chains[seed_key][0] #string

    next_word = chains.get((second_word,third_word),"Damn")

    sentence = first_word + " " + second_word + " " + third_word + " " + next_word[0]

    print sentence

    # return "Here's some random text."

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


import os, sys
import random
import string
import twitter

def make_chains(corpus1, corpus2, n):
    """Takes two input text files and returns a dictionary of
    markov chains."""

    chains = {}
    n = int(n)

    # Read in the two source files
    input_text1 = corpus1.read() 
    input_text2 = corpus2.read() 

    # Combining two source texts
    mashup = input_text1 + input_text2 

    clean_text = mashup.replace("--"," ").replace("_"," ").replace("[", " ").replace("]"," ").replace("/", " ").replace("\\", " ")

    word_list = clean_text.split() 

    # Loop through word list and create groupings (of n-length) 
    for i in range(len(word_list)-n):
        key_tuple = []
        for j in range(n):
            key_tuple.append(word_list[i+j])

        # Assign key and value to dictionary of markov chains
        key = tuple(key_tuple)
        value = word_list[i+n]
        
        if key not in chains:       
            chains[key] = [value]
        else:                       
            chains[key].append(value)

    return chains

def make_text(chains):
    """Takes a dictionary of markov chains and returns random text
    based off an original text."""

    keys_list = chains.keys()   # List of keys, tuples of n-length
          
    not_found = True    # Test random keys until a value with capital letter is found  
    while not_found:
        option = random.choice(keys_list)   # Randomly selects a key from dictionary 
       
        if chains[option][0][0] in string.ascii_uppercase:  # Chooses key if value is uppercase
            seed_key = option   
            new_word = chains[seed_key] 
            not_found = False
    
    sentence = ""

    # Generate tweet-length text
    while len(sentence) <= 130:     

        # Get new word (value of key)
        new_word = chains[seed_key] 

        # Randomly choose value from value list if there is more than one option
        new_word = new_word[random.randrange(len(new_word))] 

        # Update generated sentence with current word
        sentence = sentence + " " + new_word

        # Stitch together new key using end of last key + current word
        new_key = []
        new_key = list(seed_key[1:])
        new_key.append(new_word)
        seed_key = tuple(new_key)

    return sentence + "."

def post_to_twitter(tweet):

    if os.getenviron.get("TWITTER_API_KEY", None) == None:
        print "You need twitter access keys in your shell environment to post to twitter."
        sys.exit()

    api = twitter.Api(consumer_key = os.environ.get("TWITTER_API_KEY"),
                       consumer_secret = os.environ.get("TWITTER_CONSUMER_KEY"),
                       access_token_key = os.environ.get("TWITTER_ACCESS_TOKEN_KEY"),
                       access_token_secret= os.environ.get("TWITTER_ACCESS_TOKEN_SECRET"))

    print tweet
    post = raw_input("Do you want to post this to twitter? -->  y/n ")

    if "y" in post:
        return api.PostUpdate(tweet)

def main():
    args = sys.argv
    script, input_file1, input_file2, n = args

    # Takes text from two source files
    corpus1 = open(input_file1)
    corpus2 = open(input_file2)

    chain_dict = make_chains(corpus1, corpus2, n)  
    random_text = make_text(chain_dict)
    post_to_twitter(random_text)

    
if __name__ == "__main__":
    main()
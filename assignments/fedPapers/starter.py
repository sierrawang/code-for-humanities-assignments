from itertools import count
import math

EPSILON = 0.000001

# Return how likely a document is for a given author
# given the counts of the words and the author's distribution
def calc_log_pr_doc_given_author(prob_map, counts):
    log_prob = math.log(1)
    for word_i, c_i in counts.items():
        p_i = get_word_prob(prob_map, word_i)
        log_prob += c_i * math.log(p_i)
    return log_prob

# If a word is in a probability dictionary, return its probability
# otherwise, return epsilon
def get_word_prob(word_prob_map, word):
    if word in word_prob_map:
        return word_prob_map[word]
    return EPSILON

# Count and return the number of words in the given file. 
def get_new_words(fileName):
    # TO DO: Implement this function!
    pass

# From a file name, count the number of times each word exists
# in that file. Return the result as a map (aka a dictionary)
def make_word_count_map(fileName):
    # TO DO: Implement this function!
    pass

# From a file name, approximate the probability of a word
# being generated from the same distribution as the file.
# Assume that each word is produced independently, regardless
# of order.
def make_word_prob_map(fileName):
    wordMap = make_word_count_map(fileName)
    numWords = get_new_words(fileName)
    probabilityMap = {}
    for word in wordMap:
        count = wordMap[word]
        p = float(count) / numWords
        probabilityMap[word] = p
    return probabilityMap

# Add a word to a count map. Makes sure not to crash if the
# word has not been seen before.
def add_word_to_count_map(wordMap, word):
    # TO DO: Implement this function!
    pass

# Standardizes and returns a word. 
# This means -
# 1. remove all non-letter characters
# 2. make it lowercase
def standardize(word):
    # TO DO: Implement this function!
    pass

def main():
    # Calculate all the ps and qs
    # Eg hamiltonWordProb['congress'] = 0.005
    # hamilton_word_prob['piech'] = 0.0
    # hamilton_word_prob['the'] = 0.001

    hamilton_word_prob = make_word_prob_map('hamilton.txt')
    madison_word_prob = make_word_prob_map('madison.txt')

    # Get the word count of the unknown document
    # Eg unknown_doc_count['congress'] = 5

    # delete this line:
    # unknown_doc_count, n_words = make_word_count_map('unknown.txt') # FIX THIS!!!

    # new version:
    unknown_doc_count = make_word_count_map('unknown.txt')
    n_words = get_new_words('unknown.txt')

    print("hamilton['congress']\t", hamilton_word_prob['congress'])
    print("madison['congress']\t",  madison_word_prob['congress'])
    print("doc_count['congress']\t", unknown_doc_count['congress'])
    print("n_words", n_words)

    hamilton_term = calc_log_pr_doc_given_author(hamilton_word_prob, unknown_doc_count)
    madison_term = calc_log_pr_doc_given_author(madison_word_prob, unknown_doc_count)
    
    print("log P(D|H)\t", hamilton_term)
    print("log P(D|M)\t",madison_term)

    print('diff\t', hamilton_term - madison_term)

if __name__ == '__main__':
    main()
import csv
from itertools import count
import operator
import math

EPSILON = 0.000001

def main():
    # Calculate all the ps and qs
    # Eg hamiltonWordProb['congress'] = 0.005
    # hamilton_word_prob['piech'] = 0.0
    # hamilton_word_prob['the'] = 0.001

    hamilton_word_prob = make_word_prob_map('hamilton.txt')
    madison_word_prob = make_word_prob_map('madison.txt')

    

    # Get the word count of the unknown document
    # Eg unknown_doc_count['congress'] = 5
    unknown_doc_count, n_words = make_word_count_map('unknown.txt')

    print("hamilton['congress']\t", hamilton_word_prob['congress'])
    print("madison['congress']\t",  madison_word_prob['congress'])
    print("doc_count['congress']\t", unknown_doc_count['congress'])
    print("n_words", n_words)

    hamilton_term = calc_term_doc_given_author(hamilton_word_prob, unknown_doc_count)
    print('---'*10)
    madison_term = calc_term_doc_given_author(madison_word_prob, unknown_doc_count)
    print("Hamilton Term\t", hamilton_term)
    print("Madison Term\t",madison_term)

def calc_term_doc_given_author(prob_map, counts):
    """
    How likely is the document, given the counts of words in the doc
    and the authors prob_map
    """
    prob = 1
    for word, c_i in counts.items():
        p_word = get_word_prob(prob_map, word)
        prob *= p_word ** c_i
        print(word, c_i, prob)
    return prob
    # prob = 0
    # for word, c_i in counts.items():
    #     p_word = get_word_prob(prob_map, word)
    #     prob += math.log(p_word) * c_i
    # return prob


# If a word is in a probability dictionary, return its probability
# otherwise, return epsilon
def get_word_prob(word_prob_map, word):
    if word in word_prob_map:
        return word_prob_map[word]
    return EPSILON

# From a file name, approximate the probability of a word
# being generated from the same distribution as the file.
# Assume that each word is produced independently, regardless
# of order.
def make_word_prob_map(fileName):
    wordMap, nWords = make_word_count_map(fileName)
    probabilityMap = {}
    for word in wordMap:
        count = wordMap[word]
        p = float(count) / nWords
        probabilityMap[word] = p
    return probabilityMap

# From a file name, count the number of times each word exists
# in that file. Return the result as a map (aka a dictionary)
def make_word_count_map(fileName):
    wordMap = {}
    nWords = 0
    with open(fileName) as f:
        for line in f:
            words = line.split(' ')
            for word in words:
                word = standardize(word)
                add_word_to_count_map(wordMap, word)
                nWords+= 1
    return wordMap, nWords

# Add a word to a count map. Makes sure not to crash if the
# word has not been seen before.
def add_word_to_count_map(wordMap, word):
    if is_stop(word):
        return
    if not word in wordMap:
        wordMap[word] = 0
    wordMap[word] += 1

# Standardizes a word. For now, we are just going to make it
# lower case.
def standardize(word):
    standard = word.lower().strip()
    # remove punctuation
    standard = ''.join([i for i in standard if i.isalpha()])
    return standard

def is_stop(word):
    stop_words = ['to', 'i', 'the', 'and', 'of']
    return word in stop_words

if __name__ == '__main__':
    main()
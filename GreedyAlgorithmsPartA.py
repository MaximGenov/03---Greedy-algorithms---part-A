#We are interested in transmitting the encodings of B, E, K, P, and R (for the word BEEKEEPER)
#Transmission Time:
#1: 0.3 ms
#0: 0.1 ms
BEEKEEPER = "BEEKEEPER"
#Binary values of those letters:
#E is most used (5 times)
E = "0" #0.1 ms * 5 = 0.5 ms (shortest transmission time for a word most used)
B = "00" #0.2 ms
K = "000" #0.3 ms
P = "1" #0.3 ms
R = "10"  #0.4 ms (01 would need a prefix o ==> 0o1 as part of Python's syntax)
space = " "

#Encoding function that takes a string and outputs its binary encoded value
#A space is used as a seperator
def word_transmission(word):
    word_code = ""
    #word is bound to be a string, thus we may iterate through it to assess its components
    for i in range(len(word)):
        if i != 0:
            word_code += space
        if word[i] == 'B':
            word_code += B
        elif word[i] == 'E':
            word_code += E
        elif word[i] == 'K':
            word_code += K
        elif word[i] == 'P':
            word_code += P
        elif word[i] == 'R':
            word_code += R
    print(word_code)
    return word_code
word_transmission(BEEKEEPER)
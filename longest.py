words=input("enter message here:")
word_list=words.split()
def find_longest_word(word_list):
    longest_word = ''
    for word in word_list:
        if len(word) > len(longest_word):
            longest_word = word
    print(longest_word)
find_longest_word(word_list)
import cs50

#main function
def main():
    #Taking input from user and initializing count words ,count sentences and count letters variable
    text = cs50.get_string("Text: ")
    count_letters = 0
    count_words = 1
    count_sentence = 0
    #calculating the number of letters
    for i in text:
        #if any alphabet is found
        if (i.isalpha()):
            #count_letters variable is incremented
            count_letters += 1
    print(count_letters)
    #calculating words
    for j in text:
        #if any space character is found
        if (j == " "):
            #count word is incremented
            count_words += 1
    print(count_words)
    #counting sentences
    for k in text:
        #if (. ! ?) these character are found in string count sentences is incremented
        if (k == "." or k == "!" or k == "?"):
            count_sentence += 1
    print(count_sentence)
    #calculating index through formula
    L = (count_letters/count_words)*100
    S = (count_sentence/count_words)*100
    M = 0.0588*L
    N = 0.296*S
    index = round(M-N-15.8)
    #printing Grade levels
    if (index >= 1 and index <= 16):
        print("Grade " + str(index))
    if (index < 1):
        print("Before Grade 1")
    if (index > 16):
        print("Grade 16+")


main()

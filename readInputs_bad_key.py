'''
1. 0.25s for conscecutive taps on the same number
2. 0.5s to register the current letter so that another letter in the same number can be tapped
3. 0.25s to move between letters. Ex: from d (tap 3) to g (tap 4)
4. 2s for functionality like uppercase or special functionality like voicemail
'''
#Prepare Dict
all_letters = ['abc','def','ghi','jkl','mno','pqrs','tuv','wxyz']
keypad = {}
#Dict contains the key and no. of key presses required for each letter
for i in range(len(all_letters)):
    for j in range(len(all_letters[i])):
        keypad[all_letters[i][j]] = (i+2, j) # Key: Letter | Value: (key_to_hit, no_of_presses)
#print(keypad)

#Read text file and remove the newline characters
f = open("./test_txt/example_part2.txt", "rt")
words = f.readlines()
len_words = len(words)
for i in range(len_words):
    if words[i][-1] == '\n':
        words[i] = words[i][:-1]
#print(words)

broken_key = int(words[0]) #First line is the broken key
words = words[1:] #The remaining lines are words
for i in range(len(all_letters[broken_key-2])): #Loops through letters on broken key
    if i<2:
        keypad[all_letters[broken_key-2][i]] = ('*', (i % 2) + 1) #Adds first 2 chars to the second and third depth of *
    else:
        keypad[all_letters[broken_key-2][i]] = ('#', (i % 2) + 1) #Adds first 2 chars to the second and third depth of #
#print(keypad)

#Compute time for each word in the text file.
time_taken = []
best_words = [] #List of fastest words
fastest_time = None #Fastest time
for word in words:
    word_time = 0
    prev_key = -1
    for i in word:
        is_upper = i.isupper()
        i = i.lower()
        key, key_depth = keypad[i]

        #Start timer
        t = 0
        if prev_key == -1: #Rule 1
            pass
        elif prev_key == key: #Rule 4
            t = t + 0.5
        else:
            t = t + 0.25 #Rule 2
        
        t = t + (0.25*key_depth) #Rule 3

        if is_upper: #Rule 5
            t = t + 2
        
        word_time = word_time + t
        prev_key = key #Memorize previous key for Rule 1, 2, and 4

    if fastest_time == None:
        best_words = [word]
        fastest_time = word_time
    elif fastest_time > word_time:
        best_words = [word]
        fastest_time = word_time
    elif fastest_time == word_time:
        best_words.append(word)

    time_taken.append(word_time)
    word_time = 0 # Clear word time for next word
    prev_key = -1 # Clear previous key for next word

for i in range(len(words)):
    print('{} takes {} seconds'.format(words[i], time_taken[i]))

print('------------------------------------------')
print('The fastest word(s) are {} . They take {} seconds'.format(best_words, fastest_time))
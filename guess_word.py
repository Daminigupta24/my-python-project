import random

words_list=["allen","bob","cat","gues"]
words=random.choice(words_list)
print(words)
#create a placeholder with same number of blanks
# placeholder=""
# for i in range(0,len(words)):
#     placeholder+= "_"

# guess=input("ask the user to guess a letter").lower()
# display=""
# for letter in words:
#     if letter==guess:
#         display+=letter
#     else:
#         display+="_"
# print(placeholder,display)
game_over=False
guess_word_list=[]
p_len=len(set(words))
while not game_over and p_len>0:
    guess=input("ask the user to guess a letter").lower()
    display=""
    for letter in words:
        if letter==guess:
            display+=letter
            guess_word_list.append(guess)
        elif letter in guess_word_list:
            display+=letter
        else:
            display+="_"
            #print("the letter does not exist in the chosen word")
    p_len=p_len-1
    print(f'you have {p_len} no of lives left')
    print(display)
    if p_len==0:
        print(f'the correct word is {words}')
        print("sorry, you have no more lives left, lets meet at next game")
    if "_" not in display:
        game_over=True
        print("you win")
        
            


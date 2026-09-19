import random
import requests

print("---------------------------------------")
print("Welcome To Hangman (The guessing game)")
print("Game made by Pratik ")
print("---------------------------------------")

hangman_stages = [
    """
       ------
       |    |
       |
       |
       |
       |
    ---------
    """,
    """
       ------
       |    |
       |    O
       |
       |
       |
    ---------
    """,
    """
       ------
       |    |
       |    O
       |    |
       |
       |
    ---------
    """,
    """
       ------
       |    |
       |    O
       |   /|
       |
       |
    ---------
    """,
    """
       ------
       |    |
       |    O
       |   /|\\
       |
       |
    ---------
    """,
    """
       ------
       |    |
       |    O
       |   /|\\
       |   /
       |
    ---------
    """,
    """
       ------
       |    |
       |    O
       |   /|\\
       |   / \\
       |
    ---------
    """
    
]

def check(input_word,random_words,display):
    found = False
    for i in range(len(random_words)):
        if  random_words[i] == input_word:
            display[i] = input_word
            found = True
    return found
        
api_url = 'https://api.api-ninjas.com/v2/randomword'
response = requests.get(api_url, headers={'X-Api-Key': 'GmFyGMPTVA0yX7xqfjBonH0Y4Vho1bSF8DXnhsDW'})


if response.status_code == requests.codes.ok:
    data = response.json()
    lenght = len(data[0])
    display = [" _ "] * lenght

life = 7
guessed_li = []

while True:
    print("".join(display))
    input_word = (input(f"Guess the letter:(q to quit) \n Your guessed letter :{guessed_li} ")).strip().lower()
    if not input_word.isalpha():
        print("You should enter letter")
    elif len(input_word) != 1:
        print("Enter only one letter")
    elif input_word == "q":
        break
    
    else:
        guessed_li.append(input_word)
        correct = check(input_word,data[0],display)
        if correct :
            print("Correct 🎉🎉")
            if  " _ " not in display:
                print("-------------")
                print("Congratulation you won $3000000000 🫡🫡  😂😂😂")
                print(f"The word is: {data[0]}")
                break
                
        else:
            life -= 1
            if life==6:
                print(hangman_stages[0])
            elif life == 5:
                print(hangman_stages[1])
            elif life==4:
                print(hangman_stages[2])
            elif life == 3:
                print(hangman_stages[3])
            elif life == 2:
                print(hangman_stages[4])
            elif life==1:
                print(hangman_stages[5])
            elif life == 0:
                print(hangman_stages[6])
                print("Try next time 😂😂😂😂")
                print("----------------------")
                print(f"The word is : {data[0]}") 
                break
             

    
    

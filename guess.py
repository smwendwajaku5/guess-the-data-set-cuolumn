import random 
columns = ["customerid","orderdate","totalamount","systemstatus"]

word = random.choice(columns)
guessed = set()
attempts = 8

while attempts >0:
    display ="".join(c if c in guessed else "_" for c in word)
    print(f"word :{display}   Attempts left: {attempts}" )
    guess = input("Guess a letter: ").lower()

    if guess in guessed:
        print("You already guessed that letter.")
        continue
    guessed.add(guess)
    if guess not in word:
        attempts -= 1
        print("Not in the word.")
    if all(c in guessed for c in word):
        print(f"\n You Win!!! The word was '{word}")

else:
    print(f"\nOut of attempts! The word was '{word}'")
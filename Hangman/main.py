import json
from random import choice

# ვხსნით ფაილს და ვკითხულობთ მის შიგთავსს. 
try:
    with open("IT_STEP_Midterm/Hangman/data.json", mode="r", encoding="utf-8") as file:
        data = json.load(file)
except FileNotFoundError: # error-ის დაამუშავება
    raise FileNotFoundError("Error: File not found.")

# ფუნქცია, რომელიც მომხმარებელს სთხოვს თამაშის სირთულის არჩევას. იმის მიხედვით თუ რა სირთულეს აირჩევს მომხმარებელი, აბრუნებს ცდების რაოდენობას
def choose_game_mode():
    while True: # invalid input handling-სთვის ვიყენებთ while True ლუპს
        print("\nGame modes:", "Easy(10 attempts)", "Normal(6 attempts)", "Hard(3 attempts)", sep="\n")
        game_mode = input("Select a game mode or enter 'q' to quit: ").lower().strip() # lower() იმ შემთხვევისთვის თუ მომხმარებელი შემოიტანს დიდ 'Q' ასოს. strip() აშორებს ზედმეტ სფეისებს
        if game_mode == 'q': # თუ მომხმარებელი შემოიტანს დიდ ან პატარა 'q' ასოს ფუნქცია აბრუნებს None-ს.
            return
        elif game_mode == 'easy':
            return 10
        elif game_mode == 'normal':
            return 6
        elif game_mode == 'hard':
            return 3
        else: # თუ მომხმარებელი [easy, normal, hard] გარდა სხვა რამეს შემოიტანს იბეჭდება შესაბამისი error შეტყობინება.
            print("Error: Invalid operation selected, please choose from [Easy, Normal, Hard].")

# ფუნქცია, რომელიც მომხმარებელს სთხოვს კატეგორიის არჩევას. იმის მიხედვით თუ რომელ კატეგორიას აირჩევს მომხმარებელი, პროგრამა ამოარჩევს შემთხვევით სიტყვას ამ კატეგორიიდან.
def choose_category():
    while True: # invalid input handling-სთვის ვიყენებთ while True ლუპს
        print("1. Movies", "2. Books", "3. Celebrities", "4. Historical figures", "5. Countries", "6. Animals", sep="\n")
        category = input("Select a category or enter 'q' to quit: ").strip() # strip() აშორებს ზედმეტ სფეისებს
        if category.lower() == 'q': # თუ მომხმარებელი შემოიტანს დიდ ან პატარა 'q' ასოს ფუნქცია აბრუნებს None-ს. 
            return
        if category not in ['1', '2', '3', '4', '5', '6']: # თუ მომხმარებელი 1-6 ციფრების გარდა სხვა რამეს შემოიტანს იბეჭდება შესაბამისი error შეტყობინება.
            print("Error: Invalid operation selected, please choose from [1, 2, 3, 4, 5, 6].")
            continue # ვიწყებთ ციკლს თავიდან.
            
        # რომელ კატეგორიასაც აირჩევს მომხმარებელი იმ კატეგორიის სიტყვას აარჩევს პროგრამა შემთხვევითობის პრინციპით.
        if category == '1':
            words = data["movies"]
        elif category == '2':
            words = data["books"]  
        elif category == '3':
            words = data["celebrities"]
        elif category == '4':
            words = data["historical_figures"]   
        elif category == '5':
            words = data["countries"]
        elif category == '6':
            words = data["animals"]
        
        # ფუნქცია დააბრუნებს პროგრამის მიერ შემთხვევითობის პრინციპით არჩეულ სიტყვას.
        return choice(words)

# მთავარი ფუნქცია.
def play(attempts, random_word): # არგუმენტად გადავცემთ ცდების რაოდენობასა და პროგრამის მიერ არჩეულ სიტყვას.
    guessed_letters = set() # ვქმნით სეტს უკვე გამოცნობილი სიმბოლოების შესანახად. სეტს ვიყენებთ იმიტომ, რომ სეტი არ ინახავს დუბლიკატებს.
    hidden_word = [] # ვქმნით ლისტს რათა იმდენი "_" სიმბოლო შევინახოთ რამდენი ასო და რიცხვიცაა ამორჩეულ სიტყვაში. 
    for i in random_word: # სიტყვაში არსებული თითოეული ასოსა და რიცხვის ნაცვლად ლისტში ვინახავთ "_" სიმბოლოს, ხოლო სხვა ნებისმიერ სიმბოლოს ვინახავთ უცვლელად.
        if i.isalnum(): # ამოწმებს არის თუ არა ასო ან რიცხვი.
            hidden_word.append("_")
        else:
            hidden_word.append(i)
    print(" ".join(hidden_word)) # საბოლოოდ join()-ის საშუალებით ლისტის ელემენტებს ვაერთებთ და ვბეჭდავთ.
        
    guess_count = 0 # ცვლადი იმის დასათვლელად თუ რამდენ ცდაში გამოიცნო მომხმარებელმა სიტყვა.
    while attempts > 0: # ვიყენებთ while ციკლს რათა მომხმარებელს მანამ ვთხოვოთ სიმბოლოს შემოტანა სანამ ცდები არ ამოეწურება.
        guess = input("Guess a character: ").lower().strip() # lower()-ის საშუალებით შემოტანილი სიმბოლო თუ სიტყვა გადადის პატარა რეგისტრში. strip() აშორებს ზედმეტ სფეისებს.
        # თუ მომხმარებლის მიერ შემოტანილ სიტყვაში და პროგრამის მიერ ამორჩეულ სიტყვაში იქნება სიმბოლოები [" ", ",", ".", "-", "'"] მაშინ მათ replace()-ის გამოყენებით ვშლით(ვანაცვლებთ).
        # ამას ვაკეთებთ იმიტომ, რომ თუ ამორჩეული სიტყვა არის "Star Wars" და მომხმარებელი შემოიტანს "StarWars" პროგრამამ ეს უნდა ჩათვალოს სწორ პასუხად.  
        changed_word = random_word.lower() 
        for i in [" ", ",", ".", "-", "'"]:
            guess = guess.replace(i , "")
            changed_word = changed_word.replace(i, "")

        if len(guess) == 1: # იმ შემთხვევაში თუ მომხმარებელი შემოიტანს მხოლოდ ერთ სიმბოლოს.
            if not guess.isalnum(): # თუ ეს ერთი შემოტანილი სიმბოლო არ არის ასო ან რიცხვი, ვბეჭდავთ შესაბამის შეტყობინებას.
                print("Error: Please enter an alphanumeric character.")
                continue # ვიწყებთ ციკლს თავიდან.
                
            if guess in guessed_letters: # თუ ისეთ ასოს ან რიცხვს შემოიტანს, რომელიც უკვე შემოიტანა, ვბეჭდავთ შესაბამის შეტყობინებას.
                print("Error: You have already guessed that letter. Try another.")
                continue # ვიწყებთ ციკლს თავიდან.

            guessed_letters.add(guess) # შემოტანილ ასოსა თუ რიცხვს ვამატებთ გამოცნობილი ასოების სეტში.
            guess_count += 1 # მნიშნელობას ვზრდით ერთით(მნიშვნელობა არ იზრდება ერთი და იმავე სიმბოლოს ორჯერ შემოტანისას).

            if guess in random_word.lower(): # თუ მომხმარებელი შემოიტანს ისეთ სიმბოლოს, რომელიც არის პროგრამის მიერ ამორჩეულ სიტყვაში.
                print("***Correct guess!***")  # იბეჭდება შესაბამისი შეტყობინება.
                for i in range(len(random_word)): # გავირბენთ მთლიან ლისტს(რომელიც ეკრანზეა დაბეჭდილი "_" სიმბოლოებით).
                    if guess == random_word[i].lower(): # სადაც შეგვხვდება მომხმარებლის მიერ შემოტანილი ასო ან რიცხვი, ლისტში "_" სიმბოლოს ვანაცვლებთ ამ ასოთი თუ რიცხვით.  
                        hidden_word[i] = random_word[i]
            else: # თუ მომხმარებლის მიერ შემოტანილი სიმბოლო არ არის სიტყვაში, იბეჭდება შესაბამისი შეტყობინება.
                print("***Wrong guess!***")
                attempts -= 1 # ცდების რაოდენობას ვამცირებთ ერთით(ცდების რაოდენობა არ მცირდება თუ მომხმარებელი სწორად გამოიცნობს სიმბოლოს).
        elif len(guess) == len(changed_word): # თუ მომხმარებლის მიერ შემოტანილი და პროგრამის მიერ არჩეული სიტყვების ზომა ტოლია.
            guess_count += 1 # მნიშნველობას ვზრდით ერთით.
            if guess == changed_word: # თუ მომხმარებლის მიერ შემოტანილი და პროგრამის მიერ არჩეული სიტყვები ერთი და იგივეა
                for i in random_word: # ვბეჭდავთ გამოცნობილ სიტყვას.
                    print(i, end=' ')
                print(f"\n***Congratulations! You've guessed the word correctly in {guess_count} attempts!***") # ვბეჭდავთ თუ რამდენ ცდაში გამოიცნო მომხმარებელმა სიტყვა.
                break # გამოვდივართ while ლუპიდან
            else:
                print("***Wrong guess!***") # თუ მომხმარებლის მიერ შემოტანილი და პროგრამის მიერ არჩეული სიტყვები არ არის ერთი და იგივე
                attempts -= 1 # ცდების რაოდენობას ვამცირებთ ერთით.
        else: # თუ მოხმარებელი შემოიტანს ერთ სიმბოლოზე მეტს და ამ სიტყვის სიგრძე არ არის პროგრამის მიერ არჩეული სიტყვის სიგრძის ტოლი, ვბეჭდავთ შესაბამის შეტყობინებას.
            print("Error: Enter one alphanumeric character or whole word same size as hidden word!")
            continue # ვიწყებთ ციკლს თავიდან.

        if "_" not in hidden_word: # თუ მომხმარებლის მიერ სიმბოლოების შემოტანის შედეგად აღმოჩნდება, რომ ლისტში აღარ არის "_" სიმბოლო(ანუ სიტყვაში ყველა სიმბოლო გამოიცნო).
            print(" ".join(hidden_word)) # ვბეჭდავთ თავად სიტყვას.
            print(f"***Congratulations! You've guessed the word correctly in {guess_count} attempts!***") # ვბეჭდავთ თუ რამდენ ცდაში გამოიცნო მომხმარებელმა სიტყვა.
            break # გამოვდივართ while ლუპიდან.
            
        if attempts == 0: # თუ მომხმარებელს ამოეწურება ცდების რაოდენობა.
            print(f"Game over! The word was: {random_word}", '\n') # ვბეჭდავთ შესაბამის შეტყობინებას და გამოსაცნობ სიტყვას.
        else:
            print(" ".join(hidden_word)) # სხვა შემთხვევაში ვბეჭდავთ სიტყვას და დარჩენილი ცდების რაოდენობას.
            print(f"Attempts left: {attempts}")
        
# ფუნქცია, რომელიც მომხმარებელს ეკითხება სურს თუ არა ახლიდან თამაში.
def play_again():
    while True: # invalid input handling-სთვის ვიყენებთ while True ლუპს
        answer = input("Do you want to play again? (y/n): ").lower().strip() 
        if answer == 'y':
            return True
        elif answer == 'n':
            return False
        else:
            print("Error: Invalid input.")

# მისალმების მესიჯი დეკორაციისთვის
print("*" * 35) 
print("  Welcome to Hangman Console App!")
print("*" * 35)

while True:
    attempts = choose_game_mode() # ფუნქციის გამოძახება.
    if attempts is None: # თუ დააბრუნა None, ანუ მომხმარებელმა შემოიტანა 'q' ასო, შესაბამისად პროგრამიდან უნდა გამოვიდეთ.
        break

    random_word = choose_category() # ფუნქციის გამოძახება.
    if random_word is None: # თუ დააბრუნა None, ანუ მომხმარებელმა შემოიტანა 'q' ასო, შესაბამისად პროგრამიდან უნდა გამოვიდეთ.
        break

    play(attempts, random_word) # ფუნქციის გამოძახება.
    
    if play_again(): # თუ ფუნქცია დააბრუნებთ True-ს ვაგრძელებთ თამაშს, თუ დააბრუნებს False-ს ვწყვეტთ თამაშს.
        continue
    else:
        break
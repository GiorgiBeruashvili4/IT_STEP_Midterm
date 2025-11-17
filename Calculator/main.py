"""
ფუნქცია, რომელიც უარყოფით რიცხვებს მოაქცევს ფრჩხილებში, დადებითს კი დატოვებს უცვლელად,
რადგან ორი არითმეტიკული ოპერაცია ერთად არ შეიძლება და უარყოფითი რიცხვი ფრჩხილებში უნდა მოვაქციოთ. 
(მაგალითად: 5 + (-3) = 2 და არა 5 + -3 = 2).
"""
def brackets(num):
    if num < 0:
        return f"({num})"
    return f"{num}"


# მისალმების მესიჯი დეკორაციისთვის
print("*" * 38) 
print("  Welcome to Calculator Console App!")
print("*" * 38)

"""
მთლიანი პროგრამა მოვაქციე while True ციკლში, რათა მომხმარებელს შეეძლოს 
ოპერაციების მრავალჯერ შესრულება და არ დასჭირდეს პროგრამის ხელახლა გაშვება.
"""
while True:
    operation = input("\nSelect an operation (+, -, *, /) or enter 'q' to quit: ") # მომხმარებელს ვთხოვთ, აირჩიოს ოპერაცია ან პროგრამიდან გამოსვლა.
    if operation.lower() == 'q': # operation.lower()-ს ვიყენებთ იმ შემთხვევაში თუ მომხმარებელი შემოიტანს დიდ 'Q'-ს.
        break # გამოვდივართ while True ციკლიდან 'q'-ს შემოტანის შემთხვევაში და სრულდება პროგრამა.
    if operation not in ['+', '-', '*', '/']:  # ვამოწმებთ, რომ მომხმარებელმა სწორი ოპერაცია აირჩია.
        print("Error: Invalid operation selected, please choose from +, -, *, /.") # თუ არასწორი ოპერაცია აირჩია ვბეჭდავთ შესაბამის შეტყობინებას.
        continue # ვიწყებთ ციკლს თავიდან.

    # ვიყენებთ try-except ბლოკს შეცდომებთან გასამკლავებლად.
    try:
        quantity = int(input("Enter amount of numbers you want to perform the operation on (Max: 10): ")) # მომხმარებელს ვთხოვთ, შეიყვანოს რიცხვების რაოდენობა.
        if quantity < 2: # ვამოწმებთ, რომ რიცხვების რაოდენობა არ იყოს 2-ზე ნაკლები, რადგან ოპერაციის შესრულებისთვის მინიმუმ 2 რიცხვია საჭირო.
            print("Error: You need to enter at least two numbers to perform the operation.") # ვბეჭდავთ შესაბამის Error შეტყობინებას.
            continue # ვიწყებთ ციკლს თავიდან.
        if quantity > 10: # ვამოწმებთ, რომ რიცხვების რაოდენობა არ აღემატებოდეს 10-ს(ეს არის ჩვენი პროგრამის შეზღუდვა).
            print("Error: Maximum amount of numbers is 10.") # ვბეჭდავთ შესაბამის Error შეტყობინებას.
            continue # ვიწყებთ ციკლს თავიდან.
    except ValueError: # თუ მომხმარებელმა რიცხვის ნაცვლად სხვა რამე შეიყვანა, ვიჭერთ ValueError-ს და ვბეჭდავთ შესაბამის შეტყობინებას.
        print("Error: Invalid input, please enter a valid integer.")
        continue # ვიწყებთ ციკლს თავიდან.

    numbers = [] # ცარიელი სია შემოტანილი რიცხვების შესანახად.
    for i in range(quantity): # range(quantity)-ს საშუალებით ვიმეორებთ რიცხვების შეყვანის პროცესს იმდენჯერ, რამდენჯერაც მომხმარებელს სურს.
        while True: # invalid input-ის თავიდან ასაცილებლად ვიყენებთ while True ციკლს.
            try: 
                number = input(f"Enter number {i + 1}: ") # მომხმარებელს ვთხოვთ, შეიყვანოს რიცხვი.
                if "." in number: # ვამოწმებთ, შეიცავს თუ არა შეყვანილი რიცხვი წერტილს, რათა გავიგოთ float ტიპისაა თუ int ტიპის.
                    number = float(number)
                else:
                    number = int(number) 
                numbers.append(number) # შეყვანილ რიცხვებს ვამატებთ სიაში.
                break # ვტოვებთ while True ციკლს და გადავდივართ შემდეგ რიცხვის შეყვანაზე.
            except ValueError: # თუ მომხმარებელმა რიცხვის ნაცვლად სხვა რამე შეიყვანა, ვიჭერთ ValueError-ს და ვბეჭდავთ შესაბამის შეტყობინებას.
                print("Error: Invalid input, please enter a valid number.")

    # ვასრულებთ შესაბამის ოპერაციას შემოტანილ რიცხვებზე.
    if operation == '+': 
        result = sum(numbers)  
    elif operation == '-': # result-ს ვანიჭებთ სიის პირველ ელემენტს და შემდეგ მას ვაკლებთ დანარჩენ რიცხვებს.
        result = numbers[0]
        for i in numbers[1:]: # ვიყენებთ ჭრას, რათა გამოვტოვოთ სიის პირველი ელემენტი.
            result -= i 
    elif operation == '*': # result-ს ვანიჭებთ 1-ს და შემდეგ მას ვამრავლებთ შემოტანილ რიცხვებზე.
        result = 1
        for i in numbers:
            result *= i 
    elif operation == '/':
        division_by_zero = False # division_by_zero ცვლადს ვიყენებთ იმისთვის, რომ გავიგოთ მოხდა თუ არა ნულზე გაყოფა.
        result = numbers[0]  # result-ს ვანიჭებთ სიის პირველ ელემენტს და შემდეგ მას ვყოფთ დანარჩენ რიცხვებზე.
        for i in numbers[1:]: # ვიყენებთ ჭრას, რათა გამოვტოვოთ სიის პირველი ელემენტი.
            if i == 0:  # ვამოწმებთ, მოხდა თუ არა ნულზე გაყოფა და თუ მოხდა, ვბეჭდავთ შესაბამის შეტყობინებას.
                print("Error: Division by zero is not allowed.")
                division_by_zero = True  # თუ ნულზე გაყოფა მოხდა, division_by_zero-ს ვანიჭებთ True-ს.
                break # გამოვდივართ for ციკლიდან.
            result /= i 
            if result % 1 == 0: # ვამოწმებთ, result ცვლადში მძიმის შემდეგ რა რიცხვ(ებ)ი წერია.
                result = int(result) # თუ მძიმის შემდეგ წერია მხოლოდ 0, ვაქცევთ მას int ტიპად.
        if division_by_zero: # თუ ნულზე გაყოფა მოხდა, ვიწყებთ ციკლს თავიდან.
            continue

    # ვბეჭდავთ ფიფქებს დეკორაციისთვის და შედეგს.
    print("*" * 15, "Result", "*" * 15) 
    print(numbers[0], operation, end=' ')  # ვბეჭდავთ სიის პირველ ელემენტს(უარყოფითი რომც იყოს ფრჩხილები არ სჭირდება).
    for i in numbers[1:-1]: # ვიყენებთ ჭრას, რათა გამოვტოვოთ სიის პირველი და ბოლო ელემენტი.
        print(brackets(i), operation, end=' ') 
    print(brackets(numbers[-1]), end=' ') # ვბეჭდავთ სიის ბოლო ელემენტს.
    print("=", round(result, 5)) # round()-ს ვიყენებთ, რათა შედეგი მძიმის შემდეგ 5 რიცხვამდე დავამრგვალოთ(ძირითადად, გამოგვადგება თუ მომხმარებელი გაყოფას შეასრულებს).
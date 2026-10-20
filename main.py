welcome = "Welcome to Football La Vida Trivia".upper()
print(welcome)

while True:
    first_name = input("Enter your first name: ")
    if first_name.isalpha():
        break
    print("Name must contain letters only, please try again")

while True:
    last_name = input("Enter your last name: ")
    if last_name.isalpha():
        break
    print("Name must contain letters only, please try again")

full_name = f"{last_name} {first_name}"

age_text = input("Enter your age: ")

if not age_text.isdigit():
    print("Please enter your age in numbers only")
    exit()

age = int(age_text)
if age <= 12:
    print("*oops you still a kid*")
    exit()

gender = input("pick your gender (male or female): ").lower()

if gender == "male":
    salutation = "Sir"
elif gender == "female":
    salutation = "Miss"
else:
    print("It seem like you are an alien")
    exit()

print(f"Welcome {salutation} {full_name}".title())

club = ["Chelsea", "Manchester City", "Barcelona", "Real Madrid", "Manchester United"]

while True:
    fav_club = input(
        "Pick your favourite team among Chelsea, Manchester City, "
        "Barcelona, Real Madrid, Manchester United: "
    ).title()
    if fav_club in club:
        break
    print("Spelling error, please try again")

question = {
    "Chelsea": [
        {
            "q": "Who was the coach when Chelsea won the Champions League in 2021?",
            "option": {"a": "Xabi Alonso", "b": "Thomas Tuchel", "c": "Graham Potter"},
            "answer": "b",
        },
        {
            "q": "Who is Chelsea's all-time top scorer?",
            "option": {"a": "Frank Lampard", "b": "Didier Drogba", "c": "Eden Hazard"},
            "answer": "a",
        },
        {
            "q": "What is the name of Chelsea's home stadium?",
            "option": {"a": "Anfield", "b": "Old Trafford", "c": "Stamford Bridge"},
            "answer": "c",
        },
    ],
    "Manchester City": [
        {
            "q": "Who was the manager when Manchester City won the treble in 2023?",
            "option": {"a": "Roberto Mancini", "b": "Pep Guardiola", "c": "Manuel Pellegrini"},
            "answer": "b",
        },
        {
            "q": "What is the name of Manchester City's home stadium?",
            "option": {"a": "Etihad Stadium", "b": "Old Trafford", "c": "Goodison Park"},
            "answer": "a",
        },
        {
            "q": "Who scored the last-minute goal that won City the 2011/12 league title?",
            "option": {"a": "Carlos Tevez", "b": "Sergio Aguero", "c": "David Silva"},
            "answer": "b",
        },
    ],
    "Barcelona": [
        {
            "q": "Who is Barcelona's all-time top scorer?",
            "option": {"a": "Luis Suarez", "b": "Lionel Messi", "c": "Xavi"},
            "answer": "b",
        },
        {
            "q": "What is the name of Barcelona's home stadium?",
            "option": {"a": "Santiago Bernabeu", "b": "Mestalla", "c": "Camp Nou"},
            "answer": "c",
        },
        {
            "q": "Who managed Barcelona when they won the 2006 Champions League?",
            "option": {"a": "Frank Rijkaard", "b": "Pep Guardiola", "c": "Ronald Koeman"},
            "answer": "a",
        },
    ],
    "Manchester United": [
        {
            "q": "What is the name of Manchester United's stadium?",
            "option": {"a": "Stamford Bridge", "b": "Old Trafford", "c": "Anfield"},
            "answer": "b",
        },
        {
            "q": "What is Manchester United's nickname?",
            "option": {"a": "London Cowboys", "b": "Citizens", "c": "Red Devils"},
            "answer": "c",
        },
        {
            "q": "Who is Manchester United's all-time top scorer?",
            "option": {"a": "Wayne Rooney", "b": "Ryan Giggs", "c": "Bruno Fernandes"},
            "answer": "a",
        },
    ],
    "Real Madrid": [
        {
            "q": "Who is Real Madrid's all-time top scorer?",
            "option": {"a": "Karim Benzema", "b": "Gareth Bale", "c": "Cristiano Ronaldo"},
            "answer": "c",
        },
        {
            "q": "What is the name of Real Madrid's stadium?",
            "option": {"a": "Camp Nou", "b": "Old Trafford", "c": "Santiago Bernabeu"},
            "answer": "c",
        },
        {
            "q": "Which player has made the most appearances for Real Madrid?",
            "option": {"a": "Raul", "b": "Karim Benzema", "c": "Cristiano Ronaldo"},
            "answer": "a",
        },
    ],
}

point = 0
for item in question[fav_club]:
    print(item["q"])
    for key, text in item["option"].items():
        print(f"{key}) {text}")
    if input("Answer: ").lower() == item["answer"]:
        print("Correct")
        point += 1
    else:
        print("Wrong")

print("Total Point:", point)

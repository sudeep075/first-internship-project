# Define the questions and options
questions=("how many elements are in a peroidic table?: ",
"which animal lays largest eggs?:",
"how many continents are there in the world?:",
"which planet is the brightest in the solar system ?:")

options=(("A.116","B.117","C.118","D.119"),
         ("A.Whale","B.Crocodile","C.Ostrich","D.Elephant"),
         ("A.8","B.6","C.7","D.9"),
         ("A.Mercury","B.Venus","C.Earth","D.Mars"))


answers=("C","C","C","B")
guesses=[]
score=0
question_num=0

for questions in questions:
  print("-----------------------")
  print(questions)
  for option in options[question_num]:
     print(option)


     guess=input("Enter(A,B,C,D):").upper()
     guesses.append(guess)
     if guess==answers[question_num]:
        score+=1
        print("CORRECT")
else:
   print("INCORRECT")
   print(f"{answers[question_num]}is the correct answer")
   question_num +=1
     
print("--------------")
print("         RESULTS      ")
print("-------------")     

print("answers:",end="")  
for answers in answers:
   print(answer,end=" ")
print()

print("answers:",end="")
for guess in guesses:
   print(guess,end="")
   print()

score=int(score/len(questions)*100)
print(f"your score is:{score}%")



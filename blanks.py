
wins = 0 
qstn1 = "1. Tell me if you _____ any help."
answer_choices = ["need", "will need", "would need"]

print(qstn1)
for choice in answer_choices:
    print(f"- {choice}")

userInp1 = input ("Answer is: ")
userInp1 = userInp1.lower().replace(" ", "")

if userInp1 == "need":
    wins +=1



qstn2 = "2. The first time I _____ him was at university."
answer_choices2 = ["met", "had met", "have met"]

print(qstn2)
for choice in answer_choices2:
    print(f"- {choice}")

userInp2 = input ("Answer is: ")
userInp2 = userInp2.lower().replace(" ", "")
if userInp2 == "met":
    wins +=1



qstn3 = "3. This is the garage _____ they used to work."
answer_choices3 = ["where", "which", "that"]

print(qstn3)
for choice in answer_choices3:
    print(f"- {choice}")

userInp3 = input ("Answer is: ")
userInp3 = userInp3.lower().replace(" ", "")
if userInp3 == "where":
    wins +=1



qstn4 = "4. I _____ a terrible experience yesterday."
answer_choices4 = ["have", "had", "have had"]

print(qstn4)
for choice in answer_choices4:
    print(f"- {choice}")

userInp4 = input ("Answer is: ")
userInp4 = userInp4.lower().replace(" ", "")
if userInp4 == "had":
    wins +=1



qstn5 = "5. That is my biggest regret _____."
answer_choices5 = ["yet", "still", "already"]

print(qstn5)
for choice in answer_choices5:
    print(f"- {choice}")

userInp5 = input ("Answer is: ")
userInp5 = userInp5.lower().replace(" ", "")
if userInp5 == "yet":
    wins +=1



qstn6 = "6. The valley _____ quiet and beautiful in the morning."
answer_choices6 = ["laid", "lays", "lay"]

print(qstn6)
for choice in answer_choices6:
    print(f"- {choice}")

userInp6 = input ("Answer is: ")
userInp6 = userInp6.lower().replace(" ", "")
if userInp6 == "lay":
    wins +=1



qstn7 = "7. Each of us _____ the world differently."
answer_choices7 = ["see", "sees", "seen"]

print(qstn7)
for choice in answer_choices7:
    print(f"- {choice}")

userInp7 = input ("Answer is: ")
userInp7 = userInp7.lower().replace(" ", "")
if userInp7 == "sees":
    wins +=1



qstn8 = "8. _____ his illness, he could not write the exam."
answer_choices8 = ["Owing", "Due to", "Either"]

print(qstn8)
for choice in answer_choices8:
    print(f"- {choice}")

userInp8 = input ("Answer is: ")
userInp8 = userInp8.lower().replace(" ", "")
if userInp8 == "Due to":
    wins +=1



qstn9 = "9. The summer term _____ on April 12th."
answer_choices9 = ["will start", "start", "starts"]

print(qstn9)
for choice in answer_choices9:
    print(f"- {choice}")

userInp9 = input ("Answer is: ")
userInp9 = userInp9.lower().replace(" ", "")
if userInp9 == "starts":
    wins +=1



qstn10 = "10. I will pay you back when I _____ a job."
answer_choices10 = ["get", "will get", "would get"]

print(qstn10)
for choice in answer_choices10:
    print(f"- {choice}")

userInp10 = input ("Answer is: ")
userInp10 = userInp10.lower().replace(" ", "")
if userInp10 == "get":
    wins +=1
    
    

print("Score: ", wins)



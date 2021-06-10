


soccer = 0
basketball = 0
baseball = 0
football = 0
hockey = 0
bowling = 0
curling = 0

soc = "You are soccer! You like to be active and tend to be one of the more educated people in the room. Sometimes you may be a bit condescending though. Work on that."
bask = "You are basketball. You aren't really appreciated by people as much as you should be. You're a classic but sometimes people forget about you. You're probably pretty tall too."
base = "You are baseball. A classic American sport. You might not be as active as some other people but you can move pretty fast when you need to."
foot = "You are football. You're pretty popular and even people who don't know you at all tend to have heard of you. People who like you really like you but the people who don't like you will make sure and let everyone know."
hock = "You are hockey. You have a bit of a chip on your shoulder and you can be a little to aggressive sometimes. As long as people stay out of your way there shouldn't be any problems though."
bow = "You are bowling. You might not be the most athletic person out there but you know how to have a good time. And you really like beer."
curl = "You are curling. You're just kinda weird. Stop being so weird."

def quiz_result(a, b, c, d, e, f, g):
    if a > b and a > c and a > d and a > e and a > f and a > g:
        return soc
    elif b > a and b > c and b > d and b > e and b > f and b > g:
        return bask
    elif c > a and c > b and c > d and c > e and c > f and c > g:
        return base
    elif d > a and d > b and d > c and d > e and d > f and d > g:
        return foot
    elif e > a and e > b and e > c and e > d and e > f and e > g:
        return hock
    elif f > a and f > b and f > c and f > d and f > e and f > g:
        return bow
    elif g > a and g > b and g > c and g > d and g > e and g > f:
        return curl
    else:
        return "You don't match any sports. I guess you'd better invent your own sport. You could call it " + name + "ball!"


print("What Sport Are You?")
name = input("What is your name: ")
print("Welcome " + name)
print(input(" "))

q1 = input("""Question One: Are your hands small, medium or large?: """)
if q1 == "small":
    soccer +=1
if q1 == "small":
    hockey += 1
if q1 == "small":
    curling += 1 
if q1 == "medium":
    baseball += 1
if q1 == "medium":
    bowling += 1
if q1 == "large":
    football += 1
if q1 == "large":
    basketball += 1
    

q2_list = ["hot", "cold"]
q2 = input("Question Two: Do you like cold or hot weather better?:")
if q2 == "cold":
    hockey += 2
if q2 == "cold":
    curling += 2
if q2 == "hot":
    baseball += 1
if q2 not in q2_list:
    soccer += 1
if q2 not in q2_list:
    football += 1
if q2 not in q2_list:
    basketball += 1
if q2 not in q2_list:
    bowling += 1
    

q3_list = ["sit", "stand"]
q3 = input("Question Three: Do you prefer to sit, stand or lay on the ground like a dead person?:")
if q3 == "sit":
    baseball += 2
if q3 == "sit":
    curling += 1
if q3 == "stand":
    soccer +=2
if q3 == "stand":
    basketball += 1
if q3 == "stand":
    hockey += 1
if q3 == "stand":
    football += 1
if q3 not in q3_list:
    bowling += 3
    
q4_list = ["dogs", "cats", "birds"]
q4 = input("Question four: If you could only have one type of pet would you prefer dogs, cats, birds or something else?")
if q4 == "dogs":
    basketball += 1
if q4 == "dogs":
    baseball += 1
if q4 == "dogs":
    football += 2
if q4 == "cats":
    soccer += 2
if q4 == "birds":
    hockey += 1
if q4 == "birds":
    bowling += 1
if q4 not in q4_list:
    curling += 1
    
q5 = input("Question five: Pick a number, from 1 to 7: ")
if q5 == 1:
    soccer += 2
if q5 == 2:
    basketball += 2
if q5 == 3:
    baseball += 2
if q5 == 4:
    football += 2
if q5 == 5:
    hockey += 2
if q5 == 6:
    bowling += 2
if q5 == 7:
    curling += 2


print(quiz_result(soccer, basketball, baseball, football, hockey, bowling, curling))



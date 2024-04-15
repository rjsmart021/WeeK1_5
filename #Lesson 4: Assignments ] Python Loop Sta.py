#Lesson4:AssignmentsPythonLoopStatements
#1. The Range Riddle
#Task 1. Every Other Day
Week = ["Sunday", "Monday", "Tuesday", "Wendsday", "Thursday", "Friday", "Saturday"]
Odd_i = []
even_i = []
for i in range (0, len(Week)):
    if i % 2:
        even_i.append(Week[i])
    else:
        Odd_i.append(Week[i])
print(even_i)
print(Odd_i)
#2 Nested Loops
#Task 1: Meal Planner
Meal = ['Pasta', 'Soup', 'Waffels', 'Sandwich'] 
import random
for i in range(len(Meal)):
    print('For breakfast we are having', random.choice(Meal))
    print('For lunch we are having' ,random.choice(Meal))
    print('For dinner we are having',random.choice(Meal))
#3.Loop Condition Logic
a = 1
while a > 3:
    print(a)
    a += 1
#Task 2: Conditional Exit
u = 1
while u < 6:
  print(u)
  if (u == 8):
    break
  u += 1
#4.Python's Random Game night
list = [ 'clipbord', 'Chair', 'carpet', 'hanger']
print(random.choice(list))
#5.Advanced Looping Techniques (Bonus)
ice_Cream = ['Vanila', 'Stawberry', 'Chery', 'Lavander', ' cookie and Cream']

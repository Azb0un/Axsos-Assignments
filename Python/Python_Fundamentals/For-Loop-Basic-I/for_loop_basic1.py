#1 Basic
for i in range(150):
    print(i)

print("-------------------------------------")
#2 Multiples of Five
for i in range(5,1001,5):
    print(i)

print("-------------------------------------")
#3 Counting, the Dojo Way
for i in range(1,101):
    if i%10 == 0:
        print("Coding Dojo")
    elif i%5 ==0:
        print("Coding")
    else :
        print(i)

print("-------------------------------------")
#4 Whoa. That Sucker's Huge
final_sum = 0
for i in range(500001):
    if i%2 ==1:
        final_sum = final_sum + i
print(final_sum)

print("-------------------------------------")
#5 Countdown by Fours
for i in range(2018,0,-4):
    print(i)

print("-------------------------------------")
#6 Flexible Counter
lowNum = 2
highNum = 9
mult = 3

for i in range(lowNum, highNum +1):
    if i% mult == 0:
        print(i)
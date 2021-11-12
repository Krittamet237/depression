print ('Depression Check')
print ('Over last 2 weeks, how often have you been bothered by any of the following problems')
print('If NOT AT ALL, type 0')
print ('If you have been bothered for 1-7 days, type 1')
print('If for more than 7 days, type 2')
print ('If every day, type 3')
Q1= input ('Little interest or pleasure in doing things\n')
ansQ1= int (Q1)
Q2= input('Feeling down, depressed, or hopeless\n')
ansQ2= int (Q2)
Q3= input ('Trouble falling or staying asleep, or sleeping too much\n')
ansQ3= int (Q3)
Q4= input('Feeling tired or having little energy\n')
ansQ4= int (Q4)
Q5= input('Poor appetite or overeating\n')
ansQ5= int(Q5)
Q6= input('Feeling bad about yourself-or that you are a failure or have let yourself or family down\n')
ansQ6= int (Q6)
Q7= input ('Trouble concentrating on things, such as reading the newspaper or watching television\n')
ansQ7= int (Q7)
Q8= input ('Moving or speaking slowly that other people could have noticed? OR being so figety or restless that you have been moving a lot more than usual\n')
ansQ8= int (Q8)
Q9= input('Thoughts that you would be better off dead or of hurting yourself in some way\n')
ansQ9= int (Q9)
sum = ansQ1+ansQ2+ansQ3+ansQ4+ansQ5+ansQ6+ansQ7+ansQ8+ansQ9
print ('Your Score: ', sum)
if sum<7:
    print ('Normal')
elif sum<13:
    print ('Mild Depression')
elif sum <19:
    print ('Moderate Depression')
else :
    print ('Severe Depression')
    


       
       

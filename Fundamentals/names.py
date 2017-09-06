#Part 1 given the list:
students = [
     {'first_name':  'Michael', 'last_name' : 'Jordan'},
     {'first_name' : 'John', 'last_name' : 'Rosales'},
     {'first_name' : 'Mark', 'last_name' : 'Guillen'},
     {'first_name' : 'KB', 'last_name' : 'Tonel'}
]
#Create a program that outputs:
'''
Michael Jordan
John Rosales
Mark Guillen
KB Tonel
'''
def names():
    for i in range(len(students)):
        print students[i]['first_name'], students[i]['last_name']

#Part 2 take this dictiony:
users = {
 'Students': [
     {'first_name':  'Michael', 'last_name' : 'Jordan'},
     {'first_name' : 'John', 'last_name' : 'Rosales'},
     {'first_name' : 'Mark', 'last_name' : 'Guillen'},
     {'first_name' : 'KB', 'last_name' : 'Tonel'}
  ],
 'Instructors': [
     {'first_name' : 'Michael', 'last_name' : 'Choi'},
     {'first_name' : 'Martin', 'last_name' : 'Puryear'}
  ]
 }
#Create:
'''
Students
1 - MICHAEL JORDAN - 13
2 - JOHN ROSALES - 11
3 - MARK GUILLEN - 11
4 - KB TONEL - 7
Instructors
1 - MICHAEL CHOI - 11
2 - MARTIN PURYEAR - 13
'''
def names(users):
    for i in users:
        print i
        for j in range(0,len(users[i])):
            print j+1, '-', users[i][j]['first_name'].upper(), users[i][j]['last_name'].upper(), '-', len(users[i][j]['first_name'])+len(users[i][j]['last_name'])

names(users)
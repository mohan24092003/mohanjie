# Q.1
name = input("enter youn name\n")
print("good afternoon,"+ name )

# Q.2
letter ='''dear <|name|>,
your are selected !

date: <|date|>
'''
name = input("enter your name\n")
date = input("enter date\n")
letter = letter.replace("<|name|>",name)
letter = letter.replace("<|date|>",date)
print(letter)
#Defining Parameters and Passing Arguments to Function
#def p(text <-- define parameter, any paremeter name):
#Function is an Object
#A function can accept inputs called arguments and return outputs called return values.
#The technical term for an expected input to a function is a parameter.
#And the actual value we provide as the input when the function is invoked is called the argument.
#You can think of Def almost like a variable assignment and output text as the name of a function.
#The function is an object and we are assigning it a name here called output text.
#the parameter name is completely up to us the developer.
#This is an input that we're going to provide to p and whatever we provide inside the parentheses will be available within the body or the block that we define the rules of the function and or the steps
# will be available within the body or the block that we define the rules of the function and or the steps

def p(text): #p(text) the insdie() is varaible name for function
    print(text)
p("Hello")
p("Goodbye")
p("OK")

#p() if p() is empty will show TypeError

def add(a, b):
    print("The sum of", a, "and", b, "is", a + b)

add(3, 5)
add(-4, 7)

#add()
#add(1)
#add(3, 5, 7) #TypeError will show if put value more than you set.

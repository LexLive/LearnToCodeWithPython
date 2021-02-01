
def output_text():
    print("Welcome to the program!")
    print("It's nice to meet you")
    print("have a wonderful day programing!")
    print("-" * 40)

output_text()
output_text()
output_text()
output_text()


def p(text): 
    print(text)
p("Hello")
p("Goodbye")
p("OK")

print("/" * 50)

def add(a, b):
    print("The sum of", a, "and", b, "is", a + b)

add(3, 5)
add(-4, 7)


def add(a, b, c):
    print("The sum of the three number is", a + b + c)

add(4, 6, 10) #position Argument
add(a = 5, b = 10, c= 15)#keyword Argument
add(5, b = 10, c = 15)
add(5, c = 10, b = 15) #any order


def add(a, b):
    return a + b #output #dont
    print("This is nonesense") #not show in Terminal

result = add(3, 5)
print(result)

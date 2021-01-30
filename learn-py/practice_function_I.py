def sf(great):
    print(great)
sf("Wanna be Great")
sf("Wanna be Love")

def none():
    print("anything")
    print("ABCDEF")
    print("*" * 20)
none()

#programiz youtube
def add_number(n1, n2):
    result = n1 + n2
    #print("The sum is", round(result,3)) #use return instead
    return result

#declared add_number outside function.
n1 = 5.4
n2 = 6.7
result = add_number(n1, n2)
print("The sum is", result)


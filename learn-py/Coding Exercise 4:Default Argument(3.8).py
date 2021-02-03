def text_out(a, b):
    return a + b
    
    
print(text_out('hello ', 'world'))
print(text_out('Emilio ', 'Estevez '))
print()
print(text_out('', '-'))
print(text_out('Tiger', '_'))


def multiplication(a, b, c):
	return a * b * c
	
	
print(multiplication(2, 2, 2))
print(multiplication(1, 1, 1,))
print(multiplication(3, 1, 1,))
print(multiplication(2, 5, 1,))

#course solution
def multiplication(a=1, b=2, c=3):
	return a * b * c
	
	
print(multiplication(2, 2, 2))
print(multiplication(1, 1, 1,))
print(multiplication(3, 1, 1,))
print(multiplication(2, 5, 1,))

#The print Function III: Parameters and Arguments
#Parameter: A name for an expected argument to a function
#print(*objects, sep=' ', end='\n', file=sys.stdout, flush=False)

#print("ABC", "DEF", "XYZ", sep="--*--") sep is parameter
#parameter not care the order the function know how it work

print("ABC", "DEF", "XYZ")
print("ABC", "DEF", "XYZ", sep="!")
print("ABC", "DEF", "XYZ", sep="--*--")
print("ABC", "DEF", "XYZ", sep=" ")

print("ABC", "DEF", "XYZ", "!")

print("Hello", "Goodbye", end="456")
print("Hello")

#Parameter the order does not matter.
print("A", "B", "C", sep="**", end="#")
print("A", "B", "C", end="#", set="**")
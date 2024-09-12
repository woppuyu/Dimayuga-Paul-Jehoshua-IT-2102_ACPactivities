char1, char2 = map(str, input("Enter two space-separated characters: ").split())

ascii1 = ord(char1)
ascii2 = ord(char2)

greaterAscii = char1 if ascii1 > ascii2 else char2

print("----------------------------------------------")
print(f"The character with greater value is: {greaterAscii}")
print("----------------------------------------------")

print("Showing ASCII Values: ")
print("%s : %d" % (char1, ascii1))
print("%s : %d" % (char2, ascii2))
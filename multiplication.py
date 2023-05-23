num = 1
times = int(input("""How many times do the "*2"? : """))
print ("")

for i in range (times):
    if (i % 5 == 0):
        print ("")
    if (i == times - 1):
        print(f"{num}.")
    else:
        print (f"{num}, ", end = "")
    num *= 2
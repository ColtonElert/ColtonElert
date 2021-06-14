num = 0
tot = 0 
while True:
    val = input("Enter a number or type stop to finish: ")
    if val == "stop":
        break
    try:
        fval = float(val)
    except:
        print("Invalid Input")
        continue
    print(fval)
    num = num + 1
    tot = tot + fval
print("===================================")
print("Done\n")
print("Sum", tot,"|" ,"Count", num,"|", "Average", tot / num)
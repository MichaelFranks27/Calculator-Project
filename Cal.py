#Running A Calculator

#C1 = "1, Add"
#C2 = "2, Subtract"
#C3 = "3, Multiply"
#C4 = "4, Divide"

Cal = input("Input Your Choice ")

if "1" in Cal:
 n1 = input("First Number ")
 n2 = input("Second Number ")
 print(str(int(n1) + int(n2))) #finally continue the rest for later

elif "2" in Cal:
 n1 = input("First Number ")  #nice fixed it
 n2 = input("Second Number ")
 print(str(int(n1) - int(n2)))

elif "3" in Cal:
 n1 = input("First Number ")
 n2 = input("Second Number ")
 print(str(int(n1) * int(n2)))

elif "4" in Cal:
 n1 = input("First Number ")
 n2 = input("Second Number ")
 print(str(int(n1) / int(n2))) #results can come out as a float
else:
 print("Error!" )

#accidently used if instead of elif











































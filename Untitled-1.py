a ='N12345678,B,,D,,C,B,,A,C,C,,B,A,B,A,,,,A,C,A,A,B,D,'
answer_key = "B,A,D,D,C,B,D,A,C,C,D,B,A,B,A,C,B,D,A,C,A,A,B,D,D"
while a.count(",,") != 0:
    x = a.replace(",,", ", ,")
    a = x
print(a[10:].split(","))
print(answer_key.split(","))

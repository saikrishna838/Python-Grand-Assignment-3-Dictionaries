string = input().split()

if string[1] == "+":
    sum_of_num = int(string[0]) + int(string[2])
    print(sum_of_num)
elif string[1] == "-":
    diff_of_num = int(string[0]) - int(string[2])
    print(diff_of_num)
elif string[1] == "*":
    mul_of_num = int(string[0]) * int(string[2])
    print(mul_of_num)
elif string[1] == "/":
    div_of_num = int(string[0]) / int(string[2])
    print(div_of_num)
elif string[1] == "%":
    modulation_of_num = int(string[0]) % int(string[2])
    print(modulation_of_num)

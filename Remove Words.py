def removing_all_the_words_of_k_length(string):
    len_string = len(string)
    new_string = ""
    for i in range(len_string):
        if len(string[i]) != n:
            new_string += string[i] + " "
    return new_string
            

string = input().split()
n = int(input())
result = removing_all_the_words_of_k_length(string)
print(result)
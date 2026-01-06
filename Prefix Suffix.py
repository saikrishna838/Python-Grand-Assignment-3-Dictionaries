def find_overlapping_word(string1, string2):
    min_length = min(len(string1), len(string2))
    
    for i in range(1, min_length + 1):
        if string1[-i:] == string2[:i]:
            return string1[-i:]
    return "No overlapping"
    

string1 = input()
string2 = input()
result = find_overlapping_word(string1, string2)
print(result)
        
    
    
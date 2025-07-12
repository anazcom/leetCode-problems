
def remove_duplicates(string):

    # Replace this placeholder return statement with your code
    stck = []
    for ch in string:
        if  stck and stck[-1] == ch: stck.pop()
        else: stck.append(ch); 
    
    return ''.join(stck)
        
print(remove_duplicates("aaxx"))
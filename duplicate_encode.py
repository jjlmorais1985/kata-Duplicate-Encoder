def duplicate_encode(word):
    encode = ""
    for char in word:
        counter = 0
        for letter in word:
            if str.lower(char) == str.lower(letter):
                counter +=1
    
        if counter > 1:
            encode += "("
        else:
            encode +=")"
    
    return encode

print(duplicate_encode("Success"))

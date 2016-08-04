def rot13(sentence):
    """
    7.10
    create an encryption that is a cypher that 
    moves the letter 13 places
    Ex. a = n; b = o; z = m; w = join
    """
    import string

    lower_z = 122
    cap_Z   = 90
    rotation = 13
    
    new_sent = []
    for char in sentence: 
        if char in string.ascii_lowercase:
            rot13_char = ord(char) + rotation
            if rot13_char > lower_z:
                rot13_char = ord(char) - rotation
        elif char in string.ascii_uppercase:
            rot13_char = ord(char) + rotation
            if rot13_char > cap_Z:
                rot13_char = ord(char) - rotation
        else:
            rot13_char = ord(char) #if out of spec, keep as is!
        new_sent.append(chr(rot13_char))
    return ''.join(new_sent)
  
sentence = "The quick brown Fox Jumped over The lazy Dog"
print "before:", sentence
print "after: ", rot13(sentence), "\n"

sentence = "Gur dhvpx oebja Sbk Whzcrq bire Gur ynml Qbt"
print "before:", sentence
print "after: ", rot13(sentence)
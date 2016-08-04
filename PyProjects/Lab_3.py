fo = open("document.txt", "r")
for line in fo:
    non_blank_lines = line.strip()
    if non_blank_lines:
        print (non_blank_lines)
fo.close()

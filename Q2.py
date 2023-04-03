def revword(next_word:str):
    next_word = next_word.lower()[::-1]
    return next_word

def countword():
    read_file = open('text.txt', 'r')
    first_word_count = 1
    line_counter = 1
    first_word = ""
    for line in read_file:
        if line_counter == 1:
            first_word = line.lower().strip()
            line_counter += 1
        else:
            list_word_line = line.split(" ")
            for word in list_word_line:
                fix_word = revword(word).strip()
                if fix_word == first_word:
                    first_word_count += 1
    print(first_word_count)

countword()   
                    
                
        
            

        

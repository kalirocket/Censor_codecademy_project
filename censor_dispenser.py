email_one = open("email_one.txt", "r").read()
email_two = open("email_two.txt", "r").read()
email_three = open("email_three.txt", "r").read()
email_four = open("email_four.txt", "r").read()



def censor_1(email, word):
    lst_of_word = []
    for i in range(1):
        lst_of_word.append(word.title())
        lst_of_word.append(word.lower())
        lst_of_word.append(word.upper())
        break
    lst_of_word_with_space = []
    lst_of_word_with_space.append(word.split())
    for lst in lst_of_word_with_space:
        joined = lst[0].title()+" "+lst[1].lower()
        lst_of_word.append(joined)
    lst_of_word = sorted(lst_of_word, key=len, reverse=True)
    for word_in_lst in lst_of_word:
        if word_in_lst in email:
           censor = ""
           for i in range(len(word_in_lst)):
               if word_in_lst[i] == " ":
                  censor += " "
               else:
                   censor += "*"
           email = email.replace(word_in_lst, censor)
    return email
#print(censor_1(email_one, "learning algorithms"))



proprietary_terms = \
    ["she", "personality matrix", "sense of self", "self-preservation", "learning algorithm", "learning algorithms", "her", "herself"]
def censor_2(email, lst_initial):
    lst_of_words = []
    lst_of_words_with_space = []
    for word in lst_initial:
        lst_of_words.append(word.upper())
        lst_of_words.append(word.lower())
        lst_of_words.append(word.title())
        if " " in word:
           lst_of_words_with_space.append(word.split())
    for lst in lst_of_words_with_space:
        first_word_title = lst[0].title()
        second_to_last_word = ""
        size = len(lst)
        joined = first_word_title
        i = 1
        while i < size:
              second_to_last_word += " " + lst[i]
              i += 1
        joined += second_to_last_word
        lst_of_words.append(joined)
    lst_of_words = sorted(lst_of_words, key=len, reverse=True)
    for word in lst_of_words:
        censor = ""
        for i in range(len(word)):
            if word[i] == " ":
                censor += " "
            else:
                censor += "*"
        email = email.replace(word, censor)
    return email
#print(censor_2(email_two, proprietary_terms))



negative_words = \
    ["concerned", "behind", "danger", "dangerous", "alarming", "alarmed", "out of control", "help", "unhappy", "bad", "upset", "awful", "broken", "damage", "damaging", "dismal", "distressed", "distressed", "concerning", "horrible", "horribly", "questionable"]
def censor_3(email, lst_1, lst_2_prev):
    email =  censor_2(email, lst_2_prev)
    lst_of_words = []
    lst_of_words_with_space = []
    for word in lst_1:
        lst_of_words.append(word.lower())
        lst_of_words.append(word.upper())
        lst_of_words.append(word.title())
        if " " in word:
           lst_of_words_with_space.append(word.split())
    for lst in lst_of_words_with_space:
        first_word_title = lst[0].title()
        second_to_last_word = ""
        size = len(lst)
        joined = first_word_title
        i = 1
        while i < size:
              second_to_last_word += " " + lst[i]
              i += 1
        joined += second_to_last_word
        lst_of_words.append(joined)
    counter = 0
    lst_of_word_in_email_with_location = []
    for word in lst_of_words:
        if word in email:
           counter += 1
           lst_of_word_in_email_with_location.append((email.find(word),word))
    lst_of_word_in_email_with_location_arranged = sorted(lst_of_word_in_email_with_location)
    lst_of_word_to_be_used = []
    if counter >= 2:
        i = 2
        while i >= 2 and i < len(lst_of_word_in_email_with_location_arranged):
              lst_of_word_to_be_used.append(lst_of_word_in_email_with_location_arranged[i])
              i += 1
    words_to_be_used_to_replace = []
    for lst in lst_of_word_to_be_used:
        words_to_be_used_to_replace.append((len(lst[1]), lst[1]))
    words_to_be_used_to_replace.sort(reverse=True)
    for word in words_to_be_used_to_replace:
        censor = ""
        for i in range(len(word[1])):
            if word[1][i] == " ":
                censor += " "
            else:
                censor += "*"
        email = email.replace(word[1], censor)
    return email
#print(censor_3(email_three, negative_words, proprietary_terms))



def censor_4(email, lst_1, lst_2):
    lst = []
    for term in lst_1:
        lst.append(term)
    for term in lst_2:
        lst.append(term)
    email_split = email.split()
    email_split_strip = []
    special_char = [".", ". ",",",", ","\n","!"]
    for word in email_split:
        for char in special_char:
            word = word.strip(char)
        email_split_strip.append(word)
    counter = -1
    word_in_email_in_lst = []
    for word in email_split_strip:
        counter += 1
        if word in lst:
           word_in_email_in_lst.append((word,counter))
    index_for_words = []
    for index in word_in_email_in_lst:
        index_for_words.append([index[1]-1, index[1], index[1]+1])
    possible_words = []
    possible_words_combined = []
    
    for index in index_for_words:
        for i in index:
            possible_words.append([email_split_strip[i], email_split_strip[i+1], email_split_strip[i+2]])
            break
    for words in possible_words:
        possible_words_combined.append([words[0],words[1],words[2]])
        for char in special_char:
            possible_words_combined.append([words[0]+char,words[1],words[2]])
            possible_words_combined.append([words[0],words[1]+char,words[2]])
            possible_words_combined.append([words[0],words[1],words[2]+char])
            i = 0
            while i < len(special_char):
                possible_words_combined.append([words[0]+char+special_char[i],words[1],words[2]])
                possible_words_combined.append([words[0],words[1]+char+special_char[i],words[2]])
                possible_words_combined.append([words[0],words[1],words[2]+char+special_char[i]])
                i += 1
    possible_words_com_joined = []
    for items in possible_words_combined:
        possible_words_com_joined.append((" ".join(items)))  
    for word_joined in possible_words_com_joined:
        if word_joined in email:
           censor = ""
           for i in range(len(word_joined)):
               if word_joined[i] == " ":
                  censor += " "
               else:
                   censor += "*"
           email = email.replace(word_joined, censor)
    email = censor_3(email, lst_1, lst_2)
    return email
#print(censor_4(email_four, negative_words, proprietary_terms))
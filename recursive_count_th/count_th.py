'''
Your function should take in a single parameter (a string `word`)
Your function should return a count of how many occurences of ***"th"*** occur within `word`. Case matters.
Your function must utilize recursion. It cannot contain any loops.
'''
count = 0

def count_th(word):
    global count
    if len(word) <= 1:
        tmp = count
        count = 0 
        return tmp
    if word[0] == 't':
        if word[1] == 'h':
            count +=1
            return count_th(word[2:])
    return count_th(word[1:])
# print(count_th('ergTHtherg'))
calls = 0

def calls_func():
    global calls
    calls += 1
    return calls



#def your_f():       # через функцию счетчик
   # your_f.counters += 1

#your_f.counters = 0

#for i in range(2,53):
   ##  print(your_f.counters)

def string_info(string):
    len_case = len(string)
    lover_case = string.lower()
    upper_case = string.upper()
    print (len_case, lover_case, upper_case)
    return calls_func()


def contains_info(string, list_to_search):
    lower_set = set(word.lower() for word in list_to_search)

    print(string.lower() in lower_set)
    return calls_func()

string_info('HelLo word')
string_info('HelLo world Our World, No, Its mine world')
string_info('HackTHeUrban, If no pay - we are gay!')
contains_info('UrBan', ['Hello', 'Ne Hello', 'BanAn', 'Vseh V Ban', 'Baklan', 'urbaN'])
contains_info('Счетчик жи есть', ['Жи есть', 'cЧетЧик', 'Schetchik'])

print(calls)
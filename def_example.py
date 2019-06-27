# function to return palindrom of a string

def palindrom_str(string_to):
    return str(string_to)[::-1]

def oddoreven(no):
    return int(no)%2==0


string = input("give a string : ")
print(palindrom_str(string))
print(oddoreven(string))
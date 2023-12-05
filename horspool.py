string1 = "TTATAGATCTCGTATTCTTTTATAGATCTCCTATTCTT"
string2 = "TCCTATTCTT"
str_dict = dict()

class StringMatcher():
    def __init__(self)-> None:
        pass

    def find_shift_value(self, word):
        for i in range(len(word)-1):
            str_dict[word[i]] = (len(word)-1) -i

        print(str_dict)

    def strMatch(self, biggerStr, smallerStr):
        b = len(biggerStr)
        s = len(smallerStr)
        i = 0
        a = []

        while i <= b-s:
            if biggerStr[i:i+s] == smallerStr:
                print('Found at index:', i)
                print(a)
                print(len(a))
                print(sum(a))
                return True
            
            if biggerStr[i+s-1] in str_dict:
                a.append(str_dict[biggerStr[i+s-1]])
                i += str_dict[biggerStr[i+s-1]]
                
            else:
                a.append(s)
                i += s

        print(a)
        return False
    
s = StringMatcher()
s.find_shift_value(string2)
print(s.strMatch(string1, string2))
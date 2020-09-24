vowels='AaEeIiOoUu'
count=0
string= input('Enter a word/string: ')
for s in string:
            if s in vowels: count=count+1
print(count)

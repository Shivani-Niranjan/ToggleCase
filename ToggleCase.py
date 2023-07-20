'''
You are given a character string A having length N, consisting of only lowercase and uppercase latin letters.

You have to toggle case of each character of string A. For e.g 'A' is changed to 'a', 'e' is changed to 'E', etc.

Input 1:
A = "tHiSiSaStRiNg"

Output 1:
ThIsIsAsTrInG 
'''

string = input("Enter String : ")
result = ""
for i in range(len(string)):
    result += chr(ord(string[i]) ^ (32))
print(result)

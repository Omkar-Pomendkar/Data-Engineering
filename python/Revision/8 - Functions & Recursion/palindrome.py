# To check whether number is palindrome or not
# madam 
def palindrome(s):
    if len(s) <= 1:
        print("Palindrome")
    else:
        if s[0] == s[-1]:
            palindrome(s[1:-1])
        else:
            print("Not a Palindrome")

result = palindrome("madamr")
print(result)
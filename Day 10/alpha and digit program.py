chr=input("Enter the character:")
if(chr.isalpha()):
    if(chr in 'aeiouAEIOU'):
        print("Vowel")
    else:
        print("Consonent")
elif(chr.isdigit()):
    print("digit")
else:
    print("Special character")

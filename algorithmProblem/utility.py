# Write your code here :-)

class Utility:

    @staticmethod
    def validAnagram(str1,str2):
        if sorted(str1)==sorted(str2):
            return True
        else:
            return False

util=Utility()

str1=input("Enter string 1 : ")
str2=input("Enter string 2 : ")
if (util.validAnagram(str1,str2)):
    print("String is anagram ",str1,str2)
else:
    print("String is not anagram")
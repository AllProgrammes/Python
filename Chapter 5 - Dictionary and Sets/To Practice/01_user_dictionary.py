hindiDict = {
             "khana": "eat",
             "maro": "beat somebody",
             "pyar": "love"
            }
print("Available options are --> ", list(hindiDict.keys()))

find=input("Enter the word for which you want to know the hindi meaning : ")
print("English meaning of",find,"is ->",hindiDict.get(find))

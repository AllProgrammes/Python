fruits_dic = {
    "banana": "something something",
    "grapes": "round round",
    "apple": "doctor's recommendations",
    "rating": [1, 2, 3, 4, 5],
}
# here all he fruits name are keys
print("\nBefore type casting -->")

print(fruits_dic.keys())  # prints all the keys
print(fruits_dic.values())  # prints all the values
print(fruits_dic.items())  # displays dictionary values in a tuple form
print(fruits_dic.update({"mango": "king of mangoes"}))
print(
    fruits_dic.get("apple")
)  # why to sue this ? because if we do this -->print(fruits_dic["apple"]) and if in case it is not found then it will throw an error unlike .get funtion

# We can also do typecasting [see below for more details]
print("\nAfter type casting -->")
print(list(fruits_dic.keys()))
print(list(fruits_dic.values()))

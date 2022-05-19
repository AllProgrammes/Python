iq_test = set()
iq_test.add(20)
iq_test.add(20.0)
iq_test.add("20")
print(
    "What will be the length of set (iq_test) ?\nAns :",
    len(iq_test),
    "because 20 and 20.0 is same for python but but but if we make it to 20.02 or 20.01 then it will count that as seperate value",
)

print(
    "\nCan we change list inside a set ?\nAns : No,because :-\n   1. We cannot enter a list inside a set\n   2. We cannot change any value inside a set as it is rigid in nature"
)

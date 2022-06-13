table = [
    str(i * 7) for i in range(1, 11)
]  # typecasted this to string because join fx takes only str values
formatted_table = "\n".join(table)
print(f"Table for 7 is as follows :-\n{formatted_table}")

for file_count in range(2, 21):
    with open(f"Tables/table_for_{file_count}.txt", "w") as f:
        for i in range(1, 11):
            f.write(f"{file_count}x{i}={file_count*i}\n")
            if i == 10:
                print(f"Table of {file_count} printed successfully !!")

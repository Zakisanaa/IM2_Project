rows = int(input("Enter rows: "))
cols = int(input("Enter columns: "))

for i in range(rows):
    for j in range(cols):
        val = input(f"Value at ({i+1},{j+1}): ")
        print(f"You entered: {val}")

rows = int(input("Enter rows: "))
cols = int(input("Enter columns: "))

table = [[int(input(f"({i+1},{j+1}): ")) for j in range(cols)] for i in range(rows)]

print("\nTable:")
for r in table:
    print(*r)

search = int(input("\nSearch: "))

for i in range(rows):
    for j in range(cols):
        if table[i][j] == search:
            print(f"Found {search} at Row {i+1}, Column {j+1}")
            exit()

print(f"{search} not found in the table.")

import csv

user_input = input(
    "What would you like to sort by? (Country, Name, GDPPC, Literacy, InfantMortality, Agriculture, Population, NetMigration): ")

with open('Countries.csv', 'r', newline='') as input_file:
    csv_input = csv.DictReader(input_file)
    print(csv_input)
    f1 = lambda row: row[user_input]
    f2 = lambda row: int(row[user_input])
    f3 = lambda row: float(row[user_input])
    if user_input == 'Country' or 'GDPPC' or 'Population':
        data = sorted(csv_input, reverse=True, key=f2)
    elif user_input == 'Literacy' or 'InfantMortality' or 'Agriculture' or 'NetMigration':
        data = sorted(csv_input, reverse=True, key=f3)
    else:
        data = sorted(csv_input, reverse=False, key=f1)

with open('Countries_Sorted.csv', 'w') as output_file:
    csv_output = csv.DictWriter(output_file, fieldnames=csv_input.fieldnames)
    csv_output.writeheader()
    csv_output.writerows(data)

with open('Countries_Sorted.csv', 'r') as final_file:
    for line in final_file:
        print(line)


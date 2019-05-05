import csv


user_input = input("What would you like to sort by? (Country,Name, GDPPC, Literacy, InfantMortality, Agriculture, Population, NetMigration): ")



with open('Countries.csv', 'r', newline='') as input_file:
    csv_input = csv.DictReader(input_file)
    data = sorted(csv_input,reverse=True, key=lambda row: (row[user_input]))

with open('Countries_Sorted.csv', 'w') as output_file:
    csv_output = csv.DictWriter(output_file, fieldnames=csv_input.fieldnames)
    csv_output.writeheader()
    csv_output.writerows(data)


with open('Countries_Sorted.csv', 'r') as final_file:
    for line in final_file:
        print(line)
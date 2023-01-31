import csv

customer = open('customers.csv','r')
customerfile = csv.reader(customer, delimiter=',')

fieldrow = next(customerfile)
fields = []
customer_data = []
total_customers = 0
for field in fieldrow:
    fields.append(field)


for customer in customerfile:
    customer_id = customer[0]
    customer_first = customer[1]
    customer_last = customer[2]
    customer_city = customer[3]
    customer_country = customer[4]
    customer_phone = customer[5]
    customer_data.append([customer_id, customer_first, customer_last, customer_city, customer_country, customer_phone])

    total_customers += 1

print(f"Total customers read:   {total_customers}")

filename = "customer _country.csv"

with open(filename, 'w') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow([fields[1], fields[2], fields[4]])
    for customer in customer_data:
        writer.writerow([customer[1], customer[2], customer[4]])
import csv 

sales = open('sales.csv','r')
salesfile = csv.reader(sales,delimiter= ',')

fieldrow = next(salesfile)
salesdat = []
actID = ""
tot_amt = 0

for entry in salesfile:
    CustomerID = entry[0]
    OrderDate = entry[1]
    ShipDate = entry[2]
    SubTotal = entry[3]
    TaxAmt = entry[4]
    Freight = entry[5]

    if CustomerID != actID:
        salesdat.append([actID, round(tot_amt, 2)])
        actID = CustomerID
        tot_amt = 0
    tot_amt += float(SubTotal) + float(TaxAmt) + float(Freight)

salesdat.append([actID, round(tot_amt, 2)])
salesdat.pop(0)

filename = "salesreport.csv"

with open(filename, 'w') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(["Customer", "Total"])
    for customer in salesdat:
        writer.writerow([customer[0], customer[1]])
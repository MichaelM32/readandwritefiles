import csv

customers = open('EmployeePay.csv','r')
empfile = csv.reader(customers, delimiter=',')

next(empfile)
fields = ["ID", "EmpFName", "EmpLName", "Salary", "Bonus", "Total"]
empdat = []
totalcust = 0

print(format(fields[0], "20"), format(fields[1], "20"), format(fields[2], "20"), format(fields[3], "20"), format(fields[4], "20"), format("Total Comp", "20"))

for employee in empfile:
    empid = employee[0]
    empfirst = employee[1]
    emplast = employee[2]
    empsal = employee[3]
    empbon = employee[4]
    emptotal = round(int(empsal) * (1 + float(empbon)), 2)

    print(format(empid, "20"), format(empfirst, "20"), format(emplast, "20"), format(empsal, "20"), format(empbon, "20"), format(emptotal, "20"))
    input()


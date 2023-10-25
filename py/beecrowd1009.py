name = str(input())
salary = float(input())
sales = float(input())


salary_final = salary + (sales * 0.15)
print("TOTAL = R$ {:.2f}".format(salary_final))
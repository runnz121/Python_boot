def year_payment(monthly_payment):
    m = monthly_payment
    tax_before, tax_after = 0,0

    tax_before = m * 12
    if(tax_before <= 1200):
        tax_after = tax_before * 0.94
    elif(1200 < tax_before <= 4600):
        tax_after = tax_before * 0.85
    elif(4600 < tax_before <= 8800):
        tax_after = tax_before * 0.76
    elif(8800 < tax_before <= 15000):
        tax_after = tax_before * 0.65
    elif(15000 < tax_before <= 30000):
        tax_after = tax_before * 0.62
    elif(30000 < tax_before <= 50000):
        tax_after = tax_before * 0.6
    elif(50000 < tax_before):
        tax_after = tax_before * 0.58

    print("세전 연봉:" + str(tax_before))
    print("세후 연봉:" + str(int(tax_after)))


monthly_payment = 300
print(year_payment(monthly_payment))


import random
from datetime import datetime, timedelta

from mimesis import Numbers, Text

gennum = Numbers()
gentext = Text()


def gen_datetime(min_year=2000, max_year=datetime.now().year):
    # generate a datetime in format yyyy-mm-dd hh:mm:ss.000000
    start = datetime(min_year, 1, 1, 00, 00, 00)
    years = max_year - min_year + 1
    end = start + timedelta(days=365 * years)
    return start + (end - start) * random.random()


company = 1000000  # 10 #1000000
shipment = 100  # 10 # 100
count = -1
f_company = open("D:\Program Files\PostgreSQL\data\company.csv", "w")
f_products = open("D:\Program Files\PostgreSQL\data\products.csv", "w")
f_shipment = []
for i in range(1, 21):
    f_shipment.append(open(f"D:\Program Files\PostgreSQL\data\shipment{i}.csv", "w"))

for i in range(1, company + 1):
    row_c = (
        f"{i}|Company_{i}|" + f"{gennum.integer_number(1, 500)}|" + '{"number":'
        f'"{gennum.integer_number(1, 100)}.{gennum.integer_number(1, 10)}.{gennum.integer_number(1, 10)}",'
        '"name":' + '"Some name"}|' + "["
    )
    m = gennum.integer_number(1, 7)
    for j in range(0, m):
        row_c += (
            '{"number":'
            + f'"{gennum.integer_number(1, 100)}.{gennum.integer_number(1, 10)}.{gennum.integer_number(1, 10)}",'
            + '"name":"Some name"}'
        )
        if j < m - 1:
            row_c += ","
    row_c += "]|["
    products = []
    prices = []
    for j in range(1, 4):
        product = gentext.word()
        text = gentext.text(quantity=5)
        price = gennum.integer_number(1, 999) * 10
        products.append(product)
        prices.append(price)
        row_c += "{" + f'"name":"{product}","price":{price}' + "}"
        if j < 3:
            row_c += ","
        row_p = f"{i}|" + f"Company{i}|" + f"{product}|" + f"{text}\n"
        f_products.write(row_p)
    for s in range(1, shipment + 1):
        count += 1
        customer = gennum.integer_number(1, 10000)
        row_s = f"{i}|" + f"Company_{i}|" + f"Customer_{customer}|"
        items = "["
        total_cost = 0
        for k in range(0, 3):
            val = gennum.integer_number(1, 100) * 10
            cost = val * prices[k]
            total_cost += cost
            items += (
                "{"
                + f'"name":"{products[k]}","price":{prices[k]},'
                + f'"quantity":{val},"cost":{cost}'
                + "}"
            )
            if k < 2:
                items += ","
        items += "]|"
        row_s += items + f"{gen_datetime()}|{total_cost}\n"
        f_shipment[count // 5000000].write(row_s)
    row_c += "]\n"
    f_company.write(row_c)
    row_c = ""
f_company.close()
f_products.close()
for i in range(20):
    f_shipment[i].close()

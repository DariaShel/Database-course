import random
from datetime import datetime, timedelta


company = 1000
shipment = 1000000
id_product = 1
with open("D:\Program Files\PostgreSQL\data\products1.csv", "w") as f4:
    for j in range(1, shipment + 1):
        c = random.randint(1, company)
        products = 50  # 10 #100
        for p in range(1, products + 1):
            money = random.randint(1, 1000000)
            row4 = f"'Some name{id_product}'|" + "'Some measure'|" + f"{money}" + "\n"
            f4.write(row4)
            id_product += 1

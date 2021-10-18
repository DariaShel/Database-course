import random
from datetime import datetime, timedelta


def gen_datetime(min_year=2015, max_year=datetime.now().year):
    # generate a datetime in format yyyy-mm-dd hh:mm:ss.000000
    start = datetime(min_year, 1, 1, 00, 00, 00)
    years = max_year - min_year + 1
    end = start + timedelta(days=365 * years)
    return start + (end - start) * random.random()


company = 1000  # 10 #1000
with open("D:\Program Files\PostgreSQL\data\company.csv", "w") as f1:
    for i in range(1, company + 1):
        row1 = (
            f"'Company{i}'|" + "1000|" + "{"
            f'"{random.randint(1, 100)}.{random.randint(1, 10)}.{random.randint(1, 10)}":'
            '"Some name"}|' + "{"
        )
        m = random.randint(1, 7)
        for j in range(0, m):
            row1 += (
                f'"{random.randint(1, 100)}.{random.randint(1, 10)}.{random.randint(1, 10)}":'
                '"Some name"'
            )
            if j < m - 1:
                row1 += ","
        row1 += "}\n"
        f1.write(row1)
        row1 = ""

emp = 1000  # 10 #1000
with open("D:\Program Files\PostgreSQL\data\employees.csv", "w") as f2:
    for i in range(1, company + 1):
        for j in range(1, emp + 1):
            row2 = (
                f"{i}|" + "{"
                f'"surname":"Surname_{i}_{j}","name":"Name_{i}_{j}","patronymic":"Patronymic_{i}_{j}",'
                f'"post":"Post_{i}_{j}","phone":"Some number_{i}_{j}","e-mail":"Some e-mail_{i}_{j}"'
                + "}\n"
            )
            f2.write(row2)
            row2 = ""

shipment = 1000000  # 10 #1000000
id_product = 1
with open("D:\Program Files\PostgreSQL\data\shipment.csv", "w") as f3:
    with open("D:\Program Files\PostgreSQL\data\products1.csv", "w") as f4:
        with open("D:\Program Files\PostgreSQL\data\products2.csv", "w") as f5:
            with open("D:\Program Files\PostgreSQL\data\sale_price1.csv", "w") as f6:
                with open(
                    "D:\Program Files\PostgreSQL\data\sale_price2.csv", "w"
                ) as f7:
                    with open(
                        "D:\Program Files\PostgreSQL\data\shipment_products1.csv", "w"
                    ) as f8:
                        with open(
                            "D:\Program Files\PostgreSQL\data\shipment_products2.csv",
                            "w",
                        ) as f9:
                            for j in range(1, shipment + 1):
                                c = random.randint(1, company)
                                row3 = f"{c}|" + "'Some customer name'|" + "{"
                                items = random.randint(1, 10)
                                for i in range(1, items + 1):
                                    row3 += f"'Item{i}'"
                                    if i < items:
                                        row3 += ","
                                row3 += "}|"
                                date_shipment = gen_datetime()
                                row3 += f"{date_shipment}|"

                                products = 100  # 10 #100
                                item = 0
                                cost = 0
                                for p in range(1, products + 1):
                                    money = random.randint(1, 1000000)
                                    row4 = (
                                        f"'Some name{id_product}'|"
                                        + "'Some measure'|"
                                        + f"{money}"
                                        + "\n"
                                    )
                                    if id_product < 50000000:
                                        f4.write(row4)
                                    else:
                                        f5.write(row4)
                                    if item < items:
                                        diff = random.randint(1, 1000)
                                        sale_price = money + diff
                                        row6 = (
                                            f"{id_product}|{c}|"
                                            + f"{sale_price}"
                                            + "\n"
                                        )
                                        if id_product < 50000000:
                                            f6.write(row6)
                                        else:
                                            f7.write(row6)
                                        volume = random.randint(1, 1000)
                                        costv = sale_price * volume
                                        row7 = (
                                            f"{j}|{id_product}|"
                                            + f"{volume}|"
                                            + f"{costv}|"
                                            + f"{gen_datetime(min_year=date_shipment.year, max_year=2025)}\n"
                                        )
                                        if id_product < 50000000:
                                            f8.write(row7)
                                        else:
                                            f9.write(row7)
                                        cost += costv
                                    id_product += 1
                                    item += 1
                                row3 += f"{cost}\n"
                                f3.write(row3)

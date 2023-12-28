import sys
import csv
import os
import res

def read_csv():
    file_path = os.path.join(res.res_path(), "goods.csv")

    with open(file_path, mode="r") as csv_file:
        reader = csv.reader(csv_file)
        headers = next(reader)
        columns = len(headers)

        for good_inf in reader:
            for i in range(0, columns):
                print(f"{headers[i]} - {good_inf[i]} ", end="")

            print()


def write_csv():
    cheap_path = os.path.join(res.res_path(), "cheap_goods.csv")
    all_path = os.path.join(res.res_path(), "goods.csv")

    os.remove(cheap_path)

    with open(cheap_path, "w", newline="") as cheap_file:
        with open(all_path, "r") as all_file:

            reader = csv.reader(all_file)
            headers = next(reader)
            cheap_goods = (good for good in reader if int(good[3]) < 10)

            writer = csv.writer(cheap_file)
            writer.writerow(headers)

            for good in cheap_goods:
                writer.writerow(good)


def dict_reader():
    file_path = os.path.join(res.res_path(), "goods.csv")

    with open(file_path, "r") as file:
        reader = csv.DictReader(file)

        for row in reader:
            print(f"{row['name']} - {row['price']}")

    print()

    with open(file_path, "r") as file:
        reader = csv.DictReader(file, fieldnames=("name", "id", "count", "cost"))
        headers = next(reader)

        for row in reader:
            print(f"{row['name']},{row['id']} - {row['cost']}")


def dict_writer():
    cheap_path = os.path.join(res.res_path(), "cheap_goods.csv")
    all_path = os.path.join(res.res_path(), "goods.csv")

    os.remove(cheap_path)

    with open(cheap_path, "w", newline="") as cheap_file:
        with open(all_path, "r") as all_file:
             reader = csv.DictReader(all_file)
             writer = csv.DictWriter(cheap_file, reader.fieldnames)

             cheap_goods = (good for good in reader if int(good['price']) < 10)

             for good in cheap_goods:
                 writer.writerow(good)


dict_writer()
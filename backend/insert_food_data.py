import csv
import os

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'backend.settings')
import django

django.setup()
from restapi import models


def check_if_null(data):
    if data == "NULL":
        return 0
    return float(data)


with open('food_data.csv', newline='') as csv_file:
    csv_reader = csv.reader(csv_file, quotechar='|')
    countdown = 5
    for row in csv_reader:
        if countdown == 0:
            data_to_insert = {
                'name': row[1],
                'iron': check_if_null(row[12]),
                'description': '',
                'calories': check_if_null(row[3]),
                'serving_size_amount': 100,
                'serving_size_unit': 'g',
                'total_fat': check_if_null(row[4]),
                'saturated_fat': check_if_null(row[10]),
                'trans_fat': check_if_null(row[27]),
                'cholesterol': check_if_null(row[9]),
                'sodium': check_if_null(row[40]),
                'total_carbs': check_if_null(row[6]),
                'fiber': check_if_null(row[8]),
                'sugars': check_if_null(row[7]),
                'protein': check_if_null(row[5]),
                'vitamin_a': check_if_null(row[15]),
                'vitamin_c': check_if_null(row[17]),
                'calcium': check_if_null(row[11]),
            }
            models.Food.objects.create(**data_to_insert)
        else:
            countdown -= 1

# 1 name, 3 cal, 4 fat, 5 protein, 6 carb, 7 sugars,
# 8 fiber, 9 chol, 10 sat fat, 11 calciu, 12 iron
# 15 vit a, 17 vit cy, 40 sodium, 27 trans fat, 10

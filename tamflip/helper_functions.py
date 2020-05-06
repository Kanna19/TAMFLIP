import csv

def get_airport_codes():
    with open('tamflip/static/dataset/airport-codes.csv') as f:
        return {
            k: v
            for k, v in csv.reader(f, delimiter=',')
        }

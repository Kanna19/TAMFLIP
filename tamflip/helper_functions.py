import re
import csv
import sys
from contextlib import contextmanager
from io import StringIO

def get_airport_codes():
    with open('tamflip/static/dataset/airport-codes.csv') as f:
        return {
            k.strip(): v.strip()
            for k, v in csv.reader(f, delimiter=',')
        }

def parse_airport_code(text):
    return re.search(r'\(([A-Z]+)\)$', text).groups()[0]

def get_parsed_form_dict(form):
    parsed_form = {k: v for k, v in form.items()}
    # Get Airport codes
    parsed_form['from_location'] = parse_airport_code(form['from_location'])
    parsed_form['to_location'] = parse_airport_code(form['to_location'])
    return parsed_form

# Source: https://stackoverflow.com/a/17981937
@contextmanager
def captured_output():
    new_out, new_err = StringIO(), StringIO()
    old_out, old_err = sys.stdout, sys.stderr
    try:
        sys.stdout, sys.stderr = new_out, new_err
        yield sys.stdout, sys.stderr
    finally:
        sys.stdout, sys.stderr = old_out, old_err

#!/usr/local/Cellar/python3/3.3.0/bin/python3.3

import csv
import phonenumbers as pn
import sys

def get_phone_fields(fields):
  return [fields.index(field) for field in fields if ((field.find('Phone') != -1) and (field.find('Value') != -1))]

def should_process_phone(phone):
  return phone.find(':::') == -1

def match_phone_numbers(phone_str):
  return [match.number for match in pn.PhoneNumberMatcher(phone_str, 'IN')]

def phone_object_for_phone(phone):
  try:
    return pn.parse(phone)
  except pn.phonenumberutil.NumberParseException:
    try:
      return pn.parse(phone, 'IN')
    except pn.phonenumberutil.NumberParseException:
      print("Couldn't parse number", phone)
      matched_phone_numbers = match_phone_numbers(phone)
      if matched_phone_numbers:
        return matched_phone_numbers
      return None

def boil_phone_numbers(phone_nums):
  for phone in phone_nums:
    ph = phone_object_for_phone(phone)
    if ph and isinstance(ph, list):
      for i in ph:
        print (phone, " -> ", pn.format_number(i, pn.PhoneNumberFormat.E164))
    elif ph:
      print (phone, " -> ", pn.format_number(ph, pn.PhoneNumberFormat.E164))
    else:
      print ("Phone number couldn't be parsed")

def process(row, phone_fields):
  phone_nums = [row[i] for i in phone_fields if row[i]]
  boil_phone_numbers(phone_nums)

def start():
  with open('google.csv', encoding = 'UTF-16') as f:
    formatted_data = csv.reader(f)
    fields = next(formatted_data)
    phone_fields = get_phone_fields(fields)
    print(fields)
    print(phone_fields)
    for row in formatted_data:
      process(row, phone_fields)

def main():
  if sys.version_info.major >= 3:
    start()

main()


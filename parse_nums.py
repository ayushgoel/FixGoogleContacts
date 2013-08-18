#!/usr/local/Cellar/python3/3.3.0/bin/python3.3

import csv
import phonenumbers as pn
import sys
import argparse

FIELD_PHONE = 'Phone'
FIELD_PHONE_NUMBER = 'Value'
MULTIPLE_PHONE_SEPARATOR = ':::'
FILE_ENCODING = 'UTF-16'

def get_phone_fields(fields):
  return [fields.index(field) for field in fields if ((field.find(FIELD_PHONE) != -1) and (field.find(FIELD_PHONE_NUMBER) != -1))]

def should_process_phone(phone):
  return phone.find(MULTIPLE_PHONE_SEPARATOR) == -1

def match_phone_numbers(phone_str, country_code):
  return [match.number for match in pn.PhoneNumberMatcher(phone_str, country_code)]

def phone_object_for_phone(phone, country_code):
  try:
    return pn.parse(phone)
  except pn.phonenumberutil.NumberParseException:
    try:
      return pn.parse(phone, country_code)
    except pn.phonenumberutil.NumberParseException:
      print("Couldn't parse number", phone)
      matched_phone_numbers = match_phone_numbers(phone, country_code)
      if matched_phone_numbers:
        return matched_phone_numbers
      return None

def boil_phone_numbers(phone_nums, country_code):
  for phone in phone_nums:
    ph = phone_object_for_phone(phone, country_code)
    if ph and isinstance(ph, list):
      phone_separator = MULTIPLE_PHONE_SEPARATOR.center(len(MULTIPLE_PHONE_SEPARATOR) + 2, ' ') 
      return phone_separator.join([pn.format_number(i, pn.PhoneNumberFormat.E164) for i in ph])
    elif ph:
      return pn.format_number(ph, pn.PhoneNumberFormat.E164) 
    else:
      print ("Phone number couldn't be parsed", phone_nums)
      return None

def process(row, phone_fields, country_code):
  newrow = list(row)
  for i in phone_fields:
    if row[i]:
      newrow[i] = boil_phone_numbers([row[i]], country_code)
      print(row[i], newrow[i])
  return newrow

def start(read_file_name, write_file_name, country_code):
  assert(read_file_name)
  if not write_file_name:
    write_file_name = 'formatted_google.csv'
  with open(read_file_name, encoding = FILE_ENCODING) as rf:
    with open(write_file_name, 'w', encoding = FILE_ENCODING) as wf:
      formatted_data = csv.reader(rf)
      fields = next(formatted_data)
      output_csv = csv.writer(wf, dialect = formatted_data.dialect)
      phone_fields = get_phone_fields(fields)
      print(fields)
      print(phone_fields)
      output_csv.writerow(fields)
      for row in formatted_data:
        output_csv.writerow(process(row, phone_fields, country_code))

def main():
  if sys.version_info.major < 3:
    print("Requires Python 3+ to work.")
    return

  # TODO : Add github url to `epilog`
  parser = argparse.ArgumentParser(description = 'Format your Phone-Book', epilog = '')

  parser.add_argument('--version', '-v', action = 'version', version = 'Version 0.1')
  # All arguments are required.
  ## Use 'append' as action to take multiple files as input.
  ## Use 'nargs' on files to take file names optionally
  ## Can give choices on country code from phonenumbers.geocoder.LOCALE_DATA
  parser.add_argument('-infile', help = 'The name of the phonebook file downloaded from Google Contacts.')
  parser.add_argument('-outfile', help = 'The file name to write the output to. Output is written in csv format.')
  parser.add_argument('-cc', '--countrycode', default = 'IN', help = '(default : %(default)s). The preferred country to try to boil a phone number to. Get your ISO Country Code from here : http://en.wikipedia.org/wiki/ISO_3166-1_alpha-2#Decoding_table')
  args = parser.parse_args()

  start(args.infile, args.outfile, args.countrycode)

main()


"""Auto-generated file, do not edit by hand. PT metadata"""
from ..phonemetadata import NumberFormat, PhoneNumberDesc, PhoneMetadata

PHONE_METADATA_PT = PhoneMetadata(id='PT', country_code=351, international_prefix='00',
    general_desc=PhoneNumberDesc(national_number_pattern='[2-46-9]\\d{8}', possible_number_pattern='\\d{9}'),
    fixed_line=PhoneNumberDesc(national_number_pattern='2(?:[12]\\d|[35][1-689]|4[1-59]|6[1-35689]|7[1-9]|8[1-69]|9[1256])\\d{6}', possible_number_pattern='\\d{9}', example_number='212345678'),
    mobile=PhoneNumberDesc(national_number_pattern='9(?:[136]\\d{2}|2[0-79]\\d|480)\\d{5}', possible_number_pattern='\\d{9}', example_number='912345678'),
    toll_free=PhoneNumberDesc(national_number_pattern='80[02]\\d{6}', possible_number_pattern='\\d{9}', example_number='800123456'),
    premium_rate=PhoneNumberDesc(national_number_pattern='76(?:0[1-57]|1[2-47]|2[237])\\d{5}', possible_number_pattern='\\d{9}', example_number='760123456'),
    shared_cost=PhoneNumberDesc(national_number_pattern='80(?:8\\d|9[1579])\\d{5}', possible_number_pattern='\\d{9}', example_number='808123456'),
    personal_number=PhoneNumberDesc(national_number_pattern='884[128]\\d{5}', possible_number_pattern='\\d{9}', example_number='884123456'),
    voip=PhoneNumberDesc(national_number_pattern='30\\d{7}', possible_number_pattern='\\d{9}', example_number='301234567'),
    pager=PhoneNumberDesc(national_number_pattern='NA', possible_number_pattern='NA'),
    uan=PhoneNumberDesc(national_number_pattern='70(?:7\\d|8[17])\\d{5}', possible_number_pattern='\\d{9}', example_number='707123456'),
    emergency=PhoneNumberDesc(national_number_pattern='112', possible_number_pattern='\\d{3}', example_number='112'),
    voicemail=PhoneNumberDesc(national_number_pattern='NA', possible_number_pattern='NA'),
    short_code=PhoneNumberDesc(national_number_pattern='NA', possible_number_pattern='NA'),
    standard_rate=PhoneNumberDesc(national_number_pattern='NA', possible_number_pattern='NA'),
    no_international_dialling=PhoneNumberDesc(national_number_pattern='NA', possible_number_pattern='NA'),
    number_format=[NumberFormat(pattern='(2\\d)(\\d{3})(\\d{4})', format='\\1 \\2 \\3', leading_digits_pattern=['2[12]']),
        NumberFormat(pattern='([2-46-9]\\d{2})(\\d{3})(\\d{3})', format='\\1 \\2 \\3', leading_digits_pattern=['2[3-9]|[346-9]'])])

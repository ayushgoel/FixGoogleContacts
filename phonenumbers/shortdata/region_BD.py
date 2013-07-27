"""Auto-generated file, do not edit by hand. BD metadata"""
from ..phonemetadata import NumberFormat, PhoneNumberDesc, PhoneMetadata

PHONE_METADATA_BD = PhoneMetadata(id='BD', country_code=None, international_prefix=None,
    general_desc=PhoneNumberDesc(national_number_pattern='1\\d{2,4}', possible_number_pattern='\\d{3,5}'),
    fixed_line=PhoneNumberDesc(national_number_pattern='1\\d{2,4}', possible_number_pattern='\\d{3,5}'),
    mobile=PhoneNumberDesc(national_number_pattern='1\\d{2,4}', possible_number_pattern='\\d{3,5}'),
    toll_free=PhoneNumberDesc(national_number_pattern='NA', possible_number_pattern='NA'),
    premium_rate=PhoneNumberDesc(national_number_pattern='NA', possible_number_pattern='NA'),
    shared_cost=PhoneNumberDesc(national_number_pattern='NA', possible_number_pattern='NA'),
    personal_number=PhoneNumberDesc(national_number_pattern='NA', possible_number_pattern='NA'),
    voip=PhoneNumberDesc(national_number_pattern='NA', possible_number_pattern='NA'),
    pager=PhoneNumberDesc(national_number_pattern='NA', possible_number_pattern='NA'),
    uan=PhoneNumberDesc(national_number_pattern='NA', possible_number_pattern='NA'),
    emergency=PhoneNumberDesc(national_number_pattern='NA', possible_number_pattern='NA'),
    voicemail=PhoneNumberDesc(national_number_pattern='NA', possible_number_pattern='NA'),
    short_code=PhoneNumberDesc(national_number_pattern='1(?:0(?:[39]|5(?:0\\d|[1-4])|6\\d{2}|7[0-4]|8[0-29])|1[6-9]|2(?:2[0-5]|[34])|3(?:1\\d?|3\\d|6[3-6])|4(?:0\\d|1\\d{2})|5[2-9])', possible_number_pattern='\\d{3,5}', example_number='103'),
    standard_rate=PhoneNumberDesc(national_number_pattern='NA', possible_number_pattern='NA'),
    no_international_dialling=PhoneNumberDesc(national_number_pattern='NA', possible_number_pattern='NA'),
    short_data=True)

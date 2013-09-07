FixGoogleContacts
=================
This python script fixes your [Google Contacts] by adding appropriate Country Code for you. (See here for more info : [Country Code]).
The international dialling code for your country is prepended to your contacts numbers intelligently where ever required.  
This cleaning/boiling of numbers makes your phonebook country independent and clean.  
For eg. A number from my contact book (I am from [India]), if reads - 9812343242/09812343242, it would be converted to +919812343242.

Usage
=====
* Go to [Google Contacts].
* Click on `More`>`Export`
* Choose : 
    * `All contacts`
    * `Google CSV format (for importing into a Google account)`
* Click  `Export`  and save the file given by Google.

Let this file be `google.csv`.   
**Warning: Save this file somewhere safe. If anything goes wrong, you can always reset your contacts using this.**

Now run the script on this file and save the output. Let this output be  `google_final.csv`.

* Delete all your contacts from [Google Contacts].
* Click on `More`>`Import`.
* Choose  `google_final.csv`  from file chooser.
* Click  `Import`.

*You are done.!! Have a look at the changes and enjoy the beauty!! :)*

Credits
=======
Thanks to [libphonenumber] and the creator of it's python port here [libphonenumber-python].

Requirements
============
* Python 3

Contact
=======
Have any suggestions or just wanna thank me for this? Mail me at `ayushgoel111@gmail.com`. I would love to hear from you. :)


[Country Code]: http://countrycode.org "Country Code"
[Google Contacts]: https://www.google.com/contacts/ "Google Contacts"
[India]: http://countrycode.org/india "India"
[libphonenumber]: http://code.google.com/p/libphonenumber/ "libphonenumber"
[libphonenumber-python]: https://github.com/daviddrysdale/python-phonenumbers "libphonenumber-python"

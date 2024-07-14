#!/usr/bin/python3

petition_keys = ['created_at', 'id', 'cr_no', 'date_received', 'amount_involved', 'petition_source', 'updated_at',          
                 'casefile_no', 'date_assigned', 'status_signal', 'staff_id']

nigeria_states = ("Abia", "Abuja", "Adamawa", "Akwa Ibom", "Anambra", "Bauchi",
                  "Bayelsa", "Benue", "Borno", "Cross River", "Delta",
                  "Ebonyi", "Edo", "Ekiti", "Enugu", "Gombe", "Imo",
                  "Jigawa", "Kaduna", "Kano", "Katsina", "Kebbi",
                  "Kogi", "Kwara", "Lagos", "Nasarawa", "Niger",
                  "Ogun", "Ondo", "Osun", "Oyo", "Plateau", "Rivers",
                  "Sokoto", "Taraba", "Yobe", "Zamfara")

id_cards = ('Licence', 'NIN', 'Passport')

recovery_statuses = ('With Exhibit keeper', 'Tendered in Court',
                    'Interim forfeiture', 'Final Forfeiture')

top_currencies = ("USD", "EUR", "GBP", "NGN")

'''
top_currencies = ("USD", "EUR", "CNY", "JPY", "GBP", "AUD", "CAD", "CHF",
                  "INR", "KRW", "RUB", "BRL", "HKD", "SEK", "SGD", "TRY",
                  "MXN", "NZD", "ZAR", "NOK")
'''

nigeria_skin_colors = ('Dark Brown', 'Brown', 'Light Brown',
                                           'Dark', 'Fair', 'Caramel')

religion_types = ('Islam', 'Christianity', 'Traditional', 'Others')

offence_types = ("False Pretence", "Impersonation", "Forgery", "Conspiracy",
           "Aiding and Abetting", "Stealing", "Theft", "Bribery", "Tax Evasion")

summary = ('name', 'occupation', 'phone_no', 'nationality',
           'offence', 'gender', 'id')

petition_status = ("UI", "Legal", "Court", "Convicted")
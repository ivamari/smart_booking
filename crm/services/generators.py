import random

from transliterate import translit


class FakeTrafficGenerator:
    pass


class FakeClientGenerator:
    def generate_client(self, count):
        pass

    def generate_email(self, first_name, middle_name, last_name, dob):
        first_name_translit = translit(first_name, language_code='ru',
                                       reversed=True)
        middle_name_translit = translit(middle_name, language_code='ru',
                                        reversed=True)
        last_name_translit = translit(last_name, language_code='ru',
                                      reversed=True)

        return f'{first_name_translit[0]}{middle_name_translit[0]}.{last_name_translit}{dob.year}'

    def generate_phone(self):
        phone_number = '+7'
        for i in range(1, 11):
            phone_number = phone_number + str(random.randint(0, 9))
        return phone_number

    # def generate_dob(self):
    #     return random.randint(1960, 2005)


class FakeReservationGenerator:
    pass

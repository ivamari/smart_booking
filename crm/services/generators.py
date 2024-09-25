import os
import random
from datetime import timedelta, date

from django.db import transaction
from transliterate import translit

from clients.models.clients import Client
from dicts.models.dicts import Gender


class FakeTrafficGenerator:
    pass


class FakeClientGenerator:

    def __init__(self):
        base_dir = os.path.dirname(__file__)
        self.data_dir = os.path.join(base_dir, 'data')

        self.last_names = self.load_data('last_name.txt')
        self.first_names_male = self.load_data('first_name_male.txt')
        self.first_names_female = self.load_data('first_name_female.txt')
        self.middle_name_female = self.load_data('middle_name_female.txt')
        self.middle_name_male = self.load_data('middle_name_male.txt')

    def load_data(self, filename):
        path = os.path.join(self.data_dir, filename)
        with open(path, 'r') as f:
            return [line.strip() for line in f.readlines()]

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

    def generate_dob(self):
        start_date = date(1960, 1, 1)
        end_date = date(2005, 12, 31)
        random_date = start_date + timedelta(
            days=random.randint(0, (end_date - start_date).days))
        return random_date

    def generate_client(self, gender):
        if gender == 'male':
            first_name = random.choice(self.first_names_male)
            last_name = random.choice(self.last_names)
        else:
            first_name = random.choice(self.first_names_female)
            last_name = random.choice(self.last_names) + 'а'

        middle_name = random.choice(self.middle_name_male)
        dob = self.generate_dob()
        email = self.generate_email(first_name, middle_name, last_name, dob)
        phone = self.generate_phone()

        return {
            'first_name': first_name,
            'last_name': last_name,
            'middle_name': middle_name,
            'gender': gender,
            'dob': dob,
            'email': email,
            'phone': phone
        }

    @transaction.atomic
    def generate_clients(self, count):
        clients = []
        for _ in range(count):
            gender = random.choice(['M', 'F'])
            client_data = self.generate_client(gender)

            client = Client.objects.create(
                first_name=client_data['first_name'],
                last_name=client_data['last_name'],
                middle_name=client_data['middle_name'],
                gender=Gender.objects.get(code=client_data['gender']),
                dob=client_data['dob'],
                email=client_data['email'],
                phone=client_data['phone']
            )
            clients.append(client)
        return clients


class FakeReservationGenerator:
    pass

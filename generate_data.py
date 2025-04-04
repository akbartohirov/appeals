import os
import django
import random
from faker import Faker
from datetime import date, timedelta

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'client_registry.settings')
django.setup()

from appeals.models import Appeal

fake = Faker()

ORG_CHOICES = ['OrgA', 'OrgB']
APPOINTMENT_TYPE_CHOICES = ['Type1', 'Type2']
CURRENCY_CHOICES = ['UZS', 'USD', 'EUR']
STATUS_CHOICES = ['новое', 'в работе', 'закрыто']

def generate_appeals(n=100):
    for _ in range(n):
        Appeal.objects.create(
            name=fake.name(),
            appeal_org=random.choice(ORG_CHOICES),
            appointment=fake.job(),
            appointment_type=random.choice(APPOINTMENT_TYPE_CHOICES),
            client_code=fake.unique.bothify(text='CL###??'),
            client_card=fake.unique.bothify(text='CARD####'),
            drop_card=fake.unique.bothify(text='DROP####'),
            appeal_date=fake.date_between(start_date='-1y', end_date='today'),
            responsible=fake.name(),
            controller=fake.name(),
            damage=random.randint(1000, 100000),
            currency=random.choice(CURRENCY_CHOICES),
            status=random.choice(STATUS_CHOICES),
            measures=fake.paragraph(nb_sentences=3)
        )

    print(f"✅ {n} обращений успешно добавлены в базу данных.")

if __name__ == "__main__":
    generate_appeals(100)

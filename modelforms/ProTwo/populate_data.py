import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "ProTwo.settings")

import django
django.setup()


from appTwo.models import User
from faker import Faker
fakeobject = Faker()


def populate_data(N=5):
    for entry in range(N):
        row_object = User.objects.get_or_create(first_name=fakeobject.unique.first_name(),
                                                last_name=fakeobject.last_name(),
                                                email=fakeobject.email())[0]


if __name__ == '__main__':
    print("populating data")
    populate_data(20)
    print("populating the data completed")

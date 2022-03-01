import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "first_project.settings")

import django
django.setup()

# fake populating the script
import random
from first_app.models import AccessRecord, Topic, Webpage
from faker import Faker

fakegen = Faker()  # this generator object is created using Faker() class
topics = ["Search", "Social", "Marketplace", "News", "Games"]  # various topics for different websites.

def add_topic():
    t = Topic.objects.get_or_create(top_name=random.choice(topics))[0]  # creates single record for the table using ORM.
    t.save()
    return t


def populate(N=5):

    for entry in range(N):

        # get the topic for the entry
        top = add_topic()

        # create fake data for the entry
        fake_url = fakegen.url()
        fake_date = fakegen.date()
        fake_name = fakegen.company()

        # create a new webpage entry. Here a record is created using ORM. [0] creates single row.
        # for a foreign key, give the object itself.
        webpg = Webpage.objects.get_or_create(topic=top, name=fake_name, url=fake_url)[0]

        # create a fake access record for that webpage. A new single record is created.
        # for a foreign key, give the object itself.
        acc_rec = AccessRecord.objects.get_or_create(name=webpg, date=fake_date)[0]


if __name__ == '__main__':
    print("populating script!!")
    populate(20)
    print("population complete")

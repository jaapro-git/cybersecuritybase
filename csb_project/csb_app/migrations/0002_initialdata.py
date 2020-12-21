from django.db import migrations
from django.contrib.auth.hashers import make_password

def add_entries(apps, schema_editor):
    timeSheetEntry = apps.get_model('csb_app', 'timeSheetEntry')
    User = apps.get_model('auth', 'User')

    tester1 = User.objects.create(username='tester1', password=make_password('init1234'), is_active=True)
    tester2 = User.objects.create(username='tester2', password=make_password('init4321'), is_active=True)

    timeSheetEntry.objects.create(user=tester1, start="2020-12-10 12:00", end="2020-12-10 13:13", time=73, comment="example entry for tester1", completed=True)
    timeSheetEntry.objects.create(user=tester2, start="2020-12-10 12:00", end="2020-12-10 13:00", time=60, comment="example entry for tester2", completed=True)

class Migration(migrations.Migration):

    dependencies = [
        ('csb_app', '0001_initial'),
    ]

    operations = [
        migrations.RunPython(add_entries),
    ]

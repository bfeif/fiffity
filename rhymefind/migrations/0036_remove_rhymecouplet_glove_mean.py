# Generated by Django 3.0.1 on 2020-05-19 14:39

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('rhymefind', '0035_auto_20200518_2059'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='rhymecouplet',
            name='glove_mean',
        ),
    ]
# Generated by Django 3.0.1 on 2020-05-14 14:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rhymefind', '0031_auto_20200513_1606'),
    ]

    operations = [
        migrations.AddIndex(
            model_name='rhymefind',
            index=models.Index(fields=['word'], name='RF_word_idx'),
        ),
    ]

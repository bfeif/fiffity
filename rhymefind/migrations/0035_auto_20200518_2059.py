# Generated by Django 3.0.1 on 2020-05-18 20:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rhymefind', '0034_remove_word_glove'),
    ]

    operations = [
        migrations.AlterField(
            model_name='word',
            name='word',
            field=models.CharField(db_index=True, max_length=100, unique=True),
        ),
    ]
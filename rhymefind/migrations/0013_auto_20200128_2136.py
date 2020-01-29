# Generated by Django 3.0.1 on 2020-01-28 21:36

import django.contrib.postgres.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rhymefind', '0012_auto_20200102_2129'),
    ]

    operations = [
        migrations.CreateModel(
            name='Glove50d',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('word', models.CharField(max_length=100)),
                ('nsfw', models.BooleanField(default=False)),
                ('glove_0', models.FloatField(null=True)),
                ('glove_1', models.FloatField(null=True)),
                ('glove_2', models.FloatField(null=True)),
                ('glove_3', models.FloatField(null=True)),
                ('glove_4', models.FloatField(null=True)),
                ('glove_5', models.FloatField(null=True)),
                ('glove_6', models.FloatField(null=True)),
                ('glove_7', models.FloatField(null=True)),
                ('glove_8', models.FloatField(null=True)),
                ('glove_9', models.FloatField(null=True)),
                ('glove_10', models.FloatField(null=True)),
                ('glove_11', models.FloatField(null=True)),
                ('glove_12', models.FloatField(null=True)),
                ('glove_13', models.FloatField(null=True)),
                ('glove_14', models.FloatField(null=True)),
                ('glove_15', models.FloatField(null=True)),
                ('glove_16', models.FloatField(null=True)),
                ('glove_17', models.FloatField(null=True)),
                ('glove_18', models.FloatField(null=True)),
                ('glove_19', models.FloatField(null=True)),
                ('glove_20', models.FloatField(null=True)),
                ('glove_21', models.FloatField(null=True)),
                ('glove_22', models.FloatField(null=True)),
                ('glove_23', models.FloatField(null=True)),
                ('glove_24', models.FloatField(null=True)),
                ('glove_25', models.FloatField(null=True)),
                ('glove_26', models.FloatField(null=True)),
                ('glove_27', models.FloatField(null=True)),
                ('glove_28', models.FloatField(null=True)),
                ('glove_29', models.FloatField(null=True)),
                ('glove_30', models.FloatField(null=True)),
                ('glove_31', models.FloatField(null=True)),
                ('glove_32', models.FloatField(null=True)),
                ('glove_33', models.FloatField(null=True)),
                ('glove_34', models.FloatField(null=True)),
                ('glove_35', models.FloatField(null=True)),
                ('glove_36', models.FloatField(null=True)),
                ('glove_37', models.FloatField(null=True)),
                ('glove_38', models.FloatField(null=True)),
                ('glove_39', models.FloatField(null=True)),
                ('glove_40', models.FloatField(null=True)),
                ('glove_41', models.FloatField(null=True)),
                ('glove_42', models.FloatField(null=True)),
                ('glove_43', models.FloatField(null=True)),
                ('glove_44', models.FloatField(null=True)),
                ('glove_45', models.FloatField(null=True)),
                ('glove_46', models.FloatField(null=True)),
                ('glove_47', models.FloatField(null=True)),
                ('glove_48', models.FloatField(null=True)),
                ('glove_49', models.FloatField(null=True)),
            ],
        ),
        migrations.CreateModel(
            name='RhymeCouplet50d',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_added', models.DateField(auto_now_add=True)),
                ('date_last_updated', models.DateField(auto_now=True)),
                ('nsfw', models.BooleanField(default=False)),
                ('word_1', models.CharField(max_length=100)),
                ('word_2', models.CharField(max_length=100)),
                ('phoneme_seq_1', django.contrib.postgres.fields.ArrayField(base_field=models.CharField(max_length=3), null=True, size=None)),
                ('phoneme_seq_2', django.contrib.postgres.fields.ArrayField(base_field=models.CharField(max_length=3), null=True, size=None)),
                ('rhyme_seq', django.contrib.postgres.fields.ArrayField(base_field=models.CharField(max_length=3), null=True, size=None)),
                ('glove_mean_0', models.FloatField(null=True)),
                ('glove_mean_1', models.FloatField(null=True)),
                ('glove_mean_2', models.FloatField(null=True)),
                ('glove_mean_3', models.FloatField(null=True)),
                ('glove_mean_4', models.FloatField(null=True)),
                ('glove_mean_5', models.FloatField(null=True)),
                ('glove_mean_6', models.FloatField(null=True)),
                ('glove_mean_7', models.FloatField(null=True)),
                ('glove_mean_8', models.FloatField(null=True)),
                ('glove_mean_9', models.FloatField(null=True)),
                ('glove_mean_10', models.FloatField(null=True)),
                ('glove_mean_11', models.FloatField(null=True)),
                ('glove_mean_12', models.FloatField(null=True)),
                ('glove_mean_13', models.FloatField(null=True)),
                ('glove_mean_14', models.FloatField(null=True)),
                ('glove_mean_15', models.FloatField(null=True)),
                ('glove_mean_16', models.FloatField(null=True)),
                ('glove_mean_17', models.FloatField(null=True)),
                ('glove_mean_18', models.FloatField(null=True)),
                ('glove_mean_19', models.FloatField(null=True)),
                ('glove_mean_20', models.FloatField(null=True)),
                ('glove_mean_21', models.FloatField(null=True)),
                ('glove_mean_22', models.FloatField(null=True)),
                ('glove_mean_23', models.FloatField(null=True)),
                ('glove_mean_24', models.FloatField(null=True)),
                ('glove_mean_25', models.FloatField(null=True)),
                ('glove_mean_26', models.FloatField(null=True)),
                ('glove_mean_27', models.FloatField(null=True)),
                ('glove_mean_28', models.FloatField(null=True)),
                ('glove_mean_29', models.FloatField(null=True)),
                ('glove_mean_30', models.FloatField(null=True)),
                ('glove_mean_31', models.FloatField(null=True)),
                ('glove_mean_32', models.FloatField(null=True)),
                ('glove_mean_33', models.FloatField(null=True)),
                ('glove_mean_34', models.FloatField(null=True)),
                ('glove_mean_35', models.FloatField(null=True)),
                ('glove_mean_36', models.FloatField(null=True)),
                ('glove_mean_37', models.FloatField(null=True)),
                ('glove_mean_38', models.FloatField(null=True)),
                ('glove_mean_39', models.FloatField(null=True)),
                ('glove_mean_40', models.FloatField(null=True)),
                ('glove_mean_41', models.FloatField(null=True)),
                ('glove_mean_42', models.FloatField(null=True)),
                ('glove_mean_43', models.FloatField(null=True)),
                ('glove_mean_44', models.FloatField(null=True)),
                ('glove_mean_45', models.FloatField(null=True)),
                ('glove_mean_46', models.FloatField(null=True)),
                ('glove_mean_47', models.FloatField(null=True)),
                ('glove_mean_48', models.FloatField(null=True)),
                ('glove_mean_49', models.FloatField(null=True)),
            ],
        ),
        migrations.AddIndex(
            model_name='rhymecouplet50d',
            index=models.Index(fields=['word_1', 'word_2'], name='RhymeCoup50d_word1_word2_idx'),
        ),
        migrations.AddIndex(
            model_name='rhymecouplet50d',
            index=models.Index(fields=['word_1'], name='RhymeCoup50d_word1_idx'),
        ),
        migrations.AddIndex(
            model_name='rhymecouplet50d',
            index=models.Index(fields=['word_2'], name='RhymeCoup50d_word2_idx'),
        ),
        migrations.AddIndex(
            model_name='glove50d',
            index=models.Index(fields=['word'], name='Glove50d_word_idx'),
        ),
    ]

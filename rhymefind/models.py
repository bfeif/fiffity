from django.db import models
from django.contrib.postgres.fields import ArrayField
max_length = 100

'''
NOTE: DJANGO does not actually update the schema of the db when you add a default value to a column
'''

# rhyme couplet glove model
class RhymeCouplet32dIND(models.Model):

    # fields to add
    nsfw = models.BooleanField(default=False)

    # fields from Python model
    word_1 = models.CharField(max_length=max_length)
    word_2 = models.CharField(max_length=max_length)
    phoneme_seq_1 = ArrayField(models.CharField(max_length=3), null=True)
    phoneme_seq_2 = ArrayField(models.CharField(max_length=3), null=True)
    rhyme_seq = ArrayField(models.CharField(max_length=3), null=True)

    # indexes
    class Meta:
        indexes = [
            models.Index(fields=['word_1', 'word_2'],
                         name="RC32dIND_word1_word2_idx"),
            models.Index(fields=['word_1'], name="RC32dIND_word1_idx"),
            models.Index(fields=['word_2'], name="RC32dIND_word2_idx"),
            models.Index(fields=['glove_mean_{}'.format(i) for i in range(32)], name='RC32dIND_glove_idx')
        ]

    # method definitions
    def __str__(self):
        return (self.word_1 + ', ' + self.word_2)


# add glove attributes to RhymeCouplet
for i in range(32):
    RhymeCouplet32dIND.add_to_class(
        'glove_mean_' + str(i), models.FloatField(null=True))


# single word glove model
class Glove32dIND(models.Model):

    # fields
    word = models.CharField(max_length=max_length)
    nsfw = models.BooleanField(default=False)

    # indexes
    class Meta:
        indexes = [
            models.Index(fields=['word'], name="Glove32dIND_word_idx"),
        ]

    # method definitions
    def __str__(self):
        return (self.word)


# add glove attributes to RhymeCouplet
for i in range(32):
    Glove32dIND.add_to_class('glove_' + str(i), models.FloatField(null=True))


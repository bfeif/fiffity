import pandas as pd
import numpy as np
glove_data_path = './data/glove.6B/glove.6B.{}d.txt'


def process_glove_line(x):
    '''
    GLOVE loading helper fucntion
    '''
    splitted = x.split()
    return (splitted[0].lower(), np.array(splitted[1:], dtype=np.float64))


def process_cmu_line(x):
    '''
    CMU loading helper function
    '''
    splitted = x.split()
    return (splitted[0].lower(), splitted[1:])


def convert_phoneme_seq_to_rhyme_seq(phoneme_seq):
    '''
    Convert a phoneme sequence to a rhyme sequence
    '''
    b = ['1' in i for i in phoneme_seq]
    try:
        return tuple(phoneme_seq[b.index(True):])
    except:
        return tuple(phoneme_seq)


def load_cmu_dict(exclude_non_nltk_words=True):
    '''
    Loads cmu dictionary to a dataframe of columns [word<str>, phoneme_seq<List[str]>, rhyme_seq<List[str]>]
    '''
    cmu_records = map(process_cmu_line, open('./data/cmudict.txt').readlines())
    rhyme_dict = pd.DataFrame(cmu_records, columns=['word', 'phoneme_seq'])
    if exclude_non_nltk_words:
        from nltk.corpus import words
        nltk_words = set(words.words())
        nltk_words_mask = rhyme_dict.word.isin(nltk_words)
        rhyme_dict = rhyme_dict.loc[nltk_words_mask, :]
    rhyme_dict['rhyme_seq'] = rhyme_dict.phoneme_seq.apply(
        lambda x: convert_phoneme_seq_to_rhyme_seq(x))
    return rhyme_dict


def load_glove_dict(glove_dimensions=50, dimensions_to_reduce_to=-1):
    '''
    Loads glove dictionary to a dataframe of columns [word<str>, glove<np.array[float]>]
    '''

    # create the dataframe
    df = pd.DataFrame(map(process_glove_line, open(glove_data_path.format(
        glove_dimensions)).readlines()), columns=['word', 'glove'])

    # do dimiensionality reduction if necessary
    if dimensions_to_reduce_to == -1:
        pass
    else:
        pass

    # return
    return df


def create_rhyme_couplet_glove_df(glove_table, rhyme_table):
    '''
    Creates the rhyme couplet glove table
    '''

    # add glove data to the rhyme table
    rhyme_glove_table = rhyme_table.merge(glove_table, how='inner', left_on='word', right_on='word')

    # make a copy
    rhyme_glove_table_copy = rhyme_glove_table.copy()

    # merge copies to make the dictionary
    couplet_dictionary = rhyme_glove_table.merge(
        rhyme_glove_table_copy, how='inner', left_on='rhyme_seq', right_on='rhyme_seq', suffixes=('_l', '_r'))

    # get rid of couplets of the same word, e.g. ['and', 'and']
    couplet_dictionary = couplet_dictionary[couplet_dictionary.word_l !=
                                            couplet_dictionary.word_r]

    # get rid of duplicates, e.g. ['and', 'band'] vs ['band', 'and']
    couplet_dictionary['word_tuple'] = couplet_dictionary.apply(
        lambda x: tuple(sorted([x['word_l'], x['word_r']])), axis=1)
    couplet_dictionary.drop_duplicates(subset=['word_tuple'], inplace=True)

    # get glove_mean
    couplet_dictionary['glove_mean'] = np.split((np.vstack(couplet_dictionary['glove_l']) + np.vstack(
        couplet_dictionary['glove_r'])) / 2, indices_or_sections=len(couplet_dictionary), axis=0)

    # return
    return couplet_dictionary

def split_df_list_column(dataframe, column_name):
    '''
    Takes a dataframe that has a column of type List[obj] and returns the same dataframe with new columns obj_1, obj_2, ..., obj_n
    '''
    pass
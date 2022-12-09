"""
date: January 2021
author: Léo Picard
contact: leopicard.net
"""

import os
import pandas as pd
import glob
import regex as re


def clean_vars(path, text):
    file_id_clean = re.findall(r'\w{2}\d{4}.txt', path)
    clean_text = re.sub(r'\n|\t', ' ', text)
    clean_text = re.sub(r'\s{2,}', ' ', clean_text)
    if clean_text[0] == ' ':
        clean_text = clean_text[1:]
        
    return file_id_clean[0], clean_text


if __name__ == '__main__':
    os.chdir('/home/picard0001/Switchdrive/Private/GitHub/sots/')
    
    metadata = pd.read_csv('metadata.csv')
    
    files = glob.glob('speeches_raw/*.txt').copy()
    
    text = []
    for file in files:
        with open(file, 'r') as f:
            new_text = f.read().rstrip('\n')
        text.append(new_text)
    del file, new_text, f
    
    speeches = pd.DataFrame({'file_id': files, 'text': text})
    del files, text
    
    speeches['file_id'], speeches['text'] = zip(*speeches.apply(lambda x: clean_vars(x['file_id'], x['text']), axis = 1))
    
    dataset = speeches.merge(metadata, on = 'file_id', how = 'outer')
    
    dataset = dataset[['file_id', 'state_id', 'state_name', 'year', 'speaker', 'party', 'type', 'quality', 'text', 'source', 'remarks']].sort_values(by = 'file_id')
    
    dataset.to_csv('dataset_parsed.csv', index = False)
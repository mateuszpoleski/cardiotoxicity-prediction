# Code from data_preparation notebook. Created to have easy imports for other notebooks. 
import pandas as pd
import numpy as np


def remove_wrong_values(df):
    df['IC50'] = pd.to_numeric(df['IC50'], errors='coerce')
    df = df.dropna()
    return df

def remove_least_used(df, min_perc_used=0):
    occur = pd.DataFrame(df.drop('IC50', axis=1).sum())
    occur.columns = ['number_of_feature_occurrences']
    min_occurrs = int(df.shape[0] * min_perc_used)
    not_qualified = occur[occur['number_of_feature_occurrences']<min_occurrs]
    return df.drop(not_qualified.index, axis=1)

def remove_target_outliers(df):
    return df[(df['IC50']>1) & (df['IC50']<=100_000)]

def make_log_scale(df):
    df['IC50'] = np.log10(df['IC50'])
    return df

def prepare_df(file, min_perc_used=0, remove_outliers=True, log_scale=True):
    print(f'Preparing ({file}) file.')
    df = pd.read_csv(file, low_memory=False)
    print(f'DataFrame base shape: {df.shape}')
    
    df = remove_wrong_values(df)
    print(f'Shape after removing wrong values: {df.shape}')
    
    if min_perc_used != 0:
        df = remove_least_used(df, min_perc_used=min_perc_used)
        print(f'Shape after removing least used features: {df.shape}')
    if remove_outliers:
        df = remove_target_outliers(df)
        print(f'Shape after removing outliers: {df.shape}')
    if log_scale:
        df = make_log_scale(df)    
        
    print()
    return df

def classify_on_IC50(df, IC50_threshold, log_scale=True):
    df = df.copy()
    if log_scale:
        IC50_threshold = np.log10(IC50_threshold)
    df['IC50'] = np.where(df['IC50']<IC50_threshold, 1, 0)
    return df






def get_MACCSFP_fingerprints(min_perc_used=0, remove_outliers=True, log_scale=True):
    file = 'ready_sets/cardiotoxicity_hERG_MACCSFP.csv'
    df = prepare_df(file, min_perc_used=min_perc_used, remove_outliers=remove_outliers, log_scale=log_scale)
    return df

def get_KlekotaRoth_fingerprints(min_perc_used=0, remove_outliers=True, log_scale=True):
    file = 'ready_sets/cardiotoxicity_hERG_KlekFP.csv'
    df = prepare_df(file, min_perc_used=min_perc_used, remove_outliers=remove_outliers, log_scale=log_scale)
    return df

def get_hashed_fingerprints(min_perc_used=0, remove_outliers=True, log_scale=True):
    file = 'ready_sets/cardiotoxicity_hERG_ExtFP.csv'
    df = prepare_df(file, min_perc_used=min_perc_used, remove_outliers=remove_outliers, log_scale=log_scale)
    return df

def get_mixed_fingerprints(min_perc_used=0, remove_outliers=True, log_scale=True):
    print('Preparing files for mixed fingerprints.\n')
    df1 = get_MACCSFP_fingerprints(min_perc_used=min_perc_used, remove_outliers=remove_outliers, log_scale=log_scale)
    df2 = get_KlekotaRoth_fingerprints(min_perc_used=min_perc_used, remove_outliers=remove_outliers, log_scale=log_scale).drop('IC50',axis=1)
    df3 = get_hashed_fingerprints(min_perc_used=min_perc_used, remove_outliers=remove_outliers, log_scale=log_scale).drop('IC50',axis=1)
    
    return df1.join(df2).join(df3)

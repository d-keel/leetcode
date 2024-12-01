import pandas as pd

def combine_two_tables(person: pd.DataFrame, address: pd.DataFrame) -> pd.DataFrame:
    mergedDf: pd.DataFrame = person.merge(right=address, on='personId', how='left')
    mergedDf = mergedDf[['firstName', 'lastName', 'city', 'state']]
    return mergedDf

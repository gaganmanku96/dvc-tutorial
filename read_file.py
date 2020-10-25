import csv 

import pandas as pd
from dvc.api import read

def get_data():
    data = read('data/covid_jpn_prefecture.csv',
                repo='https://github.com/gaganmanku96/dvc-tutorial')
    data = data.split('\n')

    reader = csv.reader(data)
    fields = next(reader)

    rows = []
    for row in reader:
        rows.append(row)
    
    return pd.DataFrame(rows, columns=fields)


if __name__ == '__main__':
    df = get_data()
    print(df.head())
import requests
import pandas as pd
from bs4 import BeautifulSoup
import os

def main():
    url = 'https://www.ncei.noaa.gov/data/local-climatological-data/access/2021/'
    dir = r'C:\Users\Thiago\Documents\GitHub\data-engineering-practice\Exercises\Exercise-2'
    output_dir = os.path.join(dir, 'downloads')

    if 'downloads' in os.listdir(dir):
        pass
    else:
        os.mkdir(os.path.join(dir, 'downloads'))

    r = requests.get(url)
    soup = BeautifulSoup(r.content, 'html.parser')

    table = str(soup.find_all('table'))
    df = pd.read_html(table)
    df = df[0].drop('Description', axis=1)
    df = df.dropna()
    df_clean = df[df['Last modified'] == '2022-02-07 14:03']
    filenames = df_clean['Name']


    for i in filenames:
        req = requests.get(str(url + '/' + i))
        with open (os.path.join(output_dir, i), 'wb') as f:
            f.write(req.content)
    
    
    pathdir = os.listdir(output_dir)
    for file in pathdir:
        arq = pd.read_csv(os.path.join(output_dir, file))
        arq['HourlyDryBulbTemperature'] = arq['HourlyDryBulbTemperature'].astype(str)
        arq['HourlyDryBulbTemperature'] = arq['HourlyDryBulbTemperature'].str.replace('s', '')
        arq = arq.sort_values('HourlyDryBulbTemperature', ascending=False)
        print(arq.head(5))
    
    pass


if __name__ == "__main__":
    main()

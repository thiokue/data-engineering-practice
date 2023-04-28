import pandas as pd
import os



def main():
    pass


def json_search(path):

    json_files = []
    for root, dirs, files in os.walk(path):
            for file in files:
                if file.endswith('.json'):
                    json_files.append(os.path.join(root, file))
    return json_files

def convert_files_into_df(json_files):
    df_list = []
    for file in json_files:
        df = pd.read_json(file)
        df_list.append(df)
    return df_list

def into_csv(df_list):
     count = 1
     for df in df_list:
        df.to_csv(f'file-{count}.csv')
        count += 1
        print(f'Successfully created csv with shape {df.shape}')


if __name__ == "__main__":
    path = './data'
    json_files = json_search(path)
    df_list = convert_files_into_df(json_files)
    into_csv(df_list)


import requests
import os
import logging
import zipfile

logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s %(levelname)s:%(name)s:%(message)s',
    datefmt='%Y-%m-%d %H:%M:%S',
    filename='exercises.log',
    filemode='a'
)


logger = logging.getLogger('exercises')

download_uris = [
    "https://divvy-tripdata.s3.amazonaws.com/Divvy_Trips_2018_Q4.zip",
    "https://divvy-tripdata.s3.amazonaws.com/Divvy_Trips_2019_Q1.zip",
    "https://divvy-tripdata.s3.amazonaws.com/Divvy_Trips_2019_Q2.zip",
    "https://divvy-tripdata.s3.amazonaws.com/Divvy_Trips_2019_Q3.zip",
    "https://divvy-tripdata.s3.amazonaws.com/Divvy_Trips_2019_Q4.zip",
    "https://divvy-tripdata.s3.amazonaws.com/Divvy_Trips_2020_Q1.zip",
    "https://divvy-tripdata.s3.amazonaws.com/Divvy_Trips_2220_Q1.zip",
]

dir = r'C:\Users\Thiago\Documents\GitHub\data-engineering-practice\Exercises\Exercise-1'
folders = os.listdir(dir)
output_path = os.path.join(dir, 'downloads')

def main():
    
    pass

def folder_chkr(folders, output_path):
    if 'downloads' in folders:
        return False
    else:
        logging.info('An download folder was not found, creating one...')
        os.mkdir(output_path)
        logging.info('Folder created!')
        return True



def file_downloader(download_uris, output_path):
    logging.info('Starting downloads...')
    if folder_chkr(folders=folders, output_path=output_path):
        for uri in download_uris:
            r = requests.get(uri)
            raw_uri = uri.split('/')
            filename = raw_uri[-1]
            output_with_filename = os.path.join(output_path, filename)
            logging.info(f'Downloading {filename} at {output_with_filename}')
            with open(output_with_filename, 'wb') as f:
                f.write(r.content)
            logging.info(f'The file: {filename} was downloaded successfully!')
    else:
        pass
    pass



def data_extract():
    output_path = os.path.join(dir, 'downloads')
    try:
        logging.info('Extracting zip files...')
        for file in os.listdir(output_path):
            logging.info(f'Extracting {file}...')
            with zipfile.ZipFile(os.path.join(output_path, file), 'r') as zip:
                zip.extractall(os.path.join(dir, 'extracted_files'))
        logging.info('The files were extracted!')
    except zipfile.BadZipFile as e:
        logging.error(e)
    pass

def cleanup(output_path, dir):
    logging.info('Cleaning up...')
    if 'downloads' in os.listdir(dir):
        files = os.listdir(output_path)
        for file in files:
            os.remove(os.path.join(output_path, file))
        os.rmdir(output_path)
    logging.info('Done!')



if __name__ == "__main__":
    logging.info('Starting script...')
    file_downloader(download_uris=download_uris, output_path=output_path)
    data_extract()
    cleanup(output_path=output_path, dir=dir)
    logging.info('Script ran successfully!')


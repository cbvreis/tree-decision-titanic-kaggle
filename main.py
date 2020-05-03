import pandas as pd
import zipfile as zp




def model():
    zip = zp.ZipFile('titanic.zip')
    df_gender = pd.read_csv(zip.open(zip.filelist[0]))
    df_train = pd.read_csv(zip.open(zip.filelist[1]))
    df_gender.head()


if __name__ == '__main__':
    model()
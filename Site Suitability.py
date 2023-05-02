# Import CSV file
import csv

# Read input data
import csv
import pandas as pd

url = 'https://raw.githubusercontent.com/DanielINCE/Assignment-2/main/Geology.txt'
df = pd.read_csv(url,index_col=0)
#df = pd.read_csv(url)


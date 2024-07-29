import pandas as pd
import os

def ingest_data():
    input_file = 'data/cars_2010_2020.csv'  # Ajuste o caminho conforme necessário
    output_file = 'data/cars_data.csv'  # Ajuste o caminho conforme necessário
    
    df = pd.read_csv(input_file)
    df.to_csv(output_file, index=False)

if __name__ == "__main__":
    ingest_data()

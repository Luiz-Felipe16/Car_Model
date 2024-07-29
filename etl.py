import pandas as pd

def etl_process():
    input_file = 'data/cars_data.csv'
    output_file = 'data/transformed_cars_data.csv'
    
    df = pd.read_csv(input_file)
    
    # Exemplo de transformação: adicionar uma coluna 'Price in EUR'
    df['Price (EUR)'] = df['Price (USD)'] * 0.85  # Supondo uma taxa de câmbio fictícia
    
    df.to_csv(output_file, index=False)

if __name__ == "__main__":
    etl_process()

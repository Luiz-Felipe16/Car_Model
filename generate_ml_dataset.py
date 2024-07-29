import pandas as pd

def generate_ml_dataset():
    input_file = 'data/transformed_cars_data.csv'
    output_file = 'data/ml_cars_data.csv'
    
    df = pd.read_csv(input_file)
    
    # Seleção de features e target
    features = df[['Year', 'Engine Size (L)', 'Price (EUR)']]
    target = df['Price (USD)']
    
    ml_data = pd.concat([features, target], axis=1)
    ml_data.to_csv(output_file, index=False)

if __name__ == "__main__":
    generate_ml_dataset()

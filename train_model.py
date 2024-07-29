import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
import joblib

def train_model():
    input_file = 'data/transformed_cars_data.csv'
    model_file = 'data/cars_price_model.pkl'
    
    df = pd.read_csv(input_file)
    
    # Feature Engineering e seleção de variáveis
    X = df[['Year', 'Engine Size (L)', 'Price (EUR)']]
    y = df['Price (USD)']
    
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
    
    model = LinearRegression()
    model.fit(X_train, y_train)
    
    joblib.dump(model, model_file)
    print("Modelo treinado e salvo em", model_file)

if __name__ == "__main__":
    train_model()

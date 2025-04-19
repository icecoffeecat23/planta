import pandas as pd
import numpy as np

def load_dataB(csv_path):
    df = pd.read_csv(csv_path)
    
    # Convert to datetime and calculate days since first measurement
    df['Date'] = pd.to_datetime(df['Date'], format='mixed', dayfirst=True )
    df['Days'] = (df['Date'] - df['Date'].iloc[0]).dt.days
    
    # Extract days and height values
    days = df['Days'].values.astype(float)
    height = df['Height'].values.astype(float)
    
    return np.array([days, height])


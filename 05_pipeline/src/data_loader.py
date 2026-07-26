"""
Data Loader Module for Amazonian Plant Growth Habit Classification.
"""

import pandas as pd

def load_data(file_path: str) -> pd.DataFrame:
    """
    Loads raw CSV dataset and standardizes column names and missing values.
    
    Args:
        file_path (str): Path to the input dataset file.
        
    Returns:
        pd.DataFrame: Cleaned pandas DataFrame.
    """
    df = pd.read_csv(file_path, sep=';', encoding='latin-1')
    
    # Standardize column names
    df.columns = [
        'N', 'Family', 'Scientific_Name', 'Distribution', 'Common_Name', 
        'Uses', 'Habit', 'Group', 'Class', 'Order', 'Genus', 'References'
    ]
    
    # Strip whitespace from target variable
    df['Habit'] = df['Habit'].astype(str).str.strip()
    
    # Fill missing values in text and categorical columns
    df['Family'] = df['Family'].fillna('Unknown')
    df['Genus'] = df['Genus'].fillna('Unknown')
    df['Distribution'] = df['Distribution'].fillna('Unknown')
    df['Uses'] = df['Uses'].fillna('Unknown')
    
    return df

if __name__ == "__main__":
    import sys
    path = sys.argv[1] if len(sys.argv) > 1 else "../data/dataset.csv"
    data = load_data(path)
    print(f"Successfully loaded dataset with shape: {data.shape}")

import pandas as pd

def handle_missing_nationality(file_path):
    """
    Check the Country column for missing values and handle them.
    
    Answer:
    Out of 8205 rows, there are 1339 missing or empty 'Country' values, which 
    accounts for approximately 16% of the dataset. 
    
    Since this is a significant portion of the data, dropping these rows would result 
    in a substantial loss of information, which could negatively impact the CLV model. 
    Instead, these missing values should be imputed. Given that there's no clear way 
    to reliably infer the exact country for these customers from the other columns, 
    the safest and most informative approach is to fill the missing values with a 
    placeholder like "Unknown" (or "Other"). This preserves the transaction data while 
    allowing the model to treat missing nationalities as its own category.
    """
    df = pd.read_csv(file_path)
    
    # Check for both NaN and empty strings
    missing_country_mask = df['Country'].isnull() | (df['Country'].str.strip() == '')
    num_missing = missing_country_mask.sum()
    
    print(f"Total missing Country values: {num_missing} out of {len(df)} rows")
    
    # Fill missing with "Unknown"
    df.loc[missing_country_mask, 'Country'] = 'Unknown'
    
    return df

if __name__ == "__main__":
    handle_missing_nationality('ecommerce_data.csv')

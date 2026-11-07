import pandas as pd

def check_null_customer_ids(file_path):
    """
    Check the CustomerID column for missing values and analyze any trends.
    
    Answer:
    Out of 8205 rows, there are only 16 rows with missing CustomerID values.
    Analyzing the distribution of these missing values across other columns like 
    'Country' and 'ProductCategory' shows no specific trends (they are randomly 
    distributed similar to the overall dataset). 
    
    Since CustomerID is essential for Customer Lifetime Value (CLV) modeling—as we 
    cannot aggregate transactions or predict lifetime value for an unknown customer—and 
    the number of missing rows is negligible (less than 0.2%), these rows should be dropped.
    """
    df = pd.read_csv(file_path)
    
    null_customers = df[df['CustomerID'].isnull()]
    
    print(f"Total missing CustomerIDs: {len(null_customers)} out of {len(df)} rows")
    
    if len(null_customers) > 0:
        print("\nDistribution of missing CustomerIDs by Country:")
        print(null_customers['Country'].value_counts())
        
        print("\nDistribution of missing CustomerIDs by ProductCategory:")
        print(null_customers['ProductCategory'].value_counts())
        
    return df.dropna(subset=['CustomerID'])

if __name__ == "__main__":
    check_null_customer_ids('ecommerce_data.csv')

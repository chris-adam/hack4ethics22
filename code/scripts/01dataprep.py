import pandas as pd

# https://data.europa.eu/data/datasets/eu-ecolabel-products?locale=en
ethical_products_df = pd.read_csv('https://ecenvdatapublic.blob.core.windows.net/ecolabel/exports/most-recent-export.csv')

# https://datahub.io/core/country-list
country_codes_df = pd.read_csv('https://datahub.io/core/country-list/r/data.csv')

# set data types correct
ethical_products_df = ethical_products_df.convert_dtypes()
country_codes_df = country_codes_df.convert_dtypes()

# select only records with PRODUCT
df = ethical_products_df.loc[ethical_products_df['PRODUCT_SERVICE'] == 'PRODUCT']

# only keep relevant columns
df = df.drop(['PRODUCT_SERVICE', 'LIC_NR', 'GROUP_CODE', 'GROUP_NAME', 'EXTID_TYPE', 'EXT_ID', 'VAT', 'COMPANY_COUNTRY'], axis=1)

# rename column names to proper values
df = df.rename(columns={'NAME': 'ProductName', '\DECISION': 'Decision', 'EXPIRATION_DATE': 'ExpirationDate', 'COMPANY_NAME':'CompanyName', 'COUNTRY': 'Country'})

#merge country codes
df = pd.merge(df, 
              country_codes_df[['Name', 'Code']],
              left_on='Country',
              right_on='Code')
df = df.drop(['Country'], axis=1)
df = df.rename(columns={'Name': 'CountryName', 'Code': 'CountryCode'})

# ### Save CSVs
df[['CompanyName', 'ProductName']].drop_duplicates().to_csv("has_product.csv", index=False, sep=',')
df[['CompanyName', 'CountryName']].drop_duplicates().to_csv("located_in.csv", index=False, sep=',')
df[['ProductName', 'CountryName']].drop_duplicates().to_csv("come_from.csv", index=False, sep=',')
df[['ProductName', 'Decision', 'ExpirationDate']].drop_duplicates().to_csv("date.csv", index=False, sep=',')
df.drop_duplicates().to_csv("complete_cleaned.csv", index=False, sep=',')

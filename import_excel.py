import pandas as pd
import os
import django
from datetime import datetime

# Setup Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')
django.setup()

from assets.models import Asset, Assignment

file_path = "Asset_Register_Final.xlsx"

# Check if file exists
if not os.path.exists(file_path):
    print("Excel file not found. Place Asset_Register_Final.xlsx in project root.")
    exit()

# Read Excel
df = pd.read_excel(file_path)

# Replace NaN with None
df = df.where(pd.notnull(df), None)

current_asset = None

for _, row in df.iterrows():

    # Create new asset if Serial Number exists
    if row.get('Serial Number'):

        # Safe year conversion
        year = None
        if row.get('Year') not in [None, ""]:
            try:
                year = int(row['Year'])
            except:
                year = None

        # Safe date conversion
        invoice_date = None
        value = row.get('InvoiceDate')
        if value:
            try:
                dt = pd.to_datetime(value, errors='coerce')
                if pd.notnull(dt):
                    invoice_date = dt.date()
            except:
                invoice_date = None

        current_asset = Asset.objects.create(
            serial_number=row.get('Serial Number'),
            company=row.get('Company'),
            computer_type=row.get('Computer Type'),
            brand=row.get('Brand'),
            model=row.get('Model'),
            year=year,
            opco_asset_tag=row.get('OpCo Asset Tag'),
            invoice_number=row.get('Invoice Number'),
            invoice_date=invoice_date,
            state=row.get('State'),
            comments=row.get('Comments'),
            column1=row.get('Column1'),
            column2=row.get('Column2')
        )

    # Assignment rows
    if row.get('Assigned to') and current_asset:
        Assignment.objects.create(
            asset=current_asset,
            assigned_to=row.get('Assigned to')
        )

print("Data Imported Successfully")
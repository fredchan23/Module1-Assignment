#!/usr/bin/env python3
"""
Convert CSV to Parquet format for efficient storage and loading.
Parquet format reduces file size by ~70-80% and loads faster in Streamlit.
"""

import pandas as pd
import os

def convert_csv_to_parquet():
    csv_file = 'SGJobData_cleaned.csv'
    parquet_file = 'SGJobData_cleaned.parquet'
    
    print(f"Reading {csv_file}...")
    print(f"Original size: {os.path.getsize(csv_file) / (1024**2):.1f} MB")
    
    # Read CSV
    df = pd.read_csv(csv_file)
    print(f"Loaded {len(df):,} rows × {len(df.columns)} columns")

    # Apply salary outlier filter (mirrors salary_insights_dashboard.ipynb Section 2)
    # salary_minimum < 1200: below Singapore Progressive Wage Model / LQS floor
    # salary_maximum > 30,000: annual salaries mistakenly entered in monthly fields
    rows_before = len(df)
    df = df[
        (df['salary_minimum'] >= 1200) &
        (df['salary_maximum'] <= 30_000)
    ].copy()
    rows_dropped = rows_before - len(df)
    print(f"Salary outliers dropped: {rows_dropped:,} rows ({rows_dropped/rows_before*100:.2f}%)")
    print(f"Clean rows for export: {len(df):,}")

    # Save as Parquet with compression
    print(f"\nConverting to Parquet format...")
    df.to_parquet(parquet_file, engine='pyarrow', compression='snappy', index=False)
    
    # Show compression results
    parquet_size = os.path.getsize(parquet_file) / (1024**2)
    csv_size = os.path.getsize(csv_file) / (1024**2)
    reduction = (1 - parquet_size/csv_size) * 100
    
    print(f"\n✓ Conversion complete!")
    print(f"Parquet size: {parquet_size:.1f} MB")
    print(f"Size reduction: {reduction:.1f}%")
    print(f"Saved as: {parquet_file}")
    
    # Verify data integrity
    print("\nVerifying data integrity...")
    df_parquet = pd.read_parquet(parquet_file)
    assert len(df) == len(df_parquet), "Row count mismatch!"
    assert list(df.columns) == list(df_parquet.columns), "Column mismatch!"
    print("✓ Data integrity verified")

if __name__ == '__main__':
    convert_csv_to_parquet()

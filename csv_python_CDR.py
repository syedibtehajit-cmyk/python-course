import pandas as pd

# File paths (aapke Desktop ke path use karte hue)
call_report = "C:/Users/IbtehaJ IT/Desktop/call-report_2026-08-17_to_2026-08-22.csv"
cdr_report = "C:/Users/IbtehaJ IT/Desktop/CDR_Report_2026-08-17_to_2026-08-22.csv"

# Load CSV files
df_call = pd.read_csv(call_report)
df_cdr = pd.read_csv(cdr_report)

# Total counts
print("Total records in Call Report:", len(df_call))
print("Total records in CDR Report:", len(df_cdr))

# Unique key column
key = "srno"

# Records missing in Call Report
missing_in_call = df_cdr[~df_cdr[key].isin(df_call[key])]
missing_in_call.to_csv("C:/Users/IbtehaJ IT/Desktop/missing_in_call_report.csv", index=False)

# Records missing in CDR Report
missing_in_cdr = df_call[~df_call[key].isin(df_cdr[key])]
missing_in_cdr.to_csv("C:/Users/IbtehaJ IT/Desktop/missing_in_cdr_report.csv", index=False)

# Print summary
print("Missing in Call Report:", len(missing_in_call))
print("Missing in CDR Report:", len(missing_in_cdr))

# Show missing srno list
print("Missing srno in Call Report:\n", missing_in_call[key].tolist())
print("Missing srno in CDR Report:\n", missing_in_cdr[key].tolist())

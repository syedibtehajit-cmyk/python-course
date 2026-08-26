import pandas as pd
from collections import Counter, defaultdict

# ============================================================
# File paths (apne Desktop ke path use kar rahe hain)
# ============================================================
call_report_path = "C:/Users/IbtehaJ IT/Desktop/call-report_2026-08-17_to_2026-08-22.csv"
cdr_report_path  = "C:/Users/IbtehaJ IT/Desktop/CDR_Report_2026-08-17_to_2026-08-22.csv"

out_missing_in_call = "C:/Users/IbtehaJ IT/Desktop/missing_in_call_report.csv"
out_missing_in_cdr  = "C:/Users/IbtehaJ IT/Desktop/missing_in_cdr_report.csv"

# ============================================================
# Load files (dtype=str taake numbers/leading zeros distort na hon)
# ============================================================
df_call = pd.read_csv(call_report_path, dtype=str, keep_default_na=False)
df_cdr  = pd.read_csv(cdr_report_path,  dtype=str, keep_default_na=False)

print("Total records in Call Report:", len(df_call))
print("Total records in CDR Report:", len(df_cdr))

# ============================================================
# Helper: time ko "YYYY-MM-DD H:MM" format mein normalize karo
# (srno IGNORE - kyunke wo sirf row-number hai, call ki identity nahi)
# ============================================================
def normalize_time(dt_str, sep):
    date_part, time_part = dt_str.split(sep)
    date_part = date_part.strip()[:10]          # sirf date (YYYY-MM-DD)
    h, m = time_part.strip()[:5].split(':')[:2]
    return f"{date_part} {int(h)}:{m}"

def last10(num_str):
    digits = ''.join(ch for ch in str(num_str) if ch.isdigit())
    return digits[-10:] if len(digits) >= 10 else digits

# ============================================================
# Call Report se matching key banao
# Columns: Date/Time, Extension, Agent, Destination, Duration (s),
#          Talk Time (s), Status, ...
# ============================================================
def call_report_key(row):
    dt_norm = normalize_time(row['Date/Time'].replace('T', ' ').replace('Z', ''), ' ')
    dst = last10(row['Destination'])
    return (dt_norm, dst, row['Duration (s)'], row['Talk Time (s)'], row['Status'], row['Extension'])

# ============================================================
# CDR Report se matching key banao
# Columns: calldate, src, dst, lastapp, duration, billsec, disposition, cnum, cnam
# ============================================================
def cdr_report_key(row):
    dt_norm = normalize_time(row['calldate'], ' ')
    dst = last10(row['dst'])
    return (dt_norm, dst, row['duration'], row['billsec'], row['disposition'], row['cnum'])

# ============================================================
# Har row ke liye key nikaalo, Counter aur map banao
# (Counter isliye taake duplicate/identical calls bhi sahi handle hon)
# ============================================================
call_counter = Counter()
call_map = defaultdict(list)
for idx, row in df_call.iterrows():
    k = call_report_key(row)
    call_counter[k] += 1
    call_map[k].append(idx)

cdr_counter = Counter()
cdr_map = defaultdict(list)
for idx, row in df_cdr.iterrows():
    k = cdr_report_key(row)
    cdr_counter[k] += 1
    cdr_map[k].append(idx)

# ============================================================
# CDR mein hain lekin Call Report mein missing (ya kam count) hain
# ============================================================
missing_in_call_idx = []
for k, cnt in cdr_counter.items():
    call_cnt = call_counter.get(k, 0)
    if cnt > call_cnt:
        diff = cnt - call_cnt
        missing_in_call_idx.extend(cdr_map[k][:diff])

# ============================================================
# Call Report mein hain lekin CDR mein missing (ya kam count) hain
# ============================================================
missing_in_cdr_idx = []
for k, cnt in call_counter.items():
    cdr_cnt = cdr_counter.get(k, 0)
    if cnt > cdr_cnt:
        diff = cnt - cdr_cnt
        missing_in_cdr_idx.extend(call_map[k][:diff])

missing_in_call = df_cdr.loc[missing_in_call_idx]
missing_in_cdr  = df_call.loc[missing_in_cdr_idx]

# ============================================================
# Save raw rows (poora original data, bina kisi column drop kiye)
# ============================================================
missing_in_call.to_csv(out_missing_in_call, index=False)
missing_in_cdr.to_csv(out_missing_in_cdr, index=False)

# ============================================================
# Summary
# ============================================================
print("\nRows present in CDR but MISSING from Call Report:", len(missing_in_call))
print("Rows present in Call Report but MISSING from CDR:", len(missing_in_cdr))
print("\nSaved:")
print(" -", out_missing_in_call)
print(" -", out_missing_in_cdr)
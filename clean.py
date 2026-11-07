# Takes the two raw BLS files and makes one tidy csv with my 12 occupations.
# Run collect.py first.

import zipfile

import pandas as pd

# the 12 occupations I picked, spread across a few fields students actually go into
OCCUPATIONS = {
    "15-1252": "Software Developers",
    "15-2051": "Data Scientists",
    "15-1212": "Information Security Analysts",
    "11-3021": "Computer and Information Systems Managers",
    "13-2011": "Accountants and Auditors",
    "13-2051": "Financial and Investment Analysts",
    "13-1111": "Management Analysts",
    "11-2021": "Marketing Managers",
    "27-3031": "Public Relations Specialists",
    "29-1141": "Registered Nurses",
    "17-2051": "Civil Engineers",
    "25-2021": "Elementary School Teachers",
}

# --- wages, from the OEWS zip ---
with zipfile.ZipFile("data/raw/oesm25nat.zip") as z:
    inner = [n for n in z.namelist() if n.endswith(".xlsx")][0]
    wages = pd.read_excel(z.open(inner))

wages = wages[["OCC_CODE", "OCC_TITLE", "TOT_EMP", "A_MEDIAN"]]

# --- projections, from the Employment Projections workbook ---
proj = pd.read_excel("data/raw/occupation.xlsx", sheet_name="Table 1.2", header=1)
proj = proj.rename(columns={
    "2025 National Employment Matrix code": "OCC_CODE",
    "Employment change, percent, 2025–35": "growth_pct",
    "Occupational openings, 2025–35 annual average": "annual_openings",
    "Typical education needed for entry": "education",
})
proj = proj[["OCC_CODE", "growth_pct", "annual_openings", "education"]]

# --- join them on the occupation code ---
df = wages.merge(proj, on="OCC_CODE", how="inner")
df = df[df["OCC_CODE"].isin(OCCUPATIONS)].copy()
df["occupation"] = df["OCC_CODE"].map(OCCUPATIONS)

# everything comes out of excel as text sometimes, so force the numbers to be numbers
df["median_wage"] = pd.to_numeric(df["A_MEDIAN"], errors="coerce")
df["employment"] = pd.to_numeric(df["TOT_EMP"], errors="coerce")
df["growth_pct"] = pd.to_numeric(df["growth_pct"], errors="coerce")
df["annual_openings"] = pd.to_numeric(df["annual_openings"], errors="coerce")

tidy = df[["OCC_CODE", "occupation", "median_wage", "employment",
           "growth_pct", "annual_openings", "education"]]
tidy = tidy.rename(columns={"OCC_CODE": "soc_code"}).sort_values("median_wage", ascending=False)

tidy.to_csv("data/careers_clean.csv", index=False)

print("rows:", len(tidy), "of", len(OCCUPATIONS), "I asked for")
print("missing values per column:")
print(tidy.isna().sum().to_string())
print()
print(tidy.to_string(index=False))

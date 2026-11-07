# Downloads the two BLS files I need and saves them in data/raw.
# Run this first, then run clean.py.

import os
import time

import requests

# Say who I am, like chapter 2 said to
HEADERS = {"User-Agent": "WebDataScience/1.0 (INFO 4617; haab1186@colorado.edu)"}

FILES = {
    # median annual wages by occupation (OEWS, May 2025)
    "oesm25nat.zip": "https://www.bls.gov/oes/special-requests/oesm25nat.zip",
    # employment projections 2025-2035, openings, and education (Employment Projections)
    "occupation.xlsx": "https://www.bls.gov/emp/ind-occ-matrix/occupation.xlsx",
}

os.makedirs("data/raw", exist_ok=True)

for name, url in FILES.items():
    path = os.path.join("data", "raw", name)

    if os.path.exists(path):
        print("already downloaded, skipping:", name)
        continue

    response = requests.get(url, headers=HEADERS, timeout=120)
    print(name, "->", response.status_code, "|", len(response.content), "bytes")
    response.raise_for_status()

    with open(path, "wb") as f:
        f.write(response.content)

    time.sleep(2)   # pause so I'm not hammering BLS

print("done")

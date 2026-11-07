# Which Careers Offer the Best Combination of Pay and Growth?

Hamza Abulaila
INFO 4617 Web Data Science, CU Boulder

## About this project

Most people look at salary when they pick a career, but that doesn't tell you if the job will
actually be there later. For this project I'm looking at 12 occupations that college students
might realistically go into, and comparing the median annual wage for each one against how much
the job is projected to grow and how many openings it has each year from 2025 to 2035. The data
comes from two public BLS datasets that I'll join on occupation codes. I don't think the highest
paying jobs will also be the fastest growing ones, and that's basically what I want to find out.

## Data

Both files come from the U.S. Bureau of Labor Statistics and I downloaded them on **November 7, 2026** by running `collect.py`:

- **Occupational Employment and Wage Statistics (OEWS), May 2025** - median annual wages and how many people have each job. <https://www.bls.gov/oes/special-requests/oesm25nat.zip>
- **Employment Projections, Table 1.2** - projected growth from 2025 to 2035, average annual openings, and the education you typically need. <https://www.bls.gov/emp/ind-occ-matrix/occupation.xlsx>

`clean.py` joins the two on the SOC occupation code and pulls out the 12 occupations I picked. The cleaned file is `data/careers_clean.csv`, **12 rows**, and all 12 matched with no missing values. Fields are explained in `data/README.md`.

What I left out: the raw downloads in `data/raw/` are gitignored. They're about 700 KB of BLS spreadsheets covering every occupation in the country, and I only need 12 rows of it, so there's no reason to commit the whole thing when `collect.py` re-downloads it in a few seconds. There's no personal information in any of this, since BLS reports occupation-level totals and not individual people.

## Methods

TODO - how I picked the 12 occupations and how I joined the two datasets.

## Findings

TODO - the scatterplot and the rankings.

## How to reproduce

TODO - what to install and what order to run things in.

# data

- `careers_clean.csv` is the cleaned dataset, 12 rows, one per occupation. Made by `clean.py`.
- `raw/` has the two files straight from BLS. It's gitignored, run `collect.py` to get them.

## Data dictionary

| Field | What it means |
|---|---|
| `soc_code` | The occupation's SOC code, like `15-1252`. This is what I joined the two BLS files on. |
| `occupation` | My short name for the occupation. |
| `median_wage` | Median annual wage in dollars, May 2025, from OEWS. Half the people in the job make more than this, half make less. |
| `employment` | How many people had this job nationally, May 2025, from OEWS. |
| `growth_pct` | Projected percent change in employment from 2025 to 2035, from Employment Projections. Can be negative. |
| `annual_openings` | Average job openings per year from 2025 to 2035, in thousands. Includes people leaving the job, not just new positions. |
| `education` | The education BLS says you typically need to get into the job. |

Two things to keep in mind. `annual_openings` is in thousands, so 95.3 means about 95,300 openings a year. And the growth numbers are projections, not promises, so I shouldn't write about them like they're guaranteed.

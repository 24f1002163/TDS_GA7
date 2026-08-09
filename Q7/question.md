Below is a snapshot of a search index (180 documents). Write one query that returns exactly the 9 target URLs listed underneath — every target, and nothing else.

You are not told which properties make the targets special. Work that out by comparing them against the rest of the index. Several documents differ from a target in exactly one respect, so a nearly right query will pull them in.

Supported tokens (all tokens are ANDed together):

site:HOST        filetype:EXT     inurl:TEXT     intitle:TEXT    intext:TEXT
after:YYYY       before:YYYY      "exact phrase"                 bareTerm
prefix any token with - to negate it
(tokenA OR tokenB)   one level of OR grouping, counts as one token
site: matches the host itself or any subdomain of it.
after:/before: are strict (after:2020 excludes 2020).
A bare term matches the title or the body. All matching is case-insensitive substring matching.
Limit: 6 tokens. Listing the target URLs one by one will not fit.
Target URLs (9)
https://civicdata.example/notices/audit-220.pdf
https://civicdata.example/open-data/audit-919.pdf
https://civicdata.example/reports/audit-845.pdf
https://data.civicdata.example/archive/audit-425.pdf
https://data.civicdata.example/notices/audit-511.pdf
https://data.civicdata.example/reports/audit-520.pdf
https://docs.civicdata.example/notices/audit-609.pdf
https://docs.civicdata.example/reports/audit-263.pdf
https://docs.civicdata.example/reports/audit-963.pdf
The index

[
 {
  "url": "https://civicdata.example/reports/audit-845.pdf",
  "host": "civicdata.example",
  "title": "District audit summary 7",
  "body": "Prepared for review. Contains the tender evaluation notes for the period.",
  "filetype": "pdf",
  "year": 2020
 },
 {
  "url": "https://civicdata.example/notices/audit-220.pdf",
  "host": "civicdata.example",
  "title": "District audit summary 2",
  "body": "Prepared for review. Contains the tender evaluation notes for the period.",
  "filetype": "pdf",
  "year": 2023
 },
 {
  "url": "https://data.civicdata.example/reports/audit-520.pdf",
  "host": "data.civicdata.example",
  "title": "District audit summary 36",
  "body": "Prepared for review. Contains the tender evaluation notes for the period.",
  "filetype": "pdf",
  "year": 2025
 },
 {
  "url": "https://docs.civicdata.example/notices/audit-609.pdf",
  "host": "docs.civicdata.example",
  "title": "District audit summary 38",
  "body": "Prepared for review. Contains the tender evaluation notes for the period.",
  "filetype": "pdf",
  "year": 2022
 },
 {
  "url": "https://docs.civicdata.example/reports/audit-963.pdf",
  "host": "docs.civicdata.example",
  "title": "District audit summary 4",
  "body": "Prepared for review. Contains the tender evaluation notes for the period.",
  "filetype": "pdf",
  "year": 2021
 },
 {
  "url": "https://data.civicdata.example/notices/audit-511.pdf",
  "host": "data.civicdata.example",
  "title": "District audit summary 27",
  "body": "Prepared for review. Contains the tender evaluation notes for the period.",
  "filetype": "pdf",
  "year": 2021
 },
 {
  "url": "https://data.civicdata.example/archive/audit-425.pdf",
  "host": "data.civicdata.example",
  "title": "District audit summary 10",
  "body": "Prepared for review. Contains the tender evaluation notes for the period.",
  "filetype": "pdf",
  "year": 2025
 },
 {
  "url": "https://docs.civicdata.example/reports/audit-263.pdf",
  "host": "docs.civicdata.example",
  "title": "District audit summary 37",
  "body": "Prepared for review. Contains the tender evaluation notes for the period.",
  "filetype": "pdf",
  "year": 2023
 },
 {
  "url": "https://civicdata.example/open-data/audit-919.pdf",
  "host": "civicdata.example",
  "title": "District audit summary 2",
  "body": "Prepared for review. Contains the tender evaluation notes for the period.",
  "filetype": "pdf",
  "year": 2024
 },
 {
  "url": "https://legacy.civicdata.example/notices/audit-3736.html",
  "host": "legacy.civicdata.example",
  "title": "District audit summary 42",
  "body": "Prepared for review. Contains the tender evaluation notes for the period.",
  "filetype": "html",
  "year": 2021
 },
 {
  "url": "https://docs.civicdata.example/reports/audit-5167.pdf",
  "host": "docs.civicdata.example",
  "title": "District audit summary 79",
  "body": "Prepared for review. Contains the tender evaluation notes for the period.",
  "filetype": "pdf",
  "year": 2019
 },
 {
  "url": "https://data.civicdata.example/reports/audit-6245.pdf",
  "host": "data.civicdata.example",
  "title": "District summary 16",
  "body": "Prepared for review. Contains the tender evaluation notes for the period.",
  "filetype": "pdf",
  "year": 2026
 },
 {
  "url": "https://legacy.civicdata.example/open-data/audit-2208.pdf",
  "host": "legacy.civicdata.example",
  "title": "District audit summary 62",
  "body": "Prepared for review. Contains the tender totals only.",
  "filetype": "pdf",
  "year": 2024
 },
 {
  "url": "https://legacy.civicdata.example/drafts/audit-7843.pdf",
  "host": "legacy.civicdata.example",
  "title": "District audit summary 73",
  "body": "Prepared for review. Contains the tender evaluation notes for the period.",
  "filetype": "pdf",
  "year": 2021
 },
 {
  "url": "https://mirror.civicdata-cdn.example/archive/audit-6859.pdf",
  "host": "mirror.civicdata-cdn.example",
  "title": "District audit summary 81",
  "body": "Prepared for review. Contains the tender evaluation notes for the period.",
  "filetype": "pdf",
  "year": 2026
 },
 {
  "url": "https://legacy.civicdata.example/drafts/audit-3321.pdf",
  "host": "legacy.civicdata.example",
  "title": "District audit summary 69",
  "body": "Prepared for review. Contains the tender evaluation notes for the period.",
  "filetype": "pdf",
  "year": 2021
 },
 {
  "url": "https://data.civicdata.example/notices/audit-6871.csv",
  "host": "data.civicdata.example",
  "title": "District audit summary 73",
  "body": "Prepared for review. Contains the tender evaluation notes for the period.",
  "filetype": "csv",
  "year": 2024
 },
 {
  "url": "https://docs.civicdata.example/reports/audit-3628.pdf",
  "host": "docs.civicdata.example",
  "title": "District audit summary 92",
  "body": "Prepared for review. Contains the tender evaluation notes for the period.",
  "filetype": "pdf",
  "year": 2019
 },
 {
  "url": "https://docs.civicdata.example/notices/audit-5699.pdf",
  "host": "docs.civicdata.example",
  "title": "District summary 20",
  "body": "Prepared for review. Contains the tender evaluation notes for the period.",
  "filetype": "pdf",
  "year": 2026
 },
 {
  "url": "https://data.civicdata.example/notices/audit-2816.pdf",
  "host": "data.civicdata.example",
  "title": "District audit summary 67",
  "body": "Prepared for review. Contains the tender totals only.",
  "filetype": "pdf",
  "year": 2023
 },
 {
  "url": "https://docs.civicdata.example/drafts/audit-3291.pdf",
  "host": "docs.civicdata.example",
  "title": "District audit summary 57",
  "body": "Prepared for review. Contains the tender evaluation notes for the period.",
  "filetype": "pdf",
  "year": 2026
 },
 {
  "url": "https://mirror.civicdata-cdn.example/archive/audit-4136.pdf",
  "host": "mirror.civicdata-cdn.example",
  "title": "District audit summary 47",
  "body": "Prepared for review. Contains the tender evaluation notes for the period.",
  "filetype": "pdf",
  "year": 2024
 },
 {
  "url": "https://legacy.civicdata.example/drafts/audit-9914.pdf",
  "host": "legacy.civicdata.example",
  "title": "District audit summary 45",
  "body": "Prepared for review. Contains the tender evaluation notes for the period.",
  "filetype": "pdf",
  "year": 2020
 },
 {
  "url": "https://legacy.civicdata.example/archive/audit-5608.csv",
  "host": "legacy.civicdata.example",
  "title": "District audit summary 52",
  "body": "Prepared for review. Contains the tender evaluation notes for the period.",
  "filetype": "csv",
  "year": 2023
 },
 {
  "url": "https://civicdata.example/notices/audit-7027.pdf",
  "host": "civicdata.example",
  "title": "District audit summary 49",
  "body": "Prepared for review. Contains the tender evaluation notes for the period.",
  "filetype": "pdf",
  "year": 2017
 },
 {
  "url": "https://legacy.civicdata.example/archive/audit-9200.pdf",
  "host": "legacy.civicdata.example",
  "title": "District summary 20",
  "body": "Prepared for review. Contains the tender evaluation notes for the period.",
  "filetype": "pdf",
  "year": 2020
 },
 {
  "url": "https://docs.civicdata.example/archive/audit-3572.pdf",
  "host": "docs.civicdata.example",
  "title": "District audit summary 83",
  "body": "Prepared for review. Contains the tender totals only.",
  "filetype": "pdf",
  "year": 2022
 },
 {
  "url": "https://docs.civicdata.example/drafts/audit-4802.pdf",
  "host": "docs.civicdata.example",
  "title": "District audit summary 77",
  "body": "Prepared for review. Contains the tender evaluation notes for the period.",
  "filetype": "pdf",
  "year": 2020
 },
 {
  "url": "https://mirror.civicdata-cdn.example/open-data/audit-5139.pdf",
  "host": "mirror.civicdata-cdn.example",
  "title": "District audit summary 53",
  "body": "Prepared for review. Contains the tender evaluation notes for the period.",
  "filetype": "pdf",
  "year": 2022
 },
 {
  "url": "https://legacy.civicdata.example/drafts/audit-2795.pdf",
  "host": "legacy.civicdata.example",
  "title": "District audit summary 91",
  "body": "Prepared for review. Contains the tender evaluation notes for the period.",
  "filetype": "pdf",
  "year": 2024
 },
 {
  "url": "https://civicdata.example/archive/audit-7168.html",
  "host": "civicdata.example",
  "title": "District audit summary 95",
  "body": "Prepared for review. Contains the tender evaluation notes for the period.",
  "filetype": "html",
  "year": 2020
 },
 {
  "url": "https://docs.civicdata.example/notices/audit-4301.pdf",
  "host": "docs.civicdata.example",
  "title": "District audit summary 46",
  "body": "Prepared for review. Contains the tender evaluation notes for the period.",
  "filetype": "pdf",
  "year": 2018
 },
 {
  "url": "https://docs.civicdata.example/reports/audit-7606.pdf",
  "host": "docs.civicdata.example",
  "title": "District summary 33",
  "body": "Prepared for review. Contains the tender evaluation notes for the period.",
  "filetype": "pdf",
  "year": 2022
 },
 {
  "url": "https://docs.civicdata.example/notices/audit-1782.pdf",
  "host": "docs.civicdata.example",
  "title": "District audit summary 85",
  "body": "Prepared for review. Contains the tender totals only.",
  "filetype": "pdf",
  "year": 2025
 },
 {
  "url": "https://legacy.civicdata.example/drafts/audit-2488.pdf",
  "host": "legacy.civicdata.example",
  "title": "District audit summary 46",
  "body": "Prepared for review. Contains the tender evaluation notes for the period.",
  "filetype": "pdf",
  "year": 2023
 },
 {
  "url": "https://mirror.civicdata-cdn.example/notices/audit-9316.pdf",
  "host": "mirror.civicdata-cdn.example",
  "title": "District audit summary 95",
  "body": "Prepared for review. Contains the tender evaluation notes for the period.",
  "filetype": "pdf",
  "year": 2020
 },
 {
  "url": "https://legacy.civicdata.example/drafts/audit-8945.pdf",
  "host": "legacy.civicdata.example",
  "title": "District audit summary 59",
  "body": "Prepared for review. Contains the tender evaluation notes for the period.",
  "filetype": "pdf",
  "year": 2020
 },
 {
  "url": "https://legacy.civicdata.example/open-data/audit-6189.csv",
  "host": "legacy.civicdata.example",
  "title": "District audit summary 77",
  "body": "Prepared for review. Contains the tender evaluation notes for the period.",
  "filetype": "csv",
  "year": 2023
 },
 {
  "url": "https://data.civicdata.example/reports/audit-2608.pdf",
  "host": "data.civicdata.example",
  "title": "District audit summary 73",
  "body": "Prepared for review. Contains the tender evaluation notes for the period.",
  "filetype": "pdf",
  "year": 2019
 },
 {
  "url": "https://data.civicdata.example/reports/audit-7704.pdf",
  "host": "data.civicdata.example",
  "title": "District summary 32",
  "body": "Prepared for review. Contains the tender evaluation notes for the period.",
  "filetype": "pdf",
  "year": 2020
 },
 {
  "url": "https://docs.civicdata.example/archive/audit-5565.pdf",
  "host": "docs.civicdata.example",
  "title": "District audit summary 59",
  "body": "Prepared for review. Contains the tender totals only.",
  "filetype": "pdf",
  "year": 2026
 },
 {
  "url": "https://data.civicdata.example/drafts/audit-1351.pdf",
  "host": "data.civicdata.example",
  "title": "District audit summary 89",
  "body": "Prepared for review. Contains the tender evaluation notes for the period.",
  "filetype": "pdf",
  "year": 2025
 },
 {
  "url": "https://mirror.civicdata-cdn.example/archive/audit-2814.pdf",
  "host": "mirror.civicdata-cdn.example",
  "title": "District audit summary 95",
  "body": "Prepared for review. Contains the tender evaluation notes for the period.",
  "filetype": "pdf",
  "year": 2024
 },
 {
  "url": "https://legacy.civicdata.example/drafts/audit-1452.pdf",
  "host": "legacy.civicdata.example",
  "title": "District audit summary 78",
  "body": "Prepared for review. Contains the tender evaluation notes for the period.",
  "filetype": "pdf",
  "year": 2023
 },
 {
  "url": "https://docs.civicdata.example/notices/audit-1657.xlsx",
  "host": "docs.civicdata.example",
  "title": "District audit summary 62",
  "body": "Prepared for review. Contains the tender evaluation notes for the period.",
  "filetype": "xlsx",
  "year": 2026
 },
 {
  "url": "https://civicdata.example/notices/audit-5453.pdf",
  "host": "civicdata.example",
  "title": "District audit summary 85",
  "body": "Prepared for review. Contains the tender evaluation notes for the period.",
  "filetype": "pdf",
  "year": 2018
 },
 {
  "url": "https://docs.civicdata.example/open-data/audit-9138.pdf",
  "host": "docs.civicdata.example",
  "title": "District summary 5",
  "body": "Prepared for review. Contains the tender evaluation notes for the period.",
  "filetype": "pdf",
  "year": 2025
 },
 {
  "url": "https://docs.civicdata.example/notices/audit-1547.pdf",
  "host": "docs.civicdata.example",
  "title": "District audit summary 97",
  "body": "Prepared for review. Contains the tender totals only.",
  "filetype": "pdf",
  "year": 2022
 },
 {
  "url": "https://legacy.civicdata.example/drafts/audit-3521.pdf",
  "host": "legacy.civicdata.example",
  "title": "District audit summary 94",
  "body": "Prepared for review. Contains the tender evaluation notes for the period.",
  "filetype": "pdf",
  "year": 2023
 },
 {
  "url": "https://mirror.civicdata-cdn.example/notices/audit-5406.pdf",
  "host": "mirror.civicdata-cdn.example",
  "title": "District audit summary 62",
  "body": "Prepared for review. Contains the tender evaluation notes for the period.",
  "filetype": "pdf",
  "year": 2021
 },
 {
  "url": "https://legacy.civicdata.example/drafts/audit-9274.pdf",
  "host": "legacy.civicdata.example",
  "title": "District audit summary 53",
  "body": "Prepared for review. Contains the tender evaluation notes for the period.",
  "filetype": "pdf",
  "year": 2025
 },
 {
  "url": "https://legacy.civicdata.example/reports/audit-7914.html",
  "host": "legacy.civicdata.example",
  "title": "District audit summary 66",
  "body": "Prepared for review. Contains the tender evaluation notes for the period.",
  "filetype": "html",
  "year": 2025
 },
 {
  "url": "https://civicdata.example/notices/audit-6455.pdf",
  "host": "civicdata.example",
  "title": "District audit summary 83",
  "body": "Prepared for review. Contains the tender evaluation notes for the period.",
  "filetype": "pdf",
  "year": 2018
 },
 {
  "url": "https://data.civicdata.example/notices/audit-4113.pdf",
  "host": "data.civicdata.example",
  "title": "District summary 5",
  "body": "Prepared for review. Contains the tender evaluation notes for the period.",
  "filetype": "pdf",
  "year": 2020
 },
 {
  "url": "https://legacy.civicdata.example/notices/audit-2946.pdf",
  "host": "legacy.civicdata.example",
  "title": "District audit summary 48",
  "body": "Prepared for review. Contains the tender totals only.",
  "filetype": "pdf",
  "year": 2021
 },
 {
  "url": "https://legacy.civicdata.example/drafts/audit-3504.pdf",
  "host": "legacy.civicdata.example",
  "title": "District audit summary 84",
  "body": "Prepared for review. Contains the tender evaluation notes for the period.",
  "filetype": "pdf",
  "year": 2020
 },
 {
  "url": "https://mirror.civicdata-cdn.example/open-data/audit-8916.pdf",
  "host": "mirror.civicdata-cdn.example",
  "title": "District audit summary 82",
  "body": "Prepared for review. Contains the tender evaluation notes for the period.",
  "filetype": "pdf",
  "year": 2021
 },
 {
  "url": "https://legacy.civicdata.example/drafts/audit-7136.pdf",
  "host": "legacy.civicdata.example",
  "title": "District audit summary 67",
  "body": "Prepared for review. Contains the tender evaluation notes for the period.",
  "filetype": "pdf",
  "year": 2021
 },
 {
  "url": "https://docs.civicdata.example/open-data/audit-2296.html",
  "host": "docs.civicdata.example",
  "title": "District audit summary 43",
  "body": "Prepared for review. Contains the tender evaluation notes for the period.",
  "filetype": "html",
  "year": 2022
 },
 {
  "url": "https://data.civicdata.example/open-data/audit-6109.pdf",
  "host": "data.civicdata.example",
  "title": "District audit summary 93",
  "body": "Prepared for review. Contains the tender evaluation notes for the period.",
  "filetype": "pdf",
  "year": 2018
 },
 {
  "url": "https://legacy.civicdata.example/reports/audit-2880.pdf",
  "host": "legacy.civicdata.example",
  "title": "District summary 33",
  "body": "Prepared for review. Contains the tender evaluation notes for the period.",
  "filetype": "pdf",
  "year": 2024
 },
 {
  "url": "https://civicdata.example/archive/audit-6960.pdf",
  "host": "civicdata.example",
  "title": "District audit summary 85",
  "body": "Prepared for review. Contains the tender totals only.",
  "filetype": "pdf",
  "year": 2020
 },
 {
  "url": "https://civicdata.example/drafts/audit-2610.pdf",
  "host": "civicdata.example",
  "title": "District audit summary 61",
  "body": "Prepared for review. Contains the tender evaluation notes for the period.",
  "filetype": "pdf",
  "year": 2021
 },
 {
  "url": "https://mirror.civicdata-cdn.example/open-data/audit-2904.pdf",
  "host": "mirror.civicdata-cdn.example",
  "title": "District audit summary 73",
  "body": "Prepared for review. Contains the tender evaluation notes for the period.",
  "filetype": "pdf",
  "year": 2022
 },
 {
  "url": "https://legacy.civicdata.example/drafts/audit-3127.pdf",
  "host": "legacy.civicdata.example",
  "title": "District audit summary 74",
  "body": "Prepared for review. Contains the tender evaluation notes for the period.",
  "filetype": "pdf",
  "year": 2021
 },
 {
  "url": "https://legacy.civicdata.example/archive/audit-9757.xlsx",
  "host": "legacy.civicdata.example",
  "title": "District audit summary 85",
  "body": "Prepared for review. Contains the tender evaluation notes for the period.",
  "filetype": "xlsx",
  "year": 2021
 },
 {
  "url": "https://docs.civicdata.example/open-data/audit-4368.pdf",
  "host": "docs.civicdata.example",
  "title": "District audit summary 47",
  "body": "Prepared for review. Contains the tender evaluation notes for the period.",
  "filetype": "pdf",
  "year": 2017
 },
 {
  "url": "https://docs.civicdata.example/reports/audit-9308.pdf",
  "host": "docs.civicdata.example",
  "title": "District summary 1",
  "body": "Prepared for review. Contains the tender evaluation notes for the period.",
  "filetype": "pdf",
  "year": 2023
 },
 {
  "url": "https://legacy.civicdata.example/open-data/audit-5120.pdf",
  "host": "legacy.civicdata.example",
  "title": "District audit summary 84",
  "body": "Prepared for review. Contains the tender totals only.",
  "filetype": "pdf",
  "year": 2020
 },
 {
  "url": "https://civicdata.example/archive/sanitation-9352.xlsx",
  "host": "civicdata.example",
  "title": "Sanitation notes 265",
  "body": "Routine sanitation record. No audit content in this document.",
  "filetype": "xlsx",
  "year": 2017
 },
 {
  "url": "https://docs.civicdata.example/drafts/minutes-6618.html",
  "host": "docs.civicdata.example",
  "title": "Minutes notes 128",
  "body": "Routine minutes record. No audit content in this document.",
  "filetype": "html",
  "year": 2022
 },
 {
  "url": "https://legacy.civicdata.example/open-data/sanitation-4207.pdf",
  "host": "legacy.civicdata.example",
  "title": "Sanitation notes 117",
  "body": "Routine sanitation record. No audit content in this document.",
  "filetype": "pdf",
  "year": 2019
 },
 {
  "url": "https://mirror.civicdata-cdn.example/drafts/budget-7386.html",
  "host": "mirror.civicdata-cdn.example",
  "title": "Budget notes 487",
  "body": "Routine budget record. No audit content in this document.",
  "filetype": "html",
  "year": 2023
 },
 {
  "url": "https://data.civicdata.example/notices/budget-5664.html",
  "host": "data.civicdata.example",
  "title": "Budget notes 893",
  "body": "Routine budget record. No audit content in this document.",
  "filetype": "html",
  "year": 2016
 },
 {
  "url": "https://civicdata.example/open-data/budget-5763.xlsx",
  "host": "civicdata.example",
  "title": "Budget notes 263",
  "body": "Routine budget record. No audit content in this document.",
  "filetype": "xlsx",
  "year": 2020
 },
 {
  "url": "https://civicdata.example/notices/minutes-7987.xlsx",
  "host": "civicdata.example",
  "title": "Minutes notes 882",
  "body": "Routine minutes record. No audit content in this document.",
  "filetype": "xlsx",
  "year": 2021
 },
 {
  "url": "https://docs.civicdata.example/drafts/minutes-6448.csv",
  "host": "docs.civicdata.example",
  "title": "Minutes notes 872",
  "body": "Routine minutes record. No audit content in this document.",
  "filetype": "csv",
  "year": 2020
 },
 {
  "url": "https://mirror.civicdata-cdn.example/notices/roster-4868.html",
  "host": "mirror.civicdata-cdn.example",
  "title": "Roster notes 179",
  "body": "Routine roster record. No audit content in this document.",
  "filetype": "html",
  "year": 2026
 },
 {
  "url": "https://civicdata.example/notices/budget-5703.html",
  "host": "civicdata.example",
  "title": "Budget notes 221",
  "body": "Routine budget record. No audit content in this document.",
  "filetype": "html",
  "year": 2021
 },
 {
  "url": "https://mirror.civicdata-cdn.example/open-data/sanitation-8560.html",
  "host": "mirror.civicdata-cdn.example",
  "title": "Sanitation notes 83",
  "body": "Routine sanitation record. No audit content in this document.",
  "filetype": "html",
  "year": 2026
 },
 {
  "url": "https://mirror.civicdata-cdn.example/notices/roster-8160.html",
  "host": "mirror.civicdata-cdn.example",
  "title": "Roster notes 255",
  "body": "Routine roster record. No audit content in this document.",
  "filetype": "html",
  "year": 2019
 },
 {
  "url": "https://civicdata.example/archive/sanitation-5406.csv",
  "host": "civicdata.example",
  "title": "Sanitation notes 172",
  "body": "Routine sanitation record. No audit content in this document.",
  "filetype": "csv",
  "year": 2020
 },
 {
  "url": "https://legacy.civicdata.example/archive/heritage-9124.xlsx",
  "host": "legacy.civicdata.example",
  "title": "Heritage notes 494",
  "body": "Routine heritage record. No audit content in this document.",
  "filetype": "xlsx",
  "year": 2025
 },
 {
  "url": "https://data.civicdata.example/archive/roster-5797.xlsx",
  "host": "data.civicdata.example",
  "title": "Roster notes 598",
  "body": "Routine roster record. No audit content in this document.",
  "filetype": "xlsx",
  "year": 2015
 },
 {
  "url": "https://legacy.civicdata.example/reports/roster-2683.xlsx",
  "host": "legacy.civicdata.example",
  "title": "Roster notes 111",
  "body": "Routine roster record. No audit content in this document.",
  "filetype": "xlsx",
  "year": 2024
 },
 {
  "url": "https://data.civicdata.example/open-data/heritage-7314.csv",
  "host": "data.civicdata.example",
  "title": "Heritage notes 309",
  "body": "Routine heritage record. No audit content in this document.",
  "filetype": "csv",
  "year": 2020
 },
 {
  "url": "https://legacy.civicdata.example/open-data/heritage-2718.xlsx",
  "host": "legacy.civicdata.example",
  "title": "Heritage notes 88",
  "body": "Routine heritage record. No audit content in this document.",
  "filetype": "xlsx",
  "year": 2025
 },
 {
  "url": "https://data.civicdata.example/open-data/minutes-7962.xlsx",
  "host": "data.civicdata.example",
  "title": "Minutes notes 621",
  "body": "Routine minutes record. No audit content in this document.",
  "filetype": "xlsx",
  "year": 2020
 },
 {
  "url": "https://mirror.civicdata-cdn.example/drafts/minutes-9213.csv",
  "host": "mirror.civicdata-cdn.example",
  "title": "Minutes notes 405",
  "body": "Routine minutes record. No audit content in this document.",
  "filetype": "csv",
  "year": 2024
 },
 {
  "url": "https://civicdata.example/notices/transport-1313.html",
  "host": "civicdata.example",
  "title": "Transport notes 635",
  "body": "Routine transport record. No audit content in this document.",
  "filetype": "html",
  "year": 2021
 },
 {
  "url": "https://legacy.civicdata.example/drafts/heritage-6846.html",
  "host": "legacy.civicdata.example",
  "title": "Heritage notes 691",
  "body": "Routine heritage record. No audit content in this document.",
  "filetype": "html",
  "year": 2017
 },
 {
  "url": "https://docs.civicdata.example/notices/budget-5742.csv",
  "host": "docs.civicdata.example",
  "title": "Budget notes 139",
  "body": "Routine budget record. No audit content in this document.",
  "filetype": "csv",
  "year": 2015
 },
 {
  "url": "https://docs.civicdata.example/reports/budget-9691.xlsx",
  "host": "docs.civicdata.example",
  "title": "Budget notes 402",
  "body": "Routine budget record. No audit content in this document.",
  "filetype": "xlsx",
  "year": 2018
 },
 {
  "url": "https://civicdata.example/archive/transport-3847.xlsx",
  "host": "civicdata.example",
  "title": "Transport notes 792",
  "body": "Routine transport record. No audit content in this document.",
  "filetype": "xlsx",
  "year": 2025
 },
 {
  "url": "https://civicdata.example/reports/heritage-7487.xlsx",
  "host": "civicdata.example",
  "title": "Heritage notes 331",
  "body": "Routine heritage record. No audit content in this document.",
  "filetype": "xlsx",
  "year": 2026
 },
 {
  "url": "https://docs.civicdata.example/open-data/heritage-6744.xlsx",
  "host": "docs.civicdata.example",
  "title": "Heritage notes 81",
  "body": "Routine heritage record. No audit content in this document.",
  "filetype": "xlsx",
  "year": 2022
 },
 {
  "url": "https://civicdata.example/drafts/transport-9344.csv",
  "host": "civicdata.example",
  "title": "Transport notes 473",
  "body": "Routine transport record. No audit content in this document.",
  "filetype": "csv",
  "year": 2020
 },
 {
  "url": "https://legacy.civicdata.example/archive/roster-9326.html",
  "host": "legacy.civicdata.example",
  "title": "Roster notes 304",
  "body": "Routine roster record. No audit content in this document.",
  "filetype": "html",
  "year": 2016
 },
 {
  "url": "https://docs.civicdata.example/drafts/sanitation-3545.xlsx",
  "host": "docs.civicdata.example",
  "title": "Sanitation notes 875",
  "body": "Routine sanitation record. No audit content in this document.",
  "filetype": "xlsx",
  "year": 2023
 },
 {
  "url": "https://mirror.civicdata-cdn.example/archive/transport-8535.pdf",
  "host": "mirror.civicdata-cdn.example",
  "title": "Transport notes 556",
  "body": "Routine transport record. No audit content in this document.",
  "filetype": "pdf",
  "year": 2020
 },
 {
  "url": "https://civicdata.example/drafts/minutes-4718.html",
  "host": "civicdata.example",
  "title": "Minutes notes 841",
  "body": "Routine minutes record. No audit content in this document.",
  "filetype": "html",
  "year": 2021
 },
 {
  "url": "https://mirror.civicdata-cdn.example/reports/budget-9958.csv",
  "host": "mirror.civicdata-cdn.example",
  "title": "Budget notes 732",
  "body": "Routine budget record. No audit content in this document.",
  "filetype": "csv",
  "year": 2022
 },
 {
  "url": "https://mirror.civicdata-cdn.example/archive/minutes-8347.xlsx",
  "host": "mirror.civicdata-cdn.example",
  "title": "Minutes notes 403",
  "body": "Routine minutes record. No audit content in this document.",
  "filetype": "xlsx",
  "year": 2021
 },
 {
  "url": "https://data.civicdata.example/open-data/transport-7987.csv",
  "host": "data.civicdata.example",
  "title": "Transport notes 201",
  "body": "Routine transport record. No audit content in this document.",
  "filetype": "csv",
  "year": 2021
 },
 {
  "url": "https://legacy.civicdata.example/open-data/sanitation-2145.pdf",
  "host": "legacy.civicdata.example",
  "title": "Sanitation notes 213",
  "body": "Routine sanitation record. No audit content in this document.",
  "filetype": "pdf",
  "year": 2025
 },
 {
  "url": "https://civicdata.example/notices/transport-7604.pdf",
  "host": "civicdata.example",
  "title": "Transport notes 563",
  "body": "Routine transport record. No audit content in this document.",
  "filetype": "pdf",
  "year": 2017
 },
 {
  "url": "https://data.civicdata.example/open-data/roster-9626.xlsx",
  "host": "data.civicdata.example",
  "title": "Roster notes 165",
  "body": "Routine roster record. No audit content in this document.",
  "filetype": "xlsx",
  "year": 2022
 },
 {
  "url": "https://data.civicdata.example/reports/heritage-9842.html",
  "host": "data.civicdata.example",
  "title": "Heritage notes 656",
  "body": "Routine heritage record. No audit content in this document.",
  "filetype": "html",
  "year": 2020
 },
 {
  "url": "https://data.civicdata.example/notices/minutes-5248.pdf",
  "host": "data.civicdata.example",
  "title": "Minutes notes 56",
  "body": "Routine minutes record. No audit content in this document.",
  "filetype": "pdf",
  "year": 2024
 },
 {
  "url": "https://data.civicdata.example/archive/minutes-3716.pdf",
  "host": "data.civicdata.example",
  "title": "Minutes notes 414",
  "body": "Routine minutes record. No audit content in this document.",
  "filetype": "pdf",
  "year": 2025
 },
 {
  "url": "https://mirror.civicdata-cdn.example/archive/minutes-4719.xlsx",
  "host": "mirror.civicdata-cdn.example",
  "title": "Minutes notes 239",
  "body": "Routine minutes record. No audit content in this document.",
  "filetype": "xlsx",
  "year": 2019
 },
 {
  "url": "https://civicdata.example/reports/sanitation-6468.xlsx",
  "host": "civicdata.example",
  "title": "Sanitation notes 694",
  "body": "Routine sanitation record. No audit content in this document.",
  "filetype": "xlsx",
  "year": 2020
 },
 {
  "url": "https://data.civicdata.example/reports/minutes-5675.xlsx",
  "host": "data.civicdata.example",
  "title": "Minutes notes 384",
  "body": "Routine minutes record. No audit content in this document.",
  "filetype": "xlsx",
  "year": 2016
 },
 {
  "url": "https://civicdata.example/drafts/heritage-5823.pdf",
  "host": "civicdata.example",
  "title": "Heritage notes 82",
  "body": "Routine heritage record. No audit content in this document.",
  "filetype": "pdf",
  "year": 2022
 },
 {
  "url": "https://civicdata.example/notices/heritage-6348.xlsx",
  "host": "civicdata.example",
  "title": "Heritage notes 568",
  "body": "Routine heritage record. No audit content in this document.",
  "filetype": "xlsx",
  "year": 2019
 },
 {
  "url": "https://legacy.civicdata.example/archive/sanitation-4558.pdf",
  "host": "legacy.civicdata.example",
  "title": "Sanitation notes 738",
  "body": "Routine sanitation record. No audit content in this document.",
  "filetype": "pdf",
  "year": 2023
 },
 {
  "url": "https://data.civicdata.example/open-data/sanitation-1680.pdf",
  "host": "data.civicdata.example",
  "title": "Sanitation notes 60",
  "body": "Routine sanitation record. No audit content in this document.",
  "filetype": "pdf",
  "year": 2026
 },
 {
  "url": "https://data.civicdata.example/notices/transport-9026.xlsx",
  "host": "data.civicdata.example",
  "title": "Transport notes 445",
  "body": "Routine transport record. No audit content in this document.",
  "filetype": "xlsx",
  "year": 2022
 },
 {
  "url": "https://legacy.civicdata.example/open-data/roster-4528.csv",
  "host": "legacy.civicdata.example",
  "title": "Roster notes 651",
  "body": "Routine roster record. No audit content in this document.",
  "filetype": "csv",
  "year": 2023
 },
 {
  "url": "https://data.civicdata.example/drafts/minutes-7939.csv",
  "host": "data.civicdata.example",
  "title": "Minutes notes 868",
  "body": "Routine minutes record. No audit content in this document.",
  "filetype": "csv",
  "year": 2025
 },
 {
  "url": "https://data.civicdata.example/archive/sanitation-7298.csv",
  "host": "data.civicdata.example",
  "title": "Sanitation notes 635",
  "body": "Routine sanitation record. No audit content in this document.",
  "filetype": "csv",
  "year": 2026
 },
 {
  "url": "https://docs.civicdata.example/open-data/sanitation-3591.csv",
  "host": "docs.civicdata.example",
  "title": "Sanitation notes 253",
  "body": "Routine sanitation record. No audit content in this document.",
  "filetype": "csv",
  "year": 2016
 },
 {
  "url": "https://data.civicdata.example/notices/roster-8500.xlsx",
  "host": "data.civicdata.example",
  "title": "Roster notes 205",
  "body": "Routine roster record. No audit content in this document.",
  "filetype": "xlsx",
  "year": 2024
 },
 {
  "url": "https://data.civicdata.example/notices/budget-3268.html",
  "host": "data.civicdata.example",
  "title": "Budget notes 93",
  "body": "Routine budget record. No audit content in this document.",
  "filetype": "html",
  "year": 2017
 },
 {
  "url": "https://docs.civicdata.example/open-data/transport-7678.pdf",
  "host": "docs.civicdata.example",
  "title": "Transport notes 640",
  "body": "Routine transport record. No audit content in this document.",
  "filetype": "pdf",
  "year": 2020
 },
 {
  "url": "https://mirror.civicdata-cdn.example/notices/roster-6229.html",
  "host": "mirror.civicdata-cdn.example",
  "title": "Roster notes 21",
  "body": "Routine roster record. No audit content in this document.",
  "filetype": "html",
  "year": 2024
 },
 {
  "url": "https://docs.civicdata.example/notices/heritage-5103.xlsx",
  "host": "docs.civicdata.example",
  "title": "Heritage notes 693",
  "body": "Routine heritage record. No audit content in this document.",
  "filetype": "xlsx",
  "year": 2024
 },
 {
  "url": "https://legacy.civicdata.example/reports/minutes-8447.html",
  "host": "legacy.civicdata.example",
  "title": "Minutes notes 337",
  "body": "Routine minutes record. No audit content in this document.",
  "filetype": "html",
  "year": 2020
 },
 {
  "url": "https://data.civicdata.example/open-data/transport-9638.pdf",
  "host": "data.civicdata.example",
  "title": "Transport notes 309",
  "body": "Routine transport record. No audit content in this document.",
  "filetype": "pdf",
  "year": 2023
 },
 {
  "url": "https://docs.civicdata.example/notices/roster-8976.html",
  "host": "docs.civicdata.example",
  "title": "Roster notes 880",
  "body": "Routine roster record. No audit content in this document.",
  "filetype": "html",
  "year": 2016
 },
 {
  "url": "https://docs.civicdata.example/open-data/transport-1696.csv",
  "host": "docs.civicdata.example",
  "title": "Transport notes 520",
  "body": "Routine transport record. No audit content in this document.",
  "filetype": "csv",
  "year": 2025
 },
 {
  "url": "https://civicdata.example/notices/heritage-9612.csv",
  "host": "civicdata.example",
  "title": "Heritage notes 331",
  "body": "Routine heritage record. No audit content in this document.",
  "filetype": "csv",
  "year": 2023
 },
 {
  "url": "https://legacy.civicdata.example/reports/heritage-7753.xlsx",
  "host": "legacy.civicdata.example",
  "title": "Heritage notes 121",
  "body": "Routine heritage record. No audit content in this document.",
  "filetype": "xlsx",
  "year": 2026
 },
 {
  "url": "https://legacy.civicdata.example/notices/transport-6899.xlsx",
  "host": "legacy.civicdata.example",
  "title": "Transport notes 33",
  "body": "Routine transport record. No audit content in this document.",
  "filetype": "xlsx",
  "year": 2015
 },
 {
  "url": "https://mirror.civicdata-cdn.example/reports/budget-9565.pdf",
  "host": "mirror.civicdata-cdn.example",
  "title": "Budget notes 400",
  "body": "Routine budget record. No audit content in this document.",
  "filetype": "pdf",
  "year": 2026
 },
 {
  "url": "https://data.civicdata.example/archive/minutes-3752.html",
  "host": "data.civicdata.example",
  "title": "Minutes notes 430",
  "body": "Routine minutes record. No audit content in this document.",
  "filetype": "html",
  "year": 2021
 },
 {
  "url": "https://mirror.civicdata-cdn.example/notices/minutes-9305.xlsx",
  "host": "mirror.civicdata-cdn.example",
  "title": "Minutes notes 477",
  "body": "Routine minutes record. No audit content in this document.",
  "filetype": "xlsx",
  "year": 2017
 },
 {
  "url": "https://mirror.civicdata-cdn.example/reports/heritage-3350.pdf",
  "host": "mirror.civicdata-cdn.example",
  "title": "Heritage notes 450",
  "body": "Routine heritage record. No audit content in this document.",
  "filetype": "pdf",
  "year": 2015
 },
 {
  "url": "https://mirror.civicdata-cdn.example/open-data/transport-3688.xlsx",
  "host": "mirror.civicdata-cdn.example",
  "title": "Transport notes 690",
  "body": "Routine transport record. No audit content in this document.",
  "filetype": "xlsx",
  "year": 2024
 },
 {
  "url": "https://data.civicdata.example/archive/sanitation-9680.xlsx",
  "host": "data.civicdata.example",
  "title": "Sanitation notes 359",
  "body": "Routine sanitation record. No audit content in this document.",
  "filetype": "xlsx",
  "year": 2017
 },
 {
  "url": "https://data.civicdata.example/reports/sanitation-4308.pdf",
  "host": "data.civicdata.example",
  "title": "Sanitation notes 134",
  "body": "Routine sanitation record. No audit content in this document.",
  "filetype": "pdf",
  "year": 2021
 },
 {
  "url": "https://civicdata.example/open-data/minutes-5365.pdf",
  "host": "civicdata.example",
  "title": "Minutes notes 375",
  "body": "Routine minutes record. No audit content in this document.",
  "filetype": "pdf",
  "year": 2024
 },
 {
  "url": "https://docs.civicdata.example/open-data/heritage-5424.html",
  "host": "docs.civicdata.example",
  "title": "Heritage notes 321",
  "body": "Routine heritage record. No audit content in this document.",
  "filetype": "html",
  "year": 2020
 },
 {
  "url": "https://legacy.civicdata.example/notices/roster-2494.html",
  "host": "legacy.civicdata.example",
  "title": "Roster notes 399",
  "body": "Routine roster record. No audit content in this document.",
  "filetype": "html",
  "year": 2026
 },
 {
  "url": "https://civicdata.example/drafts/budget-9129.html",
  "host": "civicdata.example",
  "title": "Budget notes 399",
  "body": "Routine budget record. No audit content in this document.",
  "filetype": "html",
  "year": 2019
 },
 {
  "url": "https://docs.civicdata.example/archive/heritage-1576.xlsx",
  "host": "docs.civicdata.example",
  "title": "Heritage notes 536",
  "body": "Routine heritage record. No audit content in this document.",
  "filetype": "xlsx",
  "year": 2017
 },
 {
  "url": "https://mirror.civicdata-cdn.example/drafts/heritage-5876.csv",
  "host": "mirror.civicdata-cdn.example",
  "title": "Heritage notes 35",
  "body": "Routine heritage record. No audit content in this document.",
  "filetype": "csv",
  "year": 2018
 },
 {
  "url": "https://mirror.civicdata-cdn.example/open-data/minutes-4225.csv",
  "host": "mirror.civicdata-cdn.example",
  "title": "Minutes notes 541",
  "body": "Routine minutes record. No audit content in this document.",
  "filetype": "csv",
  "year": 2017
 },
 {
  "url": "https://data.civicdata.example/archive/sanitation-8073.xlsx",
  "host": "data.civicdata.example",
  "title": "Sanitation notes 252",
  "body": "Routine sanitation record. No audit content in this document.",
  "filetype": "xlsx",
  "year": 2020
 },
 {
  "url": "https://legacy.civicdata.example/reports/sanitation-3639.xlsx",
  "host": "legacy.civicdata.example",
  "title": "Sanitation notes 242",
  "body": "Routine sanitation record. No audit content in this document.",
  "filetype": "xlsx",
  "year": 2021
 },
 {
  "url": "https://mirror.civicdata-cdn.example/notices/transport-4822.pdf",
  "host": "mirror.civicdata-cdn.example",
  "title": "Transport notes 39",
  "body": "Routine transport record. No audit content in this document.",
  "filetype": "pdf",
  "year": 2026
 },
 {
  "url": "https://legacy.civicdata.example/drafts/minutes-6088.html",
  "host": "legacy.civicdata.example",
  "title": "Minutes notes 88",
  "body": "Routine minutes record. No audit content in this document.",
  "filetype": "html",
  "year": 2015
 },
 {
  "url": "https://docs.civicdata.example/open-data/heritage-6894.pdf",
  "host": "docs.civicdata.example",
  "title": "Heritage notes 575",
  "body": "Routine heritage record. No audit content in this document.",
  "filetype": "pdf",
  "year": 2017
 },
 {
  "url": "https://civicdata.example/archive/budget-4350.xlsx",
  "host": "civicdata.example",
  "title": "Budget notes 78",
  "body": "Routine budget record. No audit content in this document.",
  "filetype": "xlsx",
  "year": 2018
 },
 {
  "url": "https://mirror.civicdata-cdn.example/notices/sanitation-3157.pdf",
  "host": "mirror.civicdata-cdn.example",
  "title": "Sanitation notes 261",
  "body": "Routine sanitation record. No audit content in this document.",
  "filetype": "pdf",
  "year": 2015
 },
 {
  "url": "https://legacy.civicdata.example/open-data/minutes-3581.pdf",
  "host": "legacy.civicdata.example",
  "title": "Minutes notes 48",
  "body": "Routine minutes record. No audit content in this document.",
  "filetype": "pdf",
  "year": 2015
 },
 {
  "url": "https://civicdata.example/notices/budget-4330.html",
  "host": "civicdata.example",
  "title": "Budget notes 601",
  "body": "Routine budget record. No audit content in this document.",
  "filetype": "html",
  "year": 2025
 },
 {
  "url": "https://docs.civicdata.example/archive/minutes-9206.html",
  "host": "docs.civicdata.example",
  "title": "Minutes notes 571",
  "body": "Routine minutes record. No audit content in this document.",
  "filetype": "html",
  "year": 2026
 },
 {
  "url": "https://legacy.civicdata.example/open-data/roster-2553.html",
  "host": "legacy.civicdata.example",
  "title": "Roster notes 774",
  "body": "Routine roster record. No audit content in this document.",
  "filetype": "html",
  "year": 2026
 },
 {
  "url": "https://legacy.civicdata.example/notices/budget-1300.xlsx",
  "host": "legacy.civicdata.example",
  "title": "Budget notes 111",
  "body": "Routine budget record. No audit content in this document.",
  "filetype": "xlsx",
  "year": 2025
 },
 {
  "url": "https://docs.civicdata.example/reports/budget-6205.xlsx",
  "host": "docs.civicdata.example",
  "title": "Budget notes 551",
  "body": "Routine budget record. No audit content in this document.",
  "filetype": "xlsx",
  "year": 2022
 },
 {
  "url": "https://docs.civicdata.example/reports/sanitation-1837.csv",
  "host": "docs.civicdata.example",
  "title": "Sanitation notes 700",
  "body": "Routine sanitation record. No audit content in this document.",
  "filetype": "csv",
  "year": 2016
 },
 {
  "url": "https://mirror.civicdata-cdn.example/drafts/budget-2283.pdf",
  "host": "mirror.civicdata-cdn.example",
  "title": "Budget notes 456",
  "body": "Routine budget record. No audit content in this document.",
  "filetype": "pdf",
  "year": 2024
 },
 {
  "url": "https://legacy.civicdata.example/archive/sanitation-9890.pdf",
  "host": "legacy.civicdata.example",
  "title": "Sanitation notes 261",
  "body": "Routine sanitation record. No audit content in this document.",
  "filetype": "pdf",
  "year": 2016
 },
 {
  "url": "https://data.civicdata.example/archive/sanitation-5076.pdf",
  "host": "data.civicdata.example",
  "title": "Sanitation notes 510",
  "body": "Routine sanitation record. No audit content in this document.",
  "filetype": "pdf",
  "year": 2021
 },
 {
  "url": "https://data.civicdata.example/open-data/budget-4991.pdf",
  "host": "data.civicdata.example",
  "title": "Budget notes 10",
  "body": "Routine budget record. No audit content in this document.",
  "filetype": "pdf",
  "year": 2026
 },
 {
  "url": "https://docs.civicdata.example/notices/heritage-7906.html",
  "host": "docs.civicdata.example",
  "title": "Heritage notes 811",
  "body": "Routine heritage record. No audit content in this document.",
  "filetype": "html",
  "year": 2020
 },
 {
  "url": "https://legacy.civicdata.example/reports/roster-9679.csv",
  "host": "legacy.civicdata.example",
  "title": "Roster notes 785",
  "body": "Routine roster record. No audit content in this document.",
  "filetype": "csv",
  "year": 2020
 },
 {
  "url": "https://docs.civicdata.example/drafts/minutes-8786.html",
  "host": "docs.civicdata.example",
  "title": "Minutes notes 83",
  "body": "Routine minutes record. No audit content in this document.",
  "filetype": "html",
  "year": 2025
 },
 {
  "url": "https://civicdata.example/archive/sanitation-2981.pdf",
  "host": "civicdata.example",
  "title": "Sanitation notes 434",
  "body": "Routine sanitation record. No audit content in this document.",
  "filetype": "pdf",
  "year": 2016
 },
 {
  "url": "https://docs.civicdata.example/archive/heritage-9235.xlsx",
  "host": "docs.civicdata.example",
  "title": "Heritage notes 568",
  "body": "Routine heritage record. No audit content in this document.",
  "filetype": "xlsx",
  "year": 2016
 },
 {
  "url": "https://docs.civicdata.example/open-data/budget-1280.pdf",
  "host": "docs.civicdata.example",
  "title": "Budget notes 527",
  "body": "Routine budget record. No audit content in this document.",
  "filetype": "pdf",
  "year": 2020
 },
 {
  "url": "https://legacy.civicdata.example/drafts/roster-2444.xlsx",
  "host": "legacy.civicdata.example",
  "title": "Roster notes 544",
  "body": "Routine roster record. No audit content in this document.",
  "filetype": "xlsx",
  "year": 2024
 },
 {
  "url": "https://mirror.civicdata-cdn.example/drafts/sanitation-5355.csv",
  "host": "mirror.civicdata-cdn.example",
  "title": "Sanitation notes 732",
  "body": "Routine sanitation record. No audit content in this document.",
  "filetype": "csv",
  "year": 2017
 },
 {
  "url": "https://legacy.civicdata.example/drafts/sanitation-3086.xlsx",
  "host": "legacy.civicdata.example",
  "title": "Sanitation notes 371",
  "body": "Routine sanitation record. No audit content in this document.",
  "filetype": "xlsx",
  "year": 2019
 },
 {
  "url": "https://mirror.civicdata-cdn.example/open-data/transport-4930.html",
  "host": "mirror.civicdata-cdn.example",
  "title": "Transport notes 259",
  "body": "Routine transport record. No audit content in this document.",
  "filetype": "html",
  "year": 2018
 },
 {
  "url": "https://data.civicdata.example/archive/roster-7316.xlsx",
  "host": "data.civicdata.example",
  "title": "Roster notes 1",
  "body": "Routine roster record. No audit content in this document.",
  "filetype": "xlsx",
  "year": 2024
 },
 {
  "url": "https://docs.civicdata.example/drafts/roster-3264.pdf",
  "host": "docs.civicdata.example",
  "title": "Roster notes 234",
  "body": "Routine roster record. No audit content in this document.",
  "filetype": "pdf",
  "year": 2019
 },
 {
  "url": "https://legacy.civicdata.example/archive/transport-6553.pdf",
  "host": "legacy.civicdata.example",
  "title": "Transport notes 870",
  "body": "Routine transport record. No audit content in this document.",
  "filetype": "pdf",
  "year": 2017
 },
 {
  "url": "https://civicdata.example/open-data/minutes-2913.xlsx",
  "host": "civicdata.example",
  "title": "Minutes notes 339",
  "body": "Routine minutes record. No audit content in this document.",
  "filetype": "xlsx",
  "year": 2016
 }
]
      
Your query: ?
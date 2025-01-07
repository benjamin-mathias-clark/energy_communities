Files in this directory were generated with the following commands:

```
python compute_energy_communities.py data/la.data.64.County.2022.2024.tsv data/county_to_statistical_area_mapping.tsv data/fossil_fuel_employment_counties.tsv 2022 > data/output/calculated_energy_communities_2023.tsv
python compute_energy_communities.py data/la.data.64.County.2022.2024.tsv data/county_to_statistical_area_mapping.tsv data/fossil_fuel_employment_counties.tsv 2023 > data/output/calculated_energy_communities_2024.tsv
python compute_energy_communities.py data/la.data.64.County.2022.2024.tsv data/county_to_statistical_area_mapping.tsv data/fossil_fuel_employment_counties.tsv 2024 1 11 > data/output/calculated_energy_communities_2025_11months.tsv
 ```

The 2024 calculated list exactly matches the official list. The 2023 list mostly matches, but 35 counties (across 5 MSA/non-MSAs) are missing and 15 counties (across 5 MSA/non-MSAs) are added. This is potentially due to data revisions subsequent to the 2023 energy community list being determined, but that is yet to be confirmed. 
Files in this directory were generated with the following commands:

```
python compute_energy_communities.py data/county_labor_data_2022_11_months.tsv data/county_to_statistical_area_mapping.tsv data/fossil_fuel_employment_counties.tsv 2022 1 11 > data/output/calculated_energy_communities_2023_11_months.tsv
python compute_energy_communities.py data/county_labor_data_2022_first_annual_revision.tsv data/county_to_statistical_area_mapping.tsv data/fossil_fuel_employment_counties.tsv 2022 1 12 > data/output/calculated_energy_communities_2023_first_annual_revision.tsv
python compute_energy_communities.py data/county_labor_data_2023_11_months.tsv data/county_to_statistical_area_mapping.tsv data/fossil_fuel_employment_counties.tsv 2023 1 11 > data/output/calculated_energy_communities_2024_11_months.tsv
python compute_energy_communities.py data/county_labor_data_2023_first_annual_revision.tsv data/county_to_statistical_area_mapping.tsv data/fossil_fuel_employment_counties.tsv 2023 1 12 > data/output/calculated_energy_communities_2024_first_annual_revision.tsv
python compute_energy_communities.py data/la.data.64.County.2022.2024.tsv data/county_to_statistical_area_mapping.tsv data/fossil_fuel_employment_counties.tsv 2023 > data/output/calculated_energy_communities_2024.tsv
python compute_energy_communities.py data/la.data.64.County.2022.2024.tsv data/county_to_statistical_area_mapping.tsv data/fossil_fuel_employment_counties.tsv 2024 1 11 > data/output/calculated_energy_communities_2025_11months.tsv
 ```

The 2024 calculated lists (both calculated_energy_communities_2024.tsv and calculated_energy_communities_2024_first_annual_revision.tsv) exactly match the official list. The 2023 calculated list (calculated_energy_communities_2023_first_annual_revision.tsv) matches with the exception of omitting the U.S. Virgin Islands which is
working as intended as employment data for the U.S. Virgin Islands is sourced separately from BLS LAUS data.
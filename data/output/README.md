Files in this directory were generated with the following commands:

```
python compute_energy_communities.py data/la.data.64.County.2022.2024.tsv data/county_to_statistical_area_mapping.tsv data/fossil_fuel_employment_counties.tsv 2022 > data/output/calculated_energy_communities_2023.tsv
python compute_energy_communities.py data/la.data.64.County.2022.2024.tsv data/county_to_statistical_area_mapping.tsv data/fossil_fuel_employment_counties.tsv 2023 > data/output/calculated_energy_communities_2024.tsv
 python compute_energy_communities.py data/la.data.64.County.2022.2024.tsv data/county_to_statistical_area_mapping.tsv data/fossil_fuel_employment_counties.tsv 2024 1 11 > data/output/calculated_energy_communities_2025_11months.tsv
 ```

 Diffs exist between these calculated lists and the official lists so the code (and input data) does not currently reproduce the IRS's process with perfect fidelity. Further investigation is needed to resolve this.
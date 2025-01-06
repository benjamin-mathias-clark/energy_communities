This directory contains the necessary data to compute which geographic areas qualify as energy communities.


# Data sources
## Employment Data
Raw data files:

la.data.64.County.tsv:  
Downloaded from https://download.bls.gov/pub/time.series/la/la.data.64.County on 2025/01/04 at 11:16am EST.

la.series.tsv:  
Downloaded from https://download.bls.gov/pub/time.series/la/la.series on 2025/01/04 at 11:16am EST.

Input files:

la.data.64.County.2022.2024.tsv:  
    This is a subset of la.data.64.County.tsv. It includes only those rows with data from 2022-2024
    (and the header row). This provides a smaller file so that for analysis which only needs those
    years of data, the program doesn't have to read an unnecessarily large file. It was generated
    with the following command:
    
    `grep "^(series_id|LAU[A-Z0-9]{17}\s+202[2-4])" -E la.data.64.County.tsv > la.data.64.County.2022.2024.tsv`

la.series.counties.txt:  
    This is a subset of la.series.tsv. It includes only information of series that correspond to
    county-level employment data and are currently still being released. Neither this or
    la.series.tsv is presently used in the code, but it was utilized in various manual data
    validation steps. It was generated with the following command.
    
    `grep "^LAUCN[A-Z0-9]{15}\s+F.+2024\s+M11$" -E la.series.tsv > la.series.counties.txt`

## IRS data files
 county_to_statistical_area_mapping.tsv:  
    This file provides a mapping from a county (represented by it's state and county code) to the
    statistical area used for the purpose of energy community eligibility.
    
    It is intended to match the data in Notice 2023-29 Appendix A (available at
    https://www.irs.gov/pub/irs-drop/n-23-29-appendix-a.pdf and in the irs/ folder of this directory).
    As the data in that PDF was not readily exportable to a TSV, preparation of this file
    involved some manual processing. Consequently, erroneous differences vs. the data present
    in Appendix A might exist despite efforts to prevent them.

notice_2023-29_appendix_b.tsv:  
notice_2023-47_appendix_1.tsv:  
notice_2024-30_appendix_1.tsv:  
    These TSV files contain the content of the tables in the IRS notice appendicies that
    there name reflects. Each row specifies a county which meets the fossil fuel
    employment standard for energy community eligibility. The format of each row is
    state_code<tab>county_count<tab>msa_or_nonmsa_name.
    As the data in these PDFs was not readily exportable to a TSV, preparation of this file
    involved some manual processing. Consequently, erroneous differences vs. the data present
    in PDFs might exist despite efforts to prevent them. The source PDFs are present in the irs/
    folder of this directory.

fossil_fuel_employment_counties.tsv:  
    This file contains the sorted concatentation of notice_2023-29_appendix_b.tsv, notice_2023-47_appendix_1.tsv
    and notice_2024-30_appendix_1.tsv so that the list of all counties meeting the fossil fuel
    employment standard is conveniently available in one file. It was generated with the following
    command:

    `sort notice_2023-29_appendix_b.tsv notice_2023-47_appendix_1.tsv notice_2024-30_appendix_1.tsv > fossil_fuel_employment_counties.tsv`

## IRS Energy Community Lists
notice_2023-47_appendix_1.tsv:  
notice_2024-30_appendix_2.tsv:  
    These TSV files contain the content of the tables in the IRS notice appendicies that
    there name reflects. Each row specifies a county which qualifies as an energy community from
    January 1, 2023 to June 6, 2024. The format of each row is
    state_code<tab>county_count<tab>msa_or_nonmsa_name.
    As the data in these PDFs was not readily exportable to a TSV, preparation of this file
    involved some manual processing. Consequently, erroneous differences vs. the data present
    in PDFs might exist despite efforts to prevent them. The source PDFs are present in the irs/
    folder of this directory.

notice_2024-48_appendix_1.tsv:  
    These TSV files contain the content of the tables in the IRS notice appendicies that
    there name reflects. Each row specifies a county which qualifies as an energy community from
    June 7, 2024 to a date TBD. The format of each row is
    state_code<tab>county_count<tab>msa_or_nonmsa_name.
    As the data in these PDFs was not readily exportable to a TSV, preparation of this file
    involved some manual processing. Consequently, erroneous differences vs. the data present
    in PDFs might exist despite efforts to prevent them. The source PDFs are present in the irs/
    folder of this directory.

energy_communities_2023.tsv:  
    This file contains the sorted concatentation of notice_2023-47_appendix_1.tsv
    and notice_2024-30_appendix_2.tsv so that the list of all counties qualifying as energy 
    communities in 2023 is conveniently available in one file. It was generated with the following
    command:

    `sort notice_2023-47_appendix_1.tsv notice_2024-30_appendix_2.tsv > energy_communities_2023.tsv`

energy_communities_2024.tsv:  
    This file is a copy of notice_2024-48_appendix_1.tsv with merely a change in name.

# Links
    https://energycommunities.gov/energy-community-tax-credit-bonus/
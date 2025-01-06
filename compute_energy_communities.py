import sys
import process_employment_data


def main():
    if len(sys.argv) != 5 and len(sys.argv) != 7:
        print(
            "Usage: python compute_energy_communities.py <county_employment_file_path> <county_to_statistical_area_mapping_file_path> <fossil_fuel_employment_counties_file_path> <year> [<start_month> <end_month>]"
        )
        sys.exit(1)

    county_employment_file_path = sys.argv[1]
    county_to_statistical_area_mapping_file_path = sys.argv[2]
    fossil_fuel_employment_counties_file_path = sys.argv[3]
    year = int(sys.argv[4])
    start_month = int(sys.argv[5]) if len(sys.argv) == 7 else 13
    end_month = int(sys.argv[6]) if len(sys.argv) == 7 else 13

    labor_force = process_employment_data.read_employment_data(
        county_employment_file_path, "06"
    )
    unemployment = process_employment_data.read_employment_data(
        county_employment_file_path, "04"
    )
    county_to_statistical_area_mapping = (
        process_employment_data.read_statistical_area_mapping(
            county_to_statistical_area_mapping_file_path
        )
    )
    fossil_fuel_employment_counties_by_sa = (
        process_employment_data.read_statistical_area_mapping(
            fossil_fuel_employment_counties_file_path
        )
    )
    fossil_fuel_employment_counties = set()
    for (
        statistical_area_name,
        state_county_codes,
    ) in fossil_fuel_employment_counties_by_sa.items():
        for state_county_code in state_county_codes:
            fossil_fuel_employment_counties.add(
                (state_county_code[0], state_county_code[1], statistical_area_name)
            )

    nationwide_unemployment_rate = process_employment_data.nationwide_sum(
        unemployment, year, start_month, end_month
    ) / process_employment_data.nationwide_sum(
        labor_force, year, start_month, end_month
    )
    labor_force_sa = process_employment_data.aggregate_statistical_areas(
        process_employment_data.average_over_months(
            labor_force, year, start_month, end_month
        ),
        county_to_statistical_area_mapping,
    )
    unemployment_sa = process_employment_data.aggregate_statistical_areas(
        process_employment_data.average_over_months(
            unemployment, year, start_month, end_month
        ),
        county_to_statistical_area_mapping,
    )
    unemployment_rates_sa = (
        process_employment_data.compute_unemployment_rates_from_values(
            labor_force_sa, unemployment_sa
        )
    )
    counties_above_threshold = process_employment_data.get_counties_above_threshold(
        county_to_statistical_area_mapping,
        unemployment_rates_sa,
        nationwide_unemployment_rate,
    )

    energy_communities = [
        val
        for val in counties_above_threshold
        if val in fossil_fuel_employment_counties
    ]
    energy_communities.sort()
    for energy_community in energy_communities:
        print(f"{energy_community[0]}\t{energy_community[1]}\t{energy_community[2]}")


if __name__ == "__main__":
    main()

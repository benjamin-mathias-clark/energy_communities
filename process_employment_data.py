import csv


def read_employment_data(file_path, measure_code):
    """
    Reads Local Area Unemployment Statistics county data file and extract necessary information.
    This file (la.data.64.County.tsv) from https://download.bls.gov/pub/time.series/la is a TSV
    file containing county-level employment data on both a monthly and annual basis and processes
    it into a usable format.

    Args:
        file_path (str): The path to the TSV file.
        measure_code (str): The code for the measure (e.g. labor force, employment, unemployment)
                            to be extracted

    Returns:
        A dictionary where the key is a tuple of the state & county codes and the value is a
        dictionary where the key is a tuple of the year & period and the data is the value
        (and any footnote codes).

    Raises:
        ValueError: If a row does not have exactly 5 elements.
        ValueError: If any row's series ID does not have the expected prefix of LAUCN
        ValueError: If the area code doesn't confrom to the expected format for a county.
    """
    output = {}

    with open(file_path, "r") as file:
        tsv_reader = csv.reader(file, delimiter="\t")

        for line_number, row in enumerate(tsv_reader, start=1):
            if len(row) != 5:
                raise ValueError(
                    f"Error on line {line_number}: Expected 5 columns, got {len(row)}. Line content: {row}"
                )
            # First line is the header, which we want to skip
            if line_number == 1:
                continue

            series_id = row[0].strip()
            year = int(row[1].strip())
            period = row[2].strip()
            value = row[3].strip()
            footnote_codes = row[4].strip()

            series_id_prefix = series_id[0:5]
            state_code = series_id[5:7]
            county_code = series_id[7:10]
            remaining_area_code = series_id[10:18]
            row_measure_code = series_id[18:]

            if series_id_prefix != "LAUCN":
                raise ValueError(
                    f"Error on line {line_number}: Unexpected series ID prefix"
                )
            if remaining_area_code != "00000000":
                raise ValueError(
                    f"Error on line {line_number}: Unexpected component of area code for county-level data"
                )
            if row_measure_code != measure_code:
                continue

            location = (state_code, county_code)
            if location not in output:
                output[location] = {}
            output[location][(year, period)] = (value, footnote_codes)
    return output


def read_statistical_area_mapping(file_path):
    """
    Reads TSV file where each row corresponds to a US county and providies the statistical area
    (MSA or non-MSA) which that county is part of for the purpose of energy community status.

    Args:
        file_path (str): The path to the TSV file.

    Returns:
        A dictionary where the key is the name of the statistical area (MSA or non-MSA) and the
        value is a list of (state_code, county_code) that are part of that statistical area

    Raises:
        ValueError: If a row does not have exactly 3 elements.
    """
    output = {}

    with open(file_path, "r") as file:
        tsv_reader = csv.reader(file, delimiter="\t")

        for line_number, row in enumerate(tsv_reader, start=1):
            if len(row) != 3:
                raise ValueError(
                    f"Error on line {line_number}: Expected 3 columns, got {len(row)}. Line content: {row}"
                )

            state_code = row[0].strip()
            county_code = row[1].strip()
            statistical_area = row[2].strip()

            location = (state_code, county_code)
            # This program does not currently support American Samoa, Guam,
            # Northern Mariana Islands or the U.S. Virgin Islands as their
            # employment data can't be sourced from the same files. Adding
            # support for them is future work.
            # TODO: Add support for these territories.
            if location in (("60", "000"), ("66", "000"), ("69", "000"), ("78", "000")):
                continue
            if statistical_area not in output:
                output[statistical_area] = []
            output[statistical_area].append(location)
    return output


def annual_unemployment_rates(labor_force, unemployment, year):
    """
    Compute unemployment rate for a given year from unemployment and labor force annual data.
    This function does not independently compute annual unemployment and labor force by adding
    up monthly data. Rather, it uses the annual data already present (using period code "M13").

    Args:
        labor_force (dict): A dictionary with (state_code, county_code) as key and value being a
                            dictionary with (year, period code) as key and (labor force,
                            footnote codes) as value.
        unemployment (dict): A dictionary with (state_code, county_code) as key and value being a
                             dictionary with (year, period code) as key and (unemployment,
                             footnote codes) as value.
        year (int): The year to do the calculation for

    Returns:
        A dictionary with (state_code, county_code) and a unemployment rate as value.
    """
    return compute_unemployment_rates_for_period(
        labor_force, unemployment, year, 13, 13
    )


def average_over_months(data, year, start_month, end_month):
    """
    Average data over a given time range.

    Args:
        data (dict): A dictionary with (state_code, county_code) as key and value being a dictionary
                     with (year, period code) as key and (value, footnote codes) as value
        year (int): The year to do the calculation for
        start_month (int): The first month to use data from (inclusive).
        end_month (int): The last month to use data from (inclusive).

    Returns:
        A dictionary with (state_code, county_code) and the summed values as value.
    """
    output = {}
    for state_county_codes in data:
        total = 0
        for key in data[state_county_codes]:
            key_year = key[0]
            month = int(key[1][1:])
            if key_year == year and month >= start_month and month <= end_month:
                total += int(data[state_county_codes][key][0])
        output[state_county_codes] = total / (end_month - start_month + 1)
    return output


def nationwide_sum(data, year, start_month, end_month):
    """
    Aggregate data over a given time range and all locations.

    Args:
        data (dict): A dictionary with (state_code, county_code) as key and value being a dictionary
                     with (year, period code) as key and (value, footnote codes) as value
        year (int): The year to do the calculation for
        start_month (int): The first month to use data from (inclusive).
        end_month (int): The last month to use data from (inclusive).

    Returns:
        A dictionary with (state_code, county_code) and the summed values as value.
    """
    total = 0
    for state_county_codes in data:
        for key in data[state_county_codes]:
            key_year = key[0]
            month = int(key[1][1:])
            if key_year == year and month >= start_month and month <= end_month:
                total += int(data[state_county_codes][key][0])
    return total / (end_month - start_month + 1)


def compute_unemployment_rates_for_period(
    labor_force, unemployment, year, start_month, end_month
):
    """
    Compute unemployment rate for a given time range from unemployment and labor force monthly data.

    Args:
        labor_force (dict): A dictionary with (state_code, county_code) as key and value being a
                            dictionary with (year, period code) as key and (labor force,
                            footnote codes) as value.
        unemployment (dict): A dictionary with (state_code, county_code) as key and value being a
                             dictionary with (year, period code) as key and (unemployment,
                             footnote codes) as value.
        year (int): The year to do the calculation for
        start_month (int): The first month to use data from (inclusive).
        end_month (int): The last month to use data from (inclusive).

    Returns:
        A dictionary with (state_code, county_code) and a unemployment rate as value.
    """
    labor_force_summed = average_over_months(labor_force, year, start_month, end_month)
    unemployment_summed = average_over_months(
        unemployment, year, start_month, end_month
    )
    return compute_unemployment_rates_from_values(
        labor_force_summed, unemployment_summed
    )


def compute_unemployment_rates_from_values(labor_force, unemployment):
    """
    Compute unemployment rate from unemployment and labor force counts.

    Args:
        labor_force (dict): A dictionary with either (state_code, county_code) or statistical areas
                            as key and labor force as value
        unemployment (str): A dictionary with either (state_code, county_code) or statistical areas
                            as key and unemployment as value

    Returns:
        A dictionary with either (state_code, county_code) or statistical areas and an unemployment
        rate as value.
    """
    output = {}
    for key in labor_force:
        output[key] = unemployment[key] / labor_force[key]
    return output


def aggregate_statistical_areas(data, statistical_area_map):
    """
    Aggregate data from all counties in a statistical area.

    Args:
        data (dict): A dictionary with (state_code, county_code) as key and a number as value
        statistical_area_map (dict): A dictionary with the key being the name of a statistical area
                                     and the value being a list of (state_code, county_code)

    Returns:
        A dictionary with the statistical area name as key and the summed county data as value.
    """
    output = {}
    for key, state_county_codes in statistical_area_map.items():
        if key not in output:
            output[key] = 0
        for state_county_code in state_county_codes:
            if state_county_code not in data:
                # No employment data is expected for Kalawao County, HI.
                # For any other county this is unexpected so we throw an error
                # so investigation can take place.
                if state_county_code != ("15", "005"):
                    raise ValueError(
                        f"No data found for {state_county_code[0]},{state_county_code[1]} which is assigned to the {key} statistical area."
                    )
            else:
                output[key] += data[state_county_code]
    return output


def get_counties_above_threshold(
    statistical_area_map, unemployment_rates_sa, nationwide_unemployment_rate
):
    """
    Aggregate data from all counties in a statistical area.

    Args:
        statistical_area_map (dict): A dictionary with the key being the name of a statistical area
                                     and the value being a list of (state_code, county_code)
        unemployment_rates_sa (dict): A dictionary with the key being the name of a statistical area
                                      and the value being it's unemployment rate for the given period.
        nationwide_unemployment_rate (float): The US unemployment rate for the given time period

    Returns:
        A list of (state_code, county_code, statistical_area_name) for those counties which are in a statistical area with
        an unemployment rate above the national average.
    """
    output = []
    for statistical_area_name, state_county_codes in statistical_area_map.items():
        if unemployment_rates_sa[statistical_area_name] >= nationwide_unemployment_rate:
            for state_county_code in state_county_codes:
                output.append(
                    (state_county_code[0], state_county_code[1], statistical_area_name)
                )
    return output

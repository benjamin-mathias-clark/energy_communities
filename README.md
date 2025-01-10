# Predicting Energy Community Eligibility
Federal law provides significant investment tax credits for clean electricity and energy storage
projects, provided certain criteria are satisfied. When project labor standards are met, or if
projects qualify for size-based exceptions, the baseline tax credit is 30%. Two additional bonus
credits of 10% each are available for projects meeting one of two conditions: (1) the project is
situated within a designated "energy community," or (2) it complies with domestic content
provisions. Eligibility for these bonus tax credits can be critical to the financial viability of
a project, making it essential to understand the nuances of "energy community" designation.
## Defining Energy Communities
A location qualifies as an "energy community" under one of the following conditions:
1. Brownfield Sites: The project site has been classified as a brownfield.
2. Fossil Fuel Employment Counties: A metropolitan or non-metropolitan statistical area (an
aggregation of one or more counties) that meets a requirement for historical fossil fuel employment
above a specified level and had an unemployment rate above the national average in the prior year.
3. Coal Closure Census Tracts: A census tract where a coal mine or coal-fired power plant ceased
operation after specified dates or a census tract adjacent to such a census tract.

The second eligibility criterion is particularly significant due to its broad applicability. Of the
3,221 counties in the 50 states, DC and Puerto Rico, 1,946 (60%) meet the historical fossil fuel
employment requirement and could be eligible depending on their unemployment rate. As a result,
clean electricity and energy storage projects across much of the U.S. might benefit from this bonus
tax credit.

However, that dependence on the previous year’s unemployment rate introduces complexity for
renewable energy developers. Locations can lose and gain eligibility on an annual basis. For
example, 964 counties qualified as energy communities when 2022 employment data was used to
establish the energy community list in 2023. When the energy community list was updated the
following year using 2023 employment data, 175 (18%) counties lost eligibility and 112 gained it.
These annual updates introduce uncertainty, as a project could be in an eligible county as the
developer moves through initial planning stages, but lose eligibility while awaiting key
pre-construction milestones such as permitting and interconnection.

In contrast, eligibility under the two other criteria is mostly static. For instance, the IRS
maintains a list of census tracts satisfying the coal closure requirement. While census tracts
are added as new coal closures occur, no tract is removed. This stability allows developers in
those areas to plan with confidence.

While that is a relief to developers working in those areas, that doesn’t cover enough of the
country and is concentrated in specific regions. Renewable energy developers in other areas,
however, must navigate the uncertainty of shifting energy community eligibility.  It factors into
decisions such as site prioritization and whether to make firm orders for long lead components.
Monitoring local unemployment rates is a necessary step in making the right business decisions.
Understanding the official process and proactively analyzing data is key.

## Calculating Local Unemployment Rates
The IRS revises the list of qualifying metropolitan and non-metropolitan statistical areas (MSAs
and non-MSAs) annually, typically in May or June, based on the previous year’s employment data from
the Bureau of Labor Statistics (BLS) Local Area Unemployment Statistics program.. So the simplest
way for developers to get a head start is to go directly to the source for the data.

For instance, in 2024, BLS published the annual county-level employment data for 2023 (the exact
data the IRS uses) on April 19th. The IRS published the official energy community list on June 7th.
So one can get a seven week head start just by doing the math yourself. In fact, this works. By
applying the IRS’s published methodology using their published county-to-MSA mappings and BLS data,
I was able to exactly replicate the official energy communities lists for 2022 and 2023.

To improve on this and make predictions further into the future, developers can leverage monthly
county-level employment data rather than waiting for the annual data. The BLS publishes preliminary
monthly data on a ~1 month lag. A first revision to that data is then published the following month
at the same time as the preliminary data for the subsequent month. After the year ends, data for
all months undergoes an additional revision cycle as part of the process of producing annual data.

Using partial-year data, developers can keep track of the unemployment rate in MSA/non-MSAs where
they are considering projects. While partial-year data cannot conclusively ensure eligibility due
to potential changes in employment later in the year and subsequent adjustments, it can offer early
insights. Developers can distinguish between sites that are highly likely to qualify due to high
unemployment rates and those on the margin of eligibility. Historical patterns of data revisions
can further inform these projections.

## 2025 Energy Communities
To illustrate this approach, I applied it to predict the 2025 energy community list using currently
available data. As of today, county-level data from January to November is available (with November
figures being preliminary). Aggregating this data to the MSA/non-MSA level utilized for eligibility
determinations reveals that, of the 261 MSA/non-MSAs (representing 1,946 counties) meeting the
fossil fuel employment requirement, 124 (representing 805 counties) are on track to qualify based
on their unemployment rate.

To estimate the probability that additional data and revisions might alter this status before the
official list is established, I analyzed recent years’ data changes. Specifically, I compared
equivalent January-November data and annual data as of the annual revision for 2022 and 2023. Based
on the observed distribution of changes in local unemployment rates relative to the national
average between these data vintages, it is possible to generate probabilistic predictions for 2025
eligibility.

## Open-source code & data
To support renewable energy developers and other stakeholders, I am sharing both the code used to
generate energy community lists based on the IRS’s methodology and the
[data](https://docs.google.com/spreadsheets/d/1dwxNsArpU8WewtduW35-_tZ-ETdZwX0xTdKmldsOUE8/view)
on potential 2025 energy communities. I aim to provide regular data updates as new monthly
employment data become available. If this resource proves valuable to you, please get in touch.

I welcome feedback and questions. You can reach me at benjamin.mathias.clark@gmail.com.

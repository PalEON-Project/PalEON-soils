# PalEON-soils
Repository for aggregation of soils data across the PalEON domain

This repository uses the 10m gridded gSSURGO soil data from the USDA-NRCS, available for download here: https://gdg.sc.egov.usda.gov/
Download the gSSURGO geodatabase files by State (here we use MI, MN, WI, IN, IL for the Upper Midwest region). The latest version of this script does this for the entire domain

The gSSURGO data is stored in an ESRI Arc geodatabase that is currently not possible to to read directly into R.

Overview of steps to create 10x10m ssurgo soil dataframe for each state:

1. Download state level geodatabase
2. Read in, calculated weighted averages of variables wanted and join state level tables in R using GSSURGO_aggregation.R
3. In ArcGIS, join the state level component table (XX_component_agg.csv) file to the gssurgo 10m raster for that state.
4. Create raster lookups for each variable for each state of intererest (.py script)
5. Mosaic rasters for Midwest states and for whole paleon domain (.py script)
6. Aggregate to 8km paleon grid (.py script)-Note: we can aggregate to any grid level desired, but default produces 8km grid.

Final outputs include:

Percent sand (0-100%)
Percent clay (0-100%)
Percent silt (0-100%)
Calcium Carbonate (CaCO3)
Cation Exchange Capacity (CEC)
Saturated Hyrdaulic Conducitivity (KSAT)
Total Available Water Capacity (AWC or Water_Storage)










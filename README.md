# PalEON-soils
Repository for aggregation of soils data across the PalEON domain

This repository uses the 10m gridded gSSURGO soil data from the USDA-NRCS, available for download here: https://gdg.sc.egov.usda.gov/
Download the gSSURGO geodatabase files by State (here we use MI, MN, WI, IN, IL). 

The gSSURGO data is stored in an ESRI Arc geodatabase that is currently not possible to to read directly into R.

Overview of steps to create 10x10m ssurgo soil dataframe for each state:

1. Download state level geodatabase
2. Read in and join state level tables in R using GSSURGO_aggregation.R
3. In ArcGIS, join the IL_component_agg.csv file to the using Add Join function
4. Create lookups and aggregate using gssurgo_lookup_scripts.py (need to change the state)




The weighted averages of each soil attribute (e.g. %sand) was previously calculated from the 10m gridded gSSURGO data using the SSURGO on-demand ArcGIS toolbox (available here https://github.com/ncss-tech/ssurgoOnDemand.git, citation forthcoming). This toolbox needs to be added to ArcToolbox before beginning. 




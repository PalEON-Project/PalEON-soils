# PalEON-soils
Repository for aggregation of soils data across the PalEON domain

This repository uses the 10m gridded gSSURGO soil data from the USDA-NRCS, available for download here: https://gdg.sc.egov.usda.gov/
Download the gSSURGO geodatabase files by State (here we use MI, MN, WI, IN, IL). 

The weighted averages of each soil attribute (e.g. %sand) is calculated from the 10m gridded gSSURGO data using the SSURGO on-demand ArcGIS toolbox (available here https://github.com/ncss-tech/ssurgoOnDemand.git, citation forthcoming). This toolbox needs to be added to ArcToolbox before beginning. 

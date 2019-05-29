#Creating gssurgo rasters and aggregating to different grid cells
#Author: Kelly Heilman
#Date: 11/30/16

# This is done in Arcgis command line using mapunit 10m gssurgo rasters from NCRS geospatial gateway. These rasters are run through the Ssurgo on demand arcgis toolbox to create and join soil tables
filedir = "C:/Users/paleolab/Documents/soils/"

state = "IN"
raster10m =  ["MapunitRaster_" + state + "_10m"]


# need to do the table joins:


# Here we are processing for sand 
#lookup creates a new raster with the selected field (2nd argument) as the value for the raster
# Replace a layer/table view name with a path to a dataset (which can be a layer file) or create the layer/table view within the script
# The following inputs are layers or table views: "MapunitRaster_wi_10m"


arcpy.gp.Lookup_sa( raster10m , "tbl_Total_Sand__Rep_Value_wtd_avg_0_30.sandtotal_r", [filedir + "lookupsand_" + state ])
arcpy.gp.Lookup_sa( raster10m , "tbl_Total_Sand__Rep_Value_wtd_avg_0_30.sandtotal_r", [filedir + "lookupsilt_" + state ])
arcpy.gp.Lookup_sa( raster10m , "tbl_Total_Sand__Rep_Value_wtd_avg_0_30.sandtotal_r", [filedir + "lookupclay_" + state ])
arcpy.gp.Lookup_sa( raster10m , "tbl_Total_Sand__Rep_Value_wtd_avg_0_30.sandtotal_r", [filedir + "lookupCEC_" + state ])


# aggregate soil parameters to 1km:
arcpy.gp.Aggregate_sa(["lookupsand_" + state], [filedir + state + "8km_sand"], "100", "MEAN", "EXPAND", "DATA")

# aggregate soil parameters to 1km:
arcpy.gp.Aggregate_sa(["lookupsand_" + state], [filedir + state + "8km_sand"], "800", "MEAN", "EXPAND", "DATA")


# Here we are processing for cation exchange capacity
# lookup creates a new raster with the selected field (2nd argument) as the value for the raster
# Replace a layer/table view name with a path to a dataset (which can be a layer file) or create the layer/table view within the script
# The following inputs are layers or table views: "MapunitRaster_wi_10m"
arcpy.gp.Lookup_sa("MapunitRaster_wi_10m", "tbl_Cation_Exchange_Capcity__Rep_Value_wtd_avg_0_30.cec7_r", "C:/Users/paleolab/Documents/soils/gssurgo_g_wi/lookupCEC")
arcpy.gp.Lookup_sa("MapunitRaster_mn_10m", "tbl_Cation_Exchange_Capcity__Rep_Value_wtd_avg_0_30.cec7_r", "C:/Users/paleolab/Documents/soils/gssurgo_g_mn/lookupCEC")
arcpy.gp.Lookup_sa("MapunitRaster_il_10m", "tbl_Cation_Exchange_Capcity__Rep_Value_wtd_avg_0_30.cec7_r", "C:/Users/paleolab/Documents/soils/gssurgo_g_il/lookupCEC")
arcpy.gp.Lookup_sa("MapunitRaster_in_10m", "tbl_Cation_Exchange_Capcity__Rep_Value_wtd_avg_0_30.cec7_r", "C:/Users/paleolab/Documents/soils/gssurgo_g_in/lookupCEC")
arcpy.gp.Lookup_sa("MapunitRaster_mi_10m", "tbl_Cation_Exchange_Capcity__Rep_Value_wtd_avg_0_30.cec7_r", "C:/Users/paleolab/Documents/soils/gssurgo_g_mi/lookupCEC")

#now create 8km  aggregated rasters from the lookup raster

# for soil cation exchange capacity
arcpy.gp.Aggregate_sa("lookwiCEC", "C:/Users/paleolab/Documents/soils/gssurgo_g_wi/8km_wi_cec", "800", "MEAN", "EXPAND", "DATA")
arcpy.gp.Aggregate_sa("lookmnCEC", "C:/Users/paleolab/Documents/soils/gssurgo_g_mn/8km_mn_cec", "800", "MEAN", "EXPAND", "DATA")
arcpy.gp.Aggregate_sa("lookilCEC", "C:/Users/paleolab/Documents/soils/gssurgo_g_il/8km_il_cec", "800", "MEAN", "EXPAND", "DATA")
arcpy.gp.Aggregate_sa("lookinCEC", "C:/Users/paleolab/Documents/soils/gssurgo_g_in/8km_in_cec", "800", "MEAN", "EXPAND", "DATA")
arcpy.gp.Aggregate_sa("lookmiCEC", "C:/Users/paleolab/Documents/soils/gssurgo_g_mi/8km_mi_sand", "800", "MEAN", "EXPAND", "DATA")

#Mosaic All the Cation Exchange Capacity rasters together: CEC
arcpy.MosaicToNewRaster_management(input_rasters="C:/Users/paleolab/Documents/soils/gssurgo_g_mn/8km_mn_cec;C:/Users/paleolab/Documents/soils/gssurgo_g_il/8km_il_cec;C:/Users/paleolab/Documents/soils/gssurgo_g_wi/8km_wi_cec;C:/Users/paleolab/Documents/soils/gssurgo_g_in/8km_in_cec;C:/Users/paleolab/Documents/soils/gssurgo_g_mi/8km_mi_cec", output_location="C:/Dropbox/GIS_Kelly/Kelly Heilman/gSSURGOsoil/soils", raster_dataset_name_with_extension="mosaicCEC.tif", coordinate_system_for_the_raster="", pixel_type="32_BIT_UNSIGNED", cellsize="", number_of_bands="1", mosaic_method="BLEND", mosaic_colormap_mode="FIRST")



# Here we are processing for calcium carbonate:
# lookup creates a new raster with the selected field (2nd argument) as the value for the raster
# Replace a layer/table view name with a path to a dataset (which can be a layer file) or create the layer/table view within the script
# The following inputs are layers or table views: "MapunitRaster_wi_10m"
arcpy.gp.Lookup_sa("MapunitRaster_wi_10m", "tbl_Calcium_Carbonate__Rep_Value_wtd_avg_0_30.caco3_r", "C:/Users/paleolab/Documents/soils/gssurgo_g_wi/lookupcaco3")
arcpy.gp.Lookup_sa("MapunitRaster_mn_10m", "tbl_Calcium_Carbonate__Rep_Value_wtd_avg_0_30.caco3_r", "C:/Users/paleolab/Documents/soils/gssurgo_g_mn/lookupcaco3")
arcpy.gp.Lookup_sa("MapunitRaster_il_10m", "tbl_Calcium_Carbonate__Rep_Value_wtd_avg_0_30.caco3_r", "C:/Users/paleolab/Documents/soils/gssurgo_g_il/lookupcaco3")
arcpy.gp.Lookup_sa("MapunitRaster_in_10m", "tbl_Calcium_Carbonate__Rep_Value_wtd_avg_0_30.caco3_r", "C:/Users/paleolab/Documents/soils/gssurgo_g_in/lookupcaco3")
arcpy.gp.Lookup_sa("MapunitRaster_mi_10m", "tbl_Calcium_Carbonate__Rep_Value_wtd_avg_0_30.caco3_r", "C:/Users/paleolab/Documents/soils/gssurgo_g_mi/lookupcaco3")

#now create 8km  aggregated rasters from the lookup raster

# for soil calcium carbonate
arcpy.gp.Aggregate_sa("lookupcaco3", "C:/Users/paleolab/Documents/soils/gssurgo_g_wi/8km_wi_caco3", "800", "MEAN", "EXPAND", "DATA")
arcpy.gp.Aggregate_sa("lookupcaco3", "C:/Users/paleolab/Documents/soils/gssurgo_g_mn/8km_mn_caco3", "800", "MEAN", "EXPAND", "DATA")
arcpy.gp.Aggregate_sa("lookupcaco3", "C:/Users/paleolab/Documents/soils/gssurgo_g_il/8km_il_caco3", "800", "MEAN", "EXPAND", "DATA")
arcpy.gp.Aggregate_sa("lookupcaco3", "C:/Users/paleolab/Documents/soils/gssurgo_g_in/8km_in_caco3", "800", "MEAN", "EXPAND", "DATA")
arcpy.gp.Aggregate_sa("lookupcaco3", "C:/Users/paleolab/Documents/soils/gssurgo_g_mi/8km_mi_caco3", "800", "MEAN", "EXPAND", "DATA")

#Mosaic All the Cation Exchange Capacity rasters together: calcium carbonate
arcpy.MosaicToNewRaster_management(input_rasters="C:/Users/paleolab/Documents/soils/gssurgo_g_mn/8km_mn_caco3;C:/Users/paleolab/Documents/soils/gssurgo_g_il/8km_il_caco3;C:/Users/paleolab/Documents/soils/gssurgo_g_wi/8km_wi_caco3;C:/Users/paleolab/Documents/soils/gssurgo_g_in/8km_in_caco3;C:/Users/paleolab/Documents/soils/gssurgo_g_mi/8km_mi_caco3", output_location="C:/Dropbox/GIS_Kelly/Kelly Heilman/gSSURGOsoil/soils", raster_dataset_name_with_extension="mosaiccaco3.tif", coordinate_system_for_the_raster="", pixel_type="32_BIT_UNSIGNED", cellsize="", number_of_bands="1", mosaic_method="BLEND", mosaic_colormap_mode="FIRST")


# Replace a layer/table view name with a path to a dataset (which can be a layer file) or create the layer/table view within the script
# The following inputs are layers or table views: "lookupsand"

arcpy.gp.Aggregate_sa("lookupsand", "C:/Users/paleolab/Documents/soils/gssurgo_g_wi/8km_wi_sand", "800", "MEAN", "EXPAND", "DATA")
arcpy.gp.Aggregate_sa("lookupsand", "C:/Users/paleolab/Documents/soils/gssurgo_g_mn/8km_mn_sand", "800", "MEAN", "EXPAND", "DATA")
arcpy.gp.Aggregate_sa("lookupsand", "C:/Users/paleolab/Documents/soils/gssurgo_g_il/8km_il_sand", "800", "MEAN", "EXPAND", "DATA")
arcpy.gp.Aggregate_sa("lookupsand", "C:/Users/paleolab/Documents/soils/gssurgo_g_in/8km_in_sand", "800", "MEAN", "EXPAND", "DATA")
arcpy.gp.Aggregate_sa("lookupsand", "C:/Users/paleolab/Documents/soils/gssurgo_g_mi/8km_mi_sand", "800", "MEAN", "EXPAND", "DATA")


#now create 1km aggregated rasters from the lookup rasters
# Replace a layer/table view name with a path to a dataset (which can be a layer file) or create the layer/table view within the script
# The following inputs are layers or table views: "lookupsand"

arcpy.gp.Aggregate_sa("lookupsand", "C:/Users/paleolab/Documents/soils/gssurgo_g_wi/1km_WI_sand", "100", "MEAN", "EXPAND", "DATA")
arcpy.gp.Aggregate_sa("lookupsand", "C:/Users/paleolab/Documents/soils/gssurgo_g_mn/1km_mn_sand", "100", "MEAN", "EXPAND", "DATA")
arcpy.gp.Aggregate_sa("lookupsand", "C:/Users/paleolab/Documents/soils/gssurgo_g_il/1km_il_sand", "100", "MEAN", "EXPAND", "DATA")
arcpy.gp.Aggregate_sa("lookupsand", "C:/Users/paleolab/Documents/soils/gssurgo_g_in/1km_in_sand", "100", "MEAN", "EXPAND", "DATA")
arcpy.gp.Aggregate_sa("lookupsand", "C:/Users/paleolab/Documents/soils/gssurgo_g_mi/1km_mi_sand", "100", "MEAN", "EXPAND", "DATA")

# What we are actually interested in is merging all the "lookupsand" rasters into one big uppermidwest sand raster:

#Mosaic All the SAND rasters together
arcpy.MosaicToNewRaster_management(input_rasters="C:/Users/paleolab/Documents/soils/gssurgo_g_mn/lookupsand;C:/Users/paleolab/Documents/soils/gssurgo_g_il/lookupsand;C:/Users/paleolab/Documents/soils/gssurgo_g_wi/lookupsand;C:/Users/paleolab/Documents/soils/gssurgo_g_in/lookupsand;C:/Users/paleolab/Documents/soils/gssurgo_g_mi/lookupsand", output_location="C:/Dropbox/GIS_Kelly/Kelly Heilman/gSSURGOsoil/soils", raster_dataset_name_with_extension="mosaicsand.tif", coordinate_system_for_the_raster="", pixel_type="32_BIT_UNSIGNED", cellsize="", number_of_bands="1", mosaic_method="BLEND", mosaic_colormap_mode="FIRST")

#Mosaic All the AWC rasters together
arcpy.MosaicToNewRaster_management(input_rasters="C:/Users/paleolab/Documents/soils/gssurgo_g_mn/lookupawc;C:/Users/paleolab/Documents/soils/gssurgo_g_in/lookupawc;C:/Users/paleolab/Documents/soils/gssurgo_g_wi/lookupawc;C:/Users/paleolab/Documents/soils/gssurgo_g_il/lookupawc;C:/Users/paleolab/Documents/soils/gssurgo_g_mi/lookupawc", output_location="C:/Dropbox/GIS_Kelly/Kelly Heilman/gSSURGOsoil/soils", raster_dataset_name_with_extension="mosaicawc.tif", coordinate_system_for_the_raster="", pixel_type="32_BIT_UNSIGNED", cellsize="", number_of_bands="1", mosaic_method="BLEND", mosaic_colormap_mode="FIRST")

# run this for during lab:
arcpy.MosaicToNewRaster_management(input_rasters="C:/Users/paleolab/Documents/soils/gssurgo_g_mn/lookupsand;C:/Users/paleolab/Documents/soils/gssurgo_g_il/lookupsand;C:/Users/paleolab/Documents/soils/gssurgo_g_wi/lookupsand;C:/Users/paleolab/Documents/soils/gssurgo_g_in/lookupsand;C:/Users/paleolab/Documents/soils/gssurgo_g_mi/lookupsand", output_location="C:/Dropbox/GIS_Kelly/Kelly Heilman/gSSURGOsoil/soils", raster_dataset_name_with_extension="mosaicsand.tif", coordinate_system_for_the_raster="", pixel_type="32_BIT_UNSIGNED", cellsize="", number_of_bands="1", mosaic_method="BLEND", mosaic_colormap_mode="FIRST")
arcpy.MosaicToNewRaster_management(input_rasters="C:/Users/paleolab/Documents/soils/gssurgo_g_mn/lookupawc;C:/Users/paleolab/Documents/soils/gssurgo_g_in/lookupawc;C:/Users/paleolab/Documents/soils/gssurgo_g_wi/lookupawc;C:/Users/paleolab/Documents/soils/gssurgo_g_il/lookupawc;C:/Users/paleolab/Documents/soils/gssurgo_g_mi/lookupawc", output_location="C:/Dropbox/GIS_Kelly/Kelly Heilman/gSSURGOsoil/soils", raster_dataset_name_with_extension="mosaicawc.tif", coordinate_system_for_the_raster="", pixel_type="32_BIT_UNSIGNED", cellsize="", number_of_bands="1", mosaic_method="BLEND", mosaic_colormap_mode="FIRST")
arcpy.gp.Lookup_sa("MapunitRaster_wi_10m", "tbl_Saturated_Hydraulic_Conductivity__Rep_Value_wtd_avg_0_30.ksat_r", "C:/Users/paleolab/Documents/soils/gssurgo_g_wi/lookupksat")
arcpy.gp.Lookup_sa("MapunitRaster_mn_10m", "tbl_Saturated_Hydraulic_Conductivity__Rep_Value_wtd_avg_0_30.ksat_r", "C:/Users/paleolab/Documents/soils/gssurgo_g_mn/lookupksat")
arcpy.gp.Lookup_sa("MapunitRaster_il_10m", "tbl_Saturated_Hydraulic_Conductivity__Rep_Value_wtd_avg_0_30.ksat_r", "C:/Users/paleolab/Documents/soils/gssurgo_g_il/lookupksat")
arcpy.gp.Lookup_sa("MapunitRaster_in_10m", "tbl_Saturated_Hydraulic_Conductivity__Rep_Value_wtd_avg_0_30.ksat_r", "C:/Users/paleolab/Documents/soils/gssurgo_g_in/lookupksat")
arcpy.gp.Lookup_sa("MapunitRaster_mi_10m", "tbl_Saturated_Hydraulic_Conductivity__Rep_Value_wtd_avg_0_30.ksat_r", "C:/Users/paleolab/Documents/soils/gssurgo_g_mi/lookupksat")
arcpy.MosaicToNewRaster_management(input_rasters="C:/Users/paleolab/Documents/soils/gssurgo_g_mn/lookupksat;C:/Users/paleolab/Documents/soils/gssurgo_g_in/lookupksat;C:/Users/paleolab/Documents/soils/gssurgo_g_wi/lookupksat;C:/Users/paleolab/Documents/soils/gssurgo_g_il/lookupksat;C:/Users/paleolab/Documents/soils/gssurgo_g_mi/lookupksat", output_location="C:/Dropbox/GIS_Kelly/Kelly Heilman/gSSURGOsoil/soils", raster_dataset_name_with_extension="mosaicksat.tif", coordinate_system_for_the_raster="", pixel_type="32_BIT_UNSIGNED", cellsize="", number_of_bands="1", mosaic_method="BLEND", mosaic_colormap_mode="FIRST")


#Mosaic All the KSAT rasters together
arcpy.MosaicToNewRaster_management(input_rasters="C:/Users/paleolab/Documents/soils/gssurgo_g_mn/lookupksat;C:/Users/paleolab/Documents/soils/gssurgo_g_in/lookupksat;C:/Users/paleolab/Documents/soils/gssurgo_g_wi/lookupksat;C:/Users/paleolab/Documents/soils/gssurgo_g_il/lookupksat;C:/Users/paleolab/Documents/soils/gssurgo_g_mi/lookupksat", output_location="C:/Dropbox/GIS_Kelly/Kelly Heilman/gSSURGOsoil/soils", raster_dataset_name_with_extension="mosaicksat.tif", coordinate_system_for_the_raster="", pixel_type="32_BIT_UNSIGNED", cellsize="", number_of_bands="1", mosaic_method="BLEND", mosaic_colormap_mode="FIRST")

# now do the lookup for AWC

arcpy.gp.Lookup_sa("MapunitRaster_wi_10m", "tbl_Available_Water_Capacity__Rep_Value_wtd_avg_0_30.awc_r", "C:/Users/paleolab/Documents/soils/gssurgo_g_wi/lookupawc")
arcpy.gp.Lookup_sa("MapunitRaster_mn_10m", "tbl_Available_Water_Capacity__Rep_Value_wtd_avg_0_30.awc_r", "C:/Users/paleolab/Documents/soils/gssurgo_g_mn/lookupawc")
arcpy.gp.Lookup_sa("MapunitRaster_il_10m", "tbl_Available_Water_Capacity__Rep_Value_wtd_avg_0_30.awc_r", "C:/Users/paleolab/Documents/soils/gssurgo_g_il/lookupawc")
arcpy.gp.Lookup_sa("MapunitRaster_in_10m", "tbl_Available_Water_Capacity__Rep_Value_wtd_avg_0_30.awc_r", "C:/Users/paleolab/Documents/soils/gssurgo_g_in/lookupawc")
arcpy.gp.Lookup_sa("MapunitRaster_mi_10m", "tbl_Available_Water_Capacity__Rep_Value_wtd_avg_0_30.awc_r", "C:/Users/paleolab/Documents/soils/gssurgo_g_mi/lookupawc")


#Mosaic All the AWC rasters together
#AWC lookups are 32-bit floating point
arcpy.MosaicToNewRaster_management(input_rasters="C:/Users/paleolab/Documents/soils/gssurgo_g_mn/lookupawc;C:/Users/paleolab/Documents/soils/gssurgo_g_in/lookupawc;C:/Users/paleolab/Documents/soils/gssurgo_g_wi/lookupawc;C:/Users/paleolab/Documents/soils/gssurgo_g_il/lookupawc;C:/Users/paleolab/Documents/soils/gssurgo_g_mi/lookupawc", output_location="C:/Dropbox/GIS_Kelly/Kelly Heilman/gSSURGOsoil/soils", raster_dataset_name_with_extension="mosaicawc2.tif", coordinate_system_for_the_raster="", pixel_type="32_BIT_FLOAT", cellsize="", number_of_bands="1", mosaic_method="BLEND", mosaic_colormap_mode="FIRST")
arcpy.gp.Aggregate_sa("mosaicawc2.tif", "C:/Dropbox/GIS_Kelly/Kelly Heilman/gSSURGOsoil/soils/8km_UMW_awc", "800", "MEAN", "EXPAND", "DATA")
arcpy.gp.Aggregate_sa("mosaicawc2.tif", "C:/Dropbox/GIS_Kelly/Kelly Heilman/gSSURGOsoil/soils/1km_UMW_awc", "100", "MEAN", "EXPAND", "DATA")

#running this overnight to make aggregate rasters
# Replace a layer/table view name with a path to a dataset (which can be a layer file) or create the layer/table view within the script
# The following inputs are layers or table views: "mosaicksat.tif"
arcpy.gp.Aggregate_sa("mosaicsat.tif", "C:/Dropbox/GIS_Kelly/Kelly Heilman/gSSURGOsoil/soils/8km_UMW_satk", "800", "MEAN", "EXPAND", "DATA")
arcpy.gp.Aggregate_sa("mosaicsat.tif", "C:/Dropbox/GIS_Kelly/Kelly Heilman/gSSURGOsoil/soils/1km_UMW_satk", "100", "MEAN", "EXPAND", "DATA")
arcpy.gp.Aggregate_sa("mosaicsand.tif", "C:/Dropbox/GIS_Kelly/Kelly Heilman/gSSURGOsoil/soils/8km_UMW_sand", "800", "MEAN", "EXPAND", "DATA")
arcpy.gp.Aggregate_sa("mosaicsand.tif", "C:/Dropbox/GIS_Kelly/Kelly Heilman/gSSURGOsoil/soils/1km_UMW_sand", "100", "MEAN", "EXPAND", "DATA")

# now do the lookup for clay

arcpy.gp.Lookup_sa("MapunitRaster_wi_10m", "tbl_Total_Clay__Rep_Value_wtd_avg_0_30.claytotal_r", "C:/Users/paleolab/Documents/soils/gssurgo_g_wi/lookupclay")
arcpy.gp.Lookup_sa("MapunitRaster_mn_10m", "tbl_Total_Clay__Rep_Value_wtd_avg_0_30.claytotal_r", "C:/Users/paleolab/Documents/soils/gssurgo_g_mn/lookupclay")
arcpy.gp.Lookup_sa("MapunitRaster_il_10m", "tbl_Total_Clay__Rep_Value_wtd_avg_0_30.claytotal_r", "C:/Users/paleolab/Documents/soils/gssurgo_g_il/lookupclay")
arcpy.gp.Lookup_sa("MapunitRaster_in_10m", "tbl_Total_Clay__Rep_Value_wtd_avg_0_30.claytotal_r", "C:/Users/paleolab/Documents/soils/gssurgo_g_in/lookupclay")
arcpy.gp.Lookup_sa("MapunitRaster_mi_10m", "tbl_Total_Clay__Rep_Value_wtd_avg_0_30.claytotal_r", "C:/Users/paleolab/Documents/soils/gssurgo_g_mi/lookupclay")


#Mosaic All the CLAY rasters together
arcpy.MosaicToNewRaster_management(input_rasters="C:/Users/paleolab/Documents/soils/gssurgo_g_mn/lookupclay;C:/Users/paleolab/Documents/soils/gssurgo_g_in/lookupclay;C:/Users/paleolab/Documents/soils/gssurgo_g_wi/lookupclay;C:/Users/paleolab/Documents/soils/gssurgo_g_il/lookupclay;C:/Users/paleolab/Documents/soils/gssurgo_g_mi/lookupclay", output_location="C:/Dropbox/GIS_Kelly/Kelly Heilman/gSSURGOsoil/soils", raster_dataset_name_with_extension="mosaicclay.tif", coordinate_system_for_the_raster="", pixel_type="32_BIT_UNSIGNED", cellsize="", number_of_bands="1", mosaic_method="BLEND", mosaic_colormap_mode="FIRST")




# now do the lookup for silt

arcpy.gp.Lookup_sa("MapunitRaster_wi_10m", "tbl_Total_Silt__Rep_Value_wtd_avg_0_30.silttotal_r", "C:/Users/paleolab/Documents/soils/gssurgo_g_wi/lookupsilt")
arcpy.gp.Lookup_sa("MapunitRaster_mn_10m", "tbl_Total_Silt__Rep_Value_wtd_avg_0_30.silttotal_r", "C:/Users/paleolab/Documents/soils/gssurgo_g_mn/lookupsilt")
arcpy.gp.Lookup_sa("MapunitRaster_il_10m", "tbl_Total_Silt__Rep_Value_wtd_avg_0_30.silttotal_r", "C:/Users/paleolab/Documents/soils/gssurgo_g_il/lookupsilt")
arcpy.gp.Lookup_sa("MapunitRaster_in_10m", "tbl_Total_Silt__Rep_Value_wtd_avg_0_30.silttotal_r", "C:/Users/paleolab/Documents/soils/gssurgo_g_in/lookupsilt")
arcpy.gp.Lookup_sa("MapunitRaster_mi_10m", "tbl_Total_Silt__Rep_Value_wtd_avg_0_30.silttotal_r", "C:/Users/paleolab/Documents/soils/gssurgo_g_mi/lookupsilt")


#Mosaic All the SILT rasters together
arcpy.MosaicToNewRaster_management(input_rasters="C:/Users/paleolab/Documents/soils/gssurgo_g_mn/lookupsilt;C:/Users/paleolab/Documents/soils/gssurgo_g_in/lookupsilt;C:/Users/paleolab/Documents/soils/gssurgo_g_wi/lookupsilt;C:/Users/paleolab/Documents/soils/gssurgo_g_il/lookupsilt;C:/Users/paleolab/Documents/soils/gssurgo_g_mi/lookupsilt", output_location="C:/Dropbox/GIS_Kelly/Kelly Heilman/gSSURGOsoil/soils", raster_dataset_name_with_extension="mosaicsilt.tif", coordinate_system_for_the_raster="", pixel_type="32_BIT_UNSIGNED", cellsize="", number_of_bands="1", mosaic_method="BLEND", mosaic_colormap_mode="FIRST")



# now do the lookup for Organic matter

arcpy.gp.Lookup_sa("MapunitRaster_wi_10m", "tbl_Organic_Matter__Rep_Value_wtd_avg_0_30.om_r", "C:/Users/paleolab/Documents/soils/gssurgo_g_wi/lookupom")
arcpy.gp.Lookup_sa("MapunitRaster_mn_10m", "tbl_Organic_Matter__Rep_Value_wtd_avg_0_30.om_r", "C:/Users/paleolab/Documents/soils/gssurgo_g_mn/lookupom")
arcpy.gp.Lookup_sa("MapunitRaster_il_10m", "tbl_Organic_Matter__Rep_Value_wtd_avg_0_30.om_r", "C:/Users/paleolab/Documents/soils/gssurgo_g_il/lookupom")
arcpy.gp.Lookup_sa("MapunitRaster_in_10m", "tbl_Organic_Matter__Rep_Value_wtd_avg_0_30.om_r", "C:/Users/paleolab/Documents/soils/gssurgo_g_in/lookupom")
arcpy.gp.Lookup_sa("MapunitRaster_mi_10m", "tbl_Organic_Matter__Rep_Value_wtd_avg_0_30.om_r", "C:/Users/paleolab/Documents/soils/gssurgo_g_mi/lookupom")


#Mosaic All the OM rasters together
arcpy.MosaicToNewRaster_management(input_rasters="C:/Users/paleolab/Documents/soils/gssurgo_g_mn/lookupom;C:/Users/paleolab/Documents/soils/gssurgo_g_in/lookupom;C:/Users/paleolab/Documents/soils/gssurgo_g_wi/lookupom;C:/Users/paleolab/Documents/soils/gssurgo_g_il/lookupom;C:/Users/paleolab/Documents/soils/gssurgo_g_mi/lookupom", output_location="C:/Dropbox/GIS_Kelly/Kelly Heilman/gSSURGOsoil/soils", raster_dataset_name_with_extension="mosaicom.tif", coordinate_system_for_the_raster="", pixel_type="32_BIT_UNSIGNED", cellsize="", number_of_bands="1", mosaic_method="BLEND", mosaic_colormap_mode="FIRST")



# now do the lookup for Saturated hydraulic conductivity

arcpy.gp.Lookup_sa("MapunitRaster_wi_10m", "tbl_Saturated_Hydraulic_Conductivity__Rep_Value_wtd_avg_0_30.ksat_r", "C:/Users/paleolab/Documents/soils/gssurgo_g_wi/lookupksat")
arcpy.gp.Lookup_sa("MapunitRaster_mn_10m", "tbl_Saturated_Hydraulic_Conductivity__Rep_Value_wtd_avg_0_30.ksat_r", "C:/Users/paleolab/Documents/soils/gssurgo_g_mn/lookupksat")
arcpy.gp.Lookup_sa("MapunitRaster_il_10m", "tbl_Saturated_Hydraulic_Conductivity__Rep_Value_wtd_avg_0_30.ksat_r", "C:/Users/paleolab/Documents/soils/gssurgo_g_il/lookupksat")
arcpy.gp.Lookup_sa("MapunitRaster_in_10m", "tbl_Saturated_Hydraulic_Conductivity__Rep_Value_wtd_avg_0_30.ksat_r", "C:/Users/paleolab/Documents/soils/gssurgo_g_in/lookupksat")
arcpy.gp.Lookup_sa("MapunitRaster_mi_10m", "tbl_Saturated_Hydraulic_Conductivity__Rep_Value_wtd_avg_0_30.ksat_r", "C:/Users/paleolab/Documents/soils/gssurgo_g_mi/lookupksat")


#Mosaic All the KSAT rasters together
arcpy.MosaicToNewRaster_management(input_rasters="C:/Users/paleolab/Documents/soils/gssurgo_g_mn/lookupksat;C:/Users/paleolab/Documents/soils/gssurgo_g_in/lookupksat;C:/Users/paleolab/Documents/soils/gssurgo_g_wi/lookupksat;C:/Users/paleolab/Documents/soils/gssurgo_g_il/lookupksat;C:/Users/paleolab/Documents/soils/gssurgo_g_mi/lookupksat", output_location="C:/Dropbox/GIS_Kelly/Kelly Heilman/gSSURGOsoil/soils", raster_dataset_name_with_extension="mosaicksat.tif", coordinate_system_for_the_raster="", pixel_type="32_BIT_UNSIGNED", cellsize="", number_of_bands="1", mosaic_method="BLEND", mosaic_colormap_mode="FIRST")


#arcpy.gp.Aggregate_sa("lookupsand", "C:/Users/paleolab/Documents/soils/gssurgo_g_wi/1km_WI_sand", "100", "MEAN", "EXPAND", "DATA")

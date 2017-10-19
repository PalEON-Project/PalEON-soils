#Creating gssurgo rasters and aggregating to different grid cells
#Author: Kelly Heilman
#Date: 11/30/16

#This is done in Arcgis command line using mapunit 10m gssurgo rasters from NCRS geospatial gateway. These rasters are run through the Ssurgo on demand arcgis toolbox to create and join soil tables


# run the SDA properties tool (need gssurgo toolkiet) to get weighted averages for calcium carbonate & cation exchange capacity for each state:
arcpy.SDAPROPERTIES2(Soil_Survey_Areas="C:/Users/paleolab/Documents/soils/gssurgo_g_il/gSSURGO_IL.gdb/SAPOLYGON", Soil_Survey_Choicelist="IL001;IL003;IL005;IL007;IL009;IL011;IL013;IL015;IL017;IL019;IL021;IL023;IL025;IL027;IL029;IL031;IL033;IL035;IL037;IL039;IL041;IL043;IL045;IL047;IL049;IL051;IL053;IL055;IL057;IL059;IL061;IL063;IL065;IL067;IL069;IL071;IL073;IL075;IL077;IL079;IL081;IL083;IL085;IL087;IL089;IL091;IL093;IL095;IL097;IL099;IL101;IL103;IL105;IL107;IL109;IL111;IL113;IL115;IL117;IL119;IL121;IL123;IL125;IL127;IL129;IL131;IL133;IL135;IL137;IL139;IL141;IL143;IL145;IL147;IL149;IL151;IL153;IL155;IL157;IL159;IL161;IL163;IL165;IL167;IL169;IL171;IL173;IL175;IL177;IL179;IL181;IL183;IL185;IL187;IL189;IL191;IL193;IL195;IL197;IL199;IL201;IL203", Aggregation_Method="Weighted Average", Soil_Property="'Calcium Carbonate - Rep Value';'Cation Exchange Capcity - Rep Value'", Top_Depth="0", Bottom_Depth="30", Min_Max="", Output_File_Geodatabase="C:/Users/paleolab/Documents/soils/gssurgo_g_il/gSSURGO_IL.gdb", Join_Layer="")
arcpy.SDAPROPERTIES2(Soil_Survey_Areas="C:/Users/paleolab/Documents/soils/gssurgo_g_in/gSSURGO_IN.gdb/SAPOLYGON", Soil_Survey_Choicelist="IN001;IN003;IN005;IN007;IN009;IN011;IN013;IN015;IN017;IN019;IN021;IN023;IN025;IN027;IN029;IN031;IN033;IN035;IN037;IN039;IN041;IN043;IN045;IN047;IN049;IN051;IN053;IN055;IN057;IN059;IN061;IN063;IN065;IN067;IN069;IN071;IN073;IN075;IN077;IN079;IN081;IN083;IN085;IN087;IN089;IN091;IN093;IN095;IN097;IN099;IN101;IN103;IN105;IN107;IN109;IN111;IN113;IN115;IN117;IN119;IN121;IN123;IN125;IN127;IN129;IN131;IN133;IN135;IN137;IN139;IN141;IN143;IN145;IN147;IN149;IN151;IN153;IN155;IN157;IN159;IN161;IN163;IN165;IN167;IN169;IN171;IN173;IN175;IN177;IN179;IN181;IN183", Aggregation_Method="Weighted Average", Soil_Property="'Calcium Carbonate - Rep Value';'Cation Exchange Capcity - Rep Value'", Top_Depth="0", Bottom_Depth="30", Min_Max="", Output_File_Geodatabase="C:/Users/paleolab/Documents/soils/gssurgo_g_in/gSSURGO_IN.gdb", Join_Layer="")
arcpy.SDAPROPERTIES2(Soil_Survey_Areas="C:/Users/paleolab/Documents/soils/gssurgo_g_mn/gSSURGO_MN.gdb/SAPOLYGON", Soil_Survey_Choicelist="MN001;MN003;MN005;MN007;MN009;MN011;MN013;MN015;MN017;MN019;MN021;MN023;MN025;MN027;MN029;MN031;MN033;MN035;MN037;MN039;MN041;MN043;MN045;MN047;MN049;MN051;MN053;MN055;MN057;MN059;MN061;MN063;MN065;MN067;MN069;MN073;MN075;MN077;MN079;MN081;MN083;MN085;MN087;MN089;MN091;MN093;MN095;MN097;MN099;MN101;MN103;MN105;MN107;MN109;MN111;MN113;MN115;MN117;MN119;MN121;MN123;MN125;MN127;MN129;MN131;MN133;MN135;MN139;MN141;MN143;MN145;MN147;MN149;MN151;MN153;MN155;MN157;MN159;MN161;MN163;MN165;MN167;MN169;MN171;MN173;MN613;MN615;MN617;MN619;MN621;MN625;MN627", Aggregation_Method="Weighted Average", Soil_Property="'Calcium Carbonate - Rep Value';'Cation Exchange Capcity - Rep Value'", Top_Depth="0", Bottom_Depth="30", Min_Max="", Output_File_Geodatabase="C:/Users/paleolab/Documents/soils/gssurgo_g_mn/gSSURGO_MN.gdb", Join_Layer="")



# Here we are processing for sand 
#lookup creates a new raster with the selected field (2nd argument) as the value for the raster
# Replace a layer/table view name with a path to a dataset (which can be a layer file) or create the layer/table view within the script
# The following inputs are layers or table views: "MapunitRaster_wi_10m"
arcpy.gp.Lookup_sa("MapunitRaster_wi_10m", "tbl_Total_Sand__Rep_Value_wtd_avg_0_30.sandtotal_r", "C:/Users/paleolab/Documents/soils/gssurgo_g_wi/lookupsand")
arcpy.gp.Lookup_sa("MapunitRaster_mn_10m", "tbl_Total_Sand__Rep_Value_wtd_avg_0_30.sandtotal_r", "C:/Users/paleolab/Documents/soils/gssurgo_g_mn/lookupsand")
arcpy.gp.Lookup_sa("MapunitRaster_il_10m", "tbl_Total_Sand__Rep_Value_wtd_avg_0_30.sandtotal_r", "C:/Users/paleolab/Documents/soils/gssurgo_g_il/lookupsand")
arcpy.gp.Lookup_sa("MapunitRaster_in_10m", "tbl_Total_Sand__Rep_Value_wtd_avg_0_30.sandtotal_r", "C:/Users/paleolab/Documents/soils/gssurgo_g_in/lookupsand")
arcpy.gp.Lookup_sa("MapunitRaster_mi_10m", "tbl_Total_Sand__Rep_Value_wtd_avg_0_30.sandtotal_r", "C:/Users/paleolab/Documents/soils/gssurgo_g_mi/lookupsand")


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
arcpy.gp.Aggregate_sa("lookupCEC", "C:/Users/paleolab/Documents/soils/gssurgo_g_wi/8km_wi_cec", "800", "MEAN", "EXPAND", "DATA")
arcpy.gp.Aggregate_sa("lookupCEC", "C:/Users/paleolab/Documents/soils/gssurgo_g_mn/8km_mn_cec", "800", "MEAN", "EXPAND", "DATA")
arcpy.gp.Aggregate_sa("lookupCEC", "C:/Users/paleolab/Documents/soils/gssurgo_g_il/8km_il_cec", "800", "MEAN", "EXPAND", "DATA")
arcpy.gp.Aggregate_sa("lookupCEC", "C:/Users/paleolab/Documents/soils/gssurgo_g_in/8km_in_cec", "800", "MEAN", "EXPAND", "DATA")
arcpy.gp.Aggregate_sa("lookupCEC", "C:/Users/paleolab/Documents/soils/gssurgo_g_mi/8km_mi_sand", "800", "MEAN", "EXPAND", "DATA")

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
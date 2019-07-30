########################################
##Project: PalEON-soils, GJAM
##Script Purpose: Aggregate Soil data from USDA in ARCGIS using Python commands
##Date: Friday May 30, 12:56:00 2019
##Author: Henri Chung, Kelly Heilman
##Revisions:
########################################

#Copy and paste this script into the python terminal in ARCGIS *AFTER* Adding the MapUnitRaster_10m object 
#And aggregation file from GGSURGO_aggregation.R


###WARNING#### Sometimes ARCGIS reads in the component table as a STRING instead of number, the fix is to manually change 
##the columns names in excel for the offending component table to append "_s", and then use the var loop in the second code lbock


#Script to aggregate USDA geospatial data
filedir = "C:/Users/paleolab/Documents/soils/data/" #Where final data is to be exported.
filedir = "E:/Kelly/soils/"
#Set up initial arguments
N = "2" #When ARCGIS copies a data table, it exports it as "Export_Output_N as default
state = "NY" #State for current map
tablename = "Export_Output_" + N
raster10m =  "MapunitRaster_10m" #Default file name in USDA data, do not change.
N1 = N + "." #Some file paths require Export_Outout_N. instead
tablename1 = "Export_Output_" + N1
params = ["sand", "silt", "clay", "cec7", "caco3", "water_stor", "ksat"] #Parameters to loops over.


#Add duplicate text field with called mukey_s
arcpy.AddField_management(in_table=tablename, field_name="mukey_s", field_type="TEXT", field_precision="", field_scale="", field_length="", field_alias="", field_is_nullable="NULLABLE", field_is_required="NON_REQUIRED", field_domain="")
#Fill mukey_s with original mukey but as a text value
arcpy.CalculateField_management(in_table=tablename, field="mukey_s", expression="!mukey!", expression_type="PYTHON_9.3", code_block="")

#Join to 10m raster using mukey_s field
arcpy.AddJoin_management(in_layer_or_view=raster10m, in_field="MUKEY", join_table=tablename, join_field="mukey_s", join_type="KEEP_ALL")

filedir = "E:/Kelly/soils/"
params = ["cec7", "silt", "clay", "caco3", "water_stor", "ksat", "sand"]
#Loop uver aggregation and write files to file dir.
for val in params:
  arcpy.gp.Lookup_sa( raster10m , tablename1+val, filedir + "lookup" + val[:3] + state )
  arcpy.gp.Aggregate_sa("lookup" + val[:3]  + state, filedir + state + "1km_" + val[:3], "100", "MEAN", "EXPAND", "DATA")
  arcpy.gp.Aggregate_sa("lookup" + val[:3]  + state, filedir + state + "8km_" + val[:3], "800", "MEAN", "EXPAND", "DATA")


####
#Mosaic the midwest
dist = ["100", "800"]
params = ["sand", "silt", "clay", "cec7", "caco3", "water_stor", "ksat"]
filepath = "E:/Kelly/soils"
for val in dist:
	for var in params:
		x = filepath+"/Indiana/lookup"+var[:3]+"in;"+filepath+"/Wisconsin/lookup"+var[:3]+"wi;"+filepath+"/Illinois/lookup"+var[:3]+"il;"+filepath+"/Michigan/lookup"+var[:3]+"mi;"+filepath+"/Minnesota/lookup"+var[:3]+"mn"
		arcpy.MosaicToNewRaster_management(input_rasters=x, output_location="E:/Kelly/soils", raster_dataset_name_with_extension="mosaic"+ var + ".tif", coordinate_system_for_the_raster="", pixel_type="32_BIT_FLOAT", cellsize="", number_of_bands="1", mosaic_method="BLEND", mosaic_colormap_mode="FIRST")
		arcpy.gp.Aggregate_sa("mosaic"+var+".tif", "E:/Kelly/soils/fs_"+val[:1] +"_km_"+var[:3], val, "MEAN", "EXPAND", "DATA")


#Mosaic all the states.
dist = ["100", "800"]
params = ["sand", "silt", "clay", "cec7", "caco3", "water_stor", "ksat"]
filepath = "E:/Kelly/soils"
for val in dist:
	for var in params:
		#x = filepath+"/Minnesota/lookup"+var[:3]+"mn;" +filepath+"/Indiana/lookup"+var[:3]+"in;"+filepath+"/Wisconsin/lookup"+var[:3]+"wi;"+filepath+"/Illinois/lookup"+var[:3]+"il;"+filepath+"/Michigan/lookup"+var[:3]+"mi;" +filepath+"/Pennslyvania/lookup"+var[:3]+"pa;"+filepath+"/New York/lookup"+var[:3]+"ny;"+filepath+"/New Jersey/lookup"+var[:3]+"nj;"+filepath+"/Massachusetts/lookup"+var[:3]+"ma;"+filepath+"/Vermont/lookup"+var[:3]+"vt;"+filepath+"/New Hampshire/lookup"+var[:3]+"nh;"+filepath+"/Maine/lookup"+var[:3]+"me;"+filepath+"/Connecticut/lookup"+var[:3]+"ct;"+filepath+"/Rhode Island/lookup"+var[:3]+"ri;"+filepath+"/Delaware/lookup"+var[:3]+"de;"+filepath+"/Ohio/lookup"+var[:3]+"oh;"+filepath+"/Pennsylvania/lookup"+var[:3]+"pa"
		arcpy.MosaicToNewRaster_management(input_rasters=x, output_location="E:/Kelly/soils", raster_dataset_name_with_extension="kevmos"+ var + ".tif", coordinate_system_for_the_raster="", pixel_type="32_BIT_FLOAT", cellsize="", number_of_bands="1", mosaic_method="BLEND", mosaic_colormap_mode="FIRST")
	arcpy.gp.Aggregate_sa("kevmos"+var+".tif", "E:/Kelly/soils/kev_"+val[:1] +"_km_"+var[:3], val, "MEAN", "EXPAND", "DATA")




#This section is the same as above but the filepaths are listed as a list for readability
dist = ["100", "800"]
params = ["sand", "silt", "clay", "cec7", "caco3", "water_stor", "ksat"]
filepath = "E:/Kelly/soils"
for val in dist:
	for var in params:
		#x = filepath+"/Minnesota/lookup"+var[:3]+"mn;" +filepath+"/Indiana/lookup"+var[:3]+"in;"+filepath+"/Wisconsin/lookup"+var[:3]+"wi;"+filepath+"/Illinois/lookup"+var[:3]+"il;"+filepath+"/Michigan/lookup"+var[:3]+"mi;" +filepath+"/Pennslyvania/lookup"+var[:3]+"pa;"+filepath+"/New York/lookup"+var[:3]+"ny;"+filepath+"/New Jersey/lookup"+var[:3]+"nj;"+filepath+"/Massachusetts/lookup"+var[:3]+"ma;"+filepath+"/Vermont/lookup"+var[:3]+"vt;"+filepath+"/New Hampshire/lookup"+var[:3]+"nh;"+filepath+"/Maine/lookup"+var[:3]+"me;"+filepath+"/Connecticut/lookup"+var[:3]+"ct;"+filepath+"/Rhode Island/lookup"+var[:3]+"ri;"+filepath+"/Delaware/lookup"+var[:3]+"de;"+filepath+"/Ohio/lookup"+var[:3]+"oh;"+filepath+"/Pennsylvania/lookup"+var[:3]+"pa"
		arcpy.MosaicToNewRaster_management(input_rasters=x, output_location="E:/Kelly/soils", raster_dataset_name_with_extension="kevmos"+ var + ".tif", coordinate_system_for_the_raster="", pixel_type="32_BIT_FLOAT", cellsize="", number_of_bands="1", mosaic_method="BLEND", mosaic_colormap_mode="FIRST")
	arcpy.gp.Aggregate_sa("kevmos"+var+".tif", "E:/Kelly/soils/kev_"+val[:1] +"_km_"+var[:3], val, "MEAN", "EXPAND", "DATA")

		x = filepath+"/Minnesota/lookup"+var[:3]+"mn;"+
			filepath+"/Indiana/lookup"+var[:3]+"in;"+
			filepath+"/Wisconsin/lookup"+var[:3]+"wi;"+
			filepath+"/Illinois/lookup"+var[:3]+"il;"+
			filepath+"/Michigan/lookup"+var[:3]+"mi;" +
			filepath+"/Pennslyvania/lookup"+var[:3]+"pa;"+
			filepath+"/New York/lookup"+var[:3]+"ny;"+
			filepath+"/New Jersey/lookup"+var[:3]+"nj;"+
			filepath+"/Massachusetts/lookup"+var[:3]+"ma;"+
			filepath+"/Vermont/lookup"+var[:3]+"vt;"+
			filepath+"/New Hampshire/lookup"+var[:3]+"nh;"+
			filepath+"/Maine/lookup"+var[:3]+"me;"+
			filepath+"/Connecticut/lookup"+var[:3]+"ct;"+
			filepath+"/Rhode Island/lookup"+var[:3]+"ri;"+
			filepath+"/Delaware/lookup"+var[:3]+"de;"+
			filepath+"/Ohio/lookup"+var[:3]+"oh;"+
			filepath+"/Pennsylvania/lookup"+var[:3]+"pa"




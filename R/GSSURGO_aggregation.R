# GSSURGO_aggregation.R
# Author: K.Heilman
# Date: 5/28/19
# 
# this script reads in and join the appropriate gssurgo tables to get soil characteristics.
# the output component table needs to be joined to the 10m gssurgo rasters by state level
# downloaded state level data from:https://datagateway.nrcs.usda.gov/GDGOrder.aspx?order=QuickState

#library(plyr)
library(raster)
library(foreign)
require(rgdal)
library(dplyr)

#workingdir <- "/Users/kah/Documents/PalEON-soils/"
workingdir <- "C:/Users/paleolab/Documents/soils/gssurgo_g_il/"

setwd(workingdir)
# The input file geodatabase
state <- "IL" # just change this for each state
fgdb <-  paste0("gSSURGO_",state,".gdb") # you should have the state level gssurgo .gdb saved in a datafolder

# List all feature classes in a file geodatabase
subset(ogrDrivers(), grepl("GDB", name))
fc_list <- ogrListLayers(fgdb)
print(fc_list)


# read in the appropriate tables for chorizon and component:
chorizon <- sf::st_read(dsn = fgdb, layer = "chorizon")
component <- sf::st_read(dsn = fgdb, layer = "component")
mapunit <- sf::st_read(dsn = fgdb, layer = "mapunit")

summary(chorizon)
summary(component)
summary(mapunit)

#polygons <- readOGR(dsn = fgdb, layer = "MUPOLYGON")

# only keep some of the columns from the component table
component.subset <- component[,c('mukey','cokey','comppct_r')]


# using handy functions to do soil aggregation from: https://casoilresource.lawr.ucdavis.edu/software/r-advanced-statistical-package/aggregating-ssurgo-data-r/
# custom function for calculating a weighted mean
# values passed in should be vectors of equal length
# note KH added addditional soil variables that we might be interested in to the component_level aggregation function

wt_mean <- function(property, weights)
{
  # compute thickness weighted mean, but only when we have enough data
  # in that case return NA
  
  # save indices of data that is there
  property.that.is.na <- which( is.na(property) )
  property.that.is.not.na <- which( !is.na(property) )
  
  if( length(property) - length(property.that.is.na) >= 1)
    prop.aggregated <- sum(weights[property.that.is.not.na] * property[property.that.is.not.na], na.rm=TRUE) / sum(weights[property.that.is.not.na], na.rm=TRUE)
  else
    prop.aggregated <- NA
  
  return(prop.aggregated)
}

profile_total <- function(property, thickness)
{
  # compute profile total
  # in that case return NA
  
  # save indices of data that is there
  property.that.is.na <- which( is.na(property) )
  property.that.is.not.na <- which( !is.na(property) )
  
  if( length(property) - length(property.that.is.na) >= 1)
    prop.aggregated <- sum(thickness[property.that.is.not.na] * property[property.that.is.not.na], na.rm=TRUE)
  else
    prop.aggregated <- NA
  
  return(prop.aggregated)
}

# define a function to perfom hz-thickness weighted aggregtion
component_level_aggregation <- function(i)
{
  
  # horizon thickness is our weighting vector
  hz_thick <- i$hzdepb_r - i$hzdept_r
  
  # compute wt.mean aggregate values
  clay <- wt_mean(i$claytotal_r, hz_thick)
  silt <- wt_mean(i$silttotal_r, hz_thick)
  sand <- wt_mean(i$sandtotal_r, hz_thick)
  ksat <- wt_mean(i$ksat_r, hz_thick)
  caco3 <- wt_mean(i$caco3_r, hz_thick)
  cec7 <- wt_mean(i$cec7_r, hz_thick)
  
  # compute profile sum values
  water_storage <- profile_total(i$awc_r, hz_thick)
  
  # make a new dataframe out of the aggregate values
  d <- data.frame(cokey=unique(i$cokey), clay=clay, silt=silt, sand=sand, water_storage=water_storage, 
                  ksat = ksat, caco3 = caco3, cec7)
  
  return(d)
}

mapunit_level_aggregation <- function(i)
{
  # component percentage is our weighting vector
  comppct <- i$comppct_r
  
  # wt. mean by component percent
  clay <- wt_mean(i$clay, comppct)
  silt <- wt_mean(i$silt, comppct)
  sand <- wt_mean(i$sand, comppct)
  ksat <- wt_mean(i$ksat, comppct)
  caco3 <- wt_mean(i$caco3, comppct)
  cec7 <- wt_mean(i$cec7, comppct)
  
  water_storage <- wt_mean(i$water_storage, comppct)
  
  # make a new dataframe out of the aggregate values
  d <- data.frame(mukey=unique(i$mukey), clay=clay, silt=silt, sand=sand, 
                  water_storage=water_storage, ksat = ksat, caco3 = caco3, cec7 = cec7)
  
  return(d)
}





# here we calculated means of variables weighted by soil horizon depth (see component_level_aggregation function):
# aggregate horizon data to the component level 
chorizon.agg <- chorizon %>% group_by(cokey) %>% do(component_level_aggregation(.)) # using do with dplyr is much faster than plyr ddply

# join up the aggregate chorizon data to the component table
comp.merged <- merge(component.subset, chorizon.agg, by='cokey')

# aggregate component data to the map unit level and calculated weighted means by the components
component.agg <- comp.merged %>% group_by(mukey) %>% do(mapunit_level_aggregation(.))

component.agg$mukey <- as.character(component.agg$mukey)
component.agg$OID <- as.character(1:length(component.agg$mukey))

# save to 
savedir <- "C:/Users/paleolab/Documents/soils/"
# save data back to a csv
write.csv(component.agg, file=paste0(savedir, 'data/component_tables/',state,'_component_agg.csv'), row.names=FALSE)

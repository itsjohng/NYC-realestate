#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
'Zoning' function. Create a grid over NYC (Manhattan only, currently) 
Arguments: Takes in zone size, 1000 = 1000FT square.
Output dictionary with x_y : (long, lat) , (long,lat) format. First tuple is 'SW' corner of zone
second tuple is 'NE' corner of zone.
Relevant dims... approx NYC block size 260x1000
"""
def zonebuilder(sqft):
    strt_lat = 40.680205
    strt_long = -74.051349
    end_lat = 40.87993
    end_long = -73.906877
    tot_lat = .199725
    tot_long = .144472
    tot_ns_ft = 72945.193
    tot_ew_ft = 40009.651
    lat_in_ft = 365228.153711353110527
    long_in_ft = 276937.060468464477546
    z_quant_long = int((tot_ew_ft // sqft) + 1)
    z_quant_lat = int((tot_ns_ft // sqft) + 1)
    zones = {}
    for x in range(0,z_quant_long):
        strt_zone_long = ((x*sqft)/long_in_ft) + strt_long
        end_zone_long = (((x+1)*sqft)/long_in_ft) + strt_long
        for y in range(0, z_quant_lat):            
            strt_zone_lat = ((y*sqft)/lat_in_ft) + strt_lat
            end_zone_lat = (((y+1)*sqft)/lat_in_ft) + strt_lat
            zones[str(x)+'_'+str(y)] = (strt_zone_long, strt_zone_lat) , (end_zone_long, end_zone_lat)   
    return zones

def zoneapplier(coords):
    zones = zonebuilder(2000)
    for zone,cds in zones.items():
        if (coords[0] >= cds[0][0]) & (coords[0] < cds[1][0]) & (coords[1] >= cds[0][1]) & (coords[1] < cds[1][1]):
            return(zone)
'''
Created on 26 Jun 2018

@author: arun koshy 
'''

'''
Created on 14 Jun 2018

@author: cogarukoshy
'''

import pandas as pd
import json
import openweathermapy.core as owm
import logging
import argparse
import datetime
import os
from time import gmtime, strftime

def parse_command_line_options():
    """
    Parses arguments from the command line and returns them in the form of an ArgParser object.
    """
    parser = argparse.ArgumentParser(description="Query the Weather Data for every John Lewis store using LONG and LAT")
    parser.add_argument('--weather_api_id', type=str, help='log file path for weather data use case')
    parser.add_argument('--logfile_path', type=str, help='log file path for weather data use case')
    parser.add_argument('--jlp_store_details', type=str, help='Input file contains information about JLP stores')
    parser.add_argument('--output_weather_data', type=str, help='Path for weather data storage')
    parser.add_argument('--weather_type', type=str, help='Current weather or forcast')
    parser.add_argument('--gs_bucket_path', type=str, help='Google storage bucket')
    parser.add_argument('--gs_folder_loc', type=str, help='Folder in Google storage bucket')

    return parser.parse_args()

def main(args):
    settings = {"APPID": args.weather_api_id, "units": "metric"}
    file_ext = datetime.datetime.now().strftime("%Y%m%d%H")
    logging.basicConfig(filename=args.logfile_path+"weatherdata"+file_ext+".log", level=logging.INFO)

    # open output file for weather data
    output_file_name = args.output_weather_data+"current_wdata_"+str(file_ext)+".json"


    if args.weather_type == "current":
        with open(output_file_name, "w") as daily_outfile:           
            weather_data = owm.get_current('London', **settings)
            logging.info("WeatherApi Call for london")
            json.dump(weather_data, daily_outfile, indent=2)
            daily_outfile.write("\n")
        print("Current Weather data loaded for London")
    else:
        logging.info("Invalid weather_type function")
        print("Invalid weather_type function")
    return output_file_name

def copyToGS(args1,opfile):
    os.system("gsutil mv "+args1.output_weather_data+"/"+opfile+" "+args1.gs_bucket_path + args1.gs_folder_loc)
   

if __name__ == '__main__':
    args = parse_command_line_options()
    outputfile = main(args)
    logging.info("-------------- Copying files to Google Cloud ---------- ")
    copyToGS(args,outputfile)
    logging.info("Done")
    pass
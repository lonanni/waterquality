import pandas as pd
import matplotlib.pyplot as plt
import numpy as np


def loc_subset(df, place, location_type="label"):
	"""
	Return a subsample of the main dataset, according to the location of interest

	input:
	df (DataFrame object)
	location_label (str): the location of interest, e.g. "langstone" or "SO-G00"; empty string "" return entire catalogue
	location_type (str): either "label" (e.g. "langstone", "portsmouth") or "notation" (e.g. "SO-G00", "SW-Z94")
	
	output:
	df_subset (DataFrame object)

	.. warning:: 
	Performs **no** checks of the input.

	"""

	if location_type == "label":

		locations = set(df['sample.samplingPoint.label'])
        
		if np.size(place)>1:
			location_condition = [x for x in locations if place[0] in x.lower()]
			df_subset = df.loc[df['sample.samplingPoint.label'].isin(location_condition)].copy()
			for place_ in place[1:]:
				location_condition = [x for x in locations if place_ in x.lower()]
				df_subset_0 = df.loc[df['sample.samplingPoint.label'].isin(location_condition)].copy()

				df_subset = pd.concat([df_subset, df_subset_0])
                
		else:     

			location_condition = [x for x in locations if place.lower() in x.lower()]
			df_subset = df.loc[df['sample.samplingPoint.label'].isin(location_condition)].copy()
	if location_type == "notation":
   
		locations_notations = set(df['sample.samplingPoint.notation'])
        
		if np.size(place)>1:
			location_condition = [x for x in locations_notations if place[0] in x.lower()]
			df_subset = df.loc[df['sample.samplingPoint.notation'].isin(location_condition)].copy()
			for place_ in place[1:]:
				location_condition = [x for x in locations_notations if place_.lower() in x.lower()]
				df_subset_0 = df.loc[df['sample.samplingPoint.notation'].isin(location_condition)].copy()
				df_subset = pd.concat([df_subset, df_subset_0])
		else:     
			location_condition = [x for x in locations_notations if place.lower() in x.lower()]
			df_subset = df.loc[df['sample.samplingPoint.notation'].isin(location_condition)].copy()

	return df_subset


def nutrient_time(df, location, nutrient_determinand, location_type="label"):
	"""
	Return a plot nutrient VS time for a given location, diveded or not into winter (oct-march) and summer (apr-sept).
	
	input:
	df (DataFrame object)
	location (str): the location of interest, e.g. "langstone"; empty string "" return entire catalogue
	nutrient_determinand (int): the determinant of the nutrient, e.g. 118 for Nitrite (N), mg/l
	ax(Axes object)
	seasons (bool): False (no distinction in seasons); True (divided into seasons)
	location_type (str): either "label" (e.g. "langstone", "portsmouth") or "notation" (e.g. "SO-G00", "SW-Z94")
	
	output:
	ax (Axes object)
	"""
	df_env = loc_subset(df, location, location_type)
	df_env.loc[:,"Date"] = pd.to_datetime(df_env['sample.sampleDateTime']).dt.date
    
	if np.size(nutrient_determinand)>1:
		time = []
		nutrients = []
		for n in nutrient_determinand:
			time.append(df_env[df_env['determinand.notation'] == n].sort_values(by="Date", ascending=True)['Date'])
			nutrients.append(df_env[df_env['determinand.notation'] == n].sort_values(by="Date", ascending=True)['result'])
		time = np.concatenate(time).flatten()
		nutrient = np.concatenate(nutrients).flatten()
	else:
		time = df_env[df_env['determinand.notation'] ==nutrient_determinand].sort_values(by="Date", ascending=True)['Date']
		nutrient = df_env[df_env['determinand.notation'] ==nutrient_determinand].sort_values(by="Date", ascending=True)['result']
	return(time, nutrient)
    
    
	
	

def nutrient_time_seasons(df, location, nutrient_determinand, location_type="label"):	
	"""
	Return a plot nutrient VS time for a given location, diveded or not into winter (oct-march) and summer (apr-sept).
	
	input:
	df (DataFrame object)
	location (str): the location of interest, e.g. "langstone"; empty string "" return entire catalogue
	nutrient_determinand (int): the determinant of the nutrient, e.g. 118 for Nitrite (N), mg/l
	ax(Axes object)
	seasons (bool): False (no distinction in seasons); True (divided into seasons)
	location_type (str): either "label" (e.g. "langstone", "portsmouth") or "notation" (e.g. "SO-G00", "SW-Z94")
	
	output:
	ax (Axes object)
	"""
	

	df_env_summer = loc_subset(df.loc[(df["month"]>4)&(df["month"]<9)], location, location_type)
	df_env_summer.loc[:,"Date"] = pd.to_datetime(df_env_summer['sample.sampleDateTime']).dt.date

	df_env_winter = loc_subset(df.loc[np.logical_or(df["month"]<4,df["month"]>9)], location, location_type)
	df_env_winter.loc[:,"Date"] = pd.to_datetime(df_env_winter['sample.sampleDateTime']).dt.date
    
    
	if np.size(nutrient_determinand)>1:
		time_summer = []
		nutrients_summer = []
		time_winter = []
		nutrients_winter = []
		for n in nutrient_determinand:
			time_summer.append(df_env_summer[df_env_summer['determinand.notation'] == n].sort_values(by="Date", ascending=True)['Date'])
			nutrients_summer.append(df_env_summer[df_env_summer['determinand.notation'] == n].sort_values(by="Date", ascending=True)['result'])
            
			time_winter.append(df_env_winter[df_env_winter['determinand.notation'] == n].sort_values(by="Date", ascending=True)['Date'])
			nutrients_winter.append(df_env_winter[df_env_winter['determinand.notation'] == n].sort_values(by="Date", ascending=True)['result'])
        
		time_summer = np.concatenate(time_summer).flatten()
		nutrients_summer = np.concatenate(nutrients_summer).flatten()
        
		time_winter = np.concatenate(time_winter).flatten()
		nutrients_winter = np.concatenate(nutrients_winter).flatten()
	else:
		time_summer = df_env_summer[df_env_summer['determinand.notation'] ==nutrient_determinand].sort_values(by="Date", ascending=True)['Date']
		nutrients_summer = df_env_summer[df_env_summer['determinand.notation'] ==nutrient_determinand].sort_values(by="Date", ascending=True)['result']
		time_winter = df_env_winter[df_env_winter['determinand.notation'] ==nutrient_determinand].sort_values(by="Date", ascending=True)['Date']
		nutrients_winter = df_env_winter[df_env_winter['determinand.notation'] ==nutrient_determinand].sort_values(by="Date", ascending=True)['result']
	return(time_summer, nutrients_summer, time_winter, nutrients_winter)

		

	
	
def DAIN_time(df, location, location_type="label"):
	df_env =  loc_subset(df,  location, location_type)
	df_env.loc[:,"Date"] = pd.to_datetime(df_env['sample.sampleDateTime']).dt.date
	
	df_NA = df_env[(df_env["determinand.notation"]==116)|(df_env["determinand.notation"]==9943)|(df_env["determinand.notation"]==111)|(df_env["determinand.notation"]==119)]
	dain = df_NA.groupby("Date")["result"].sum().reset_index()
	date_ = dain["Date"]
	dain_ = dain["result"]	
				
	return(dain_, date_)
		
def DAIN_time_seasons(df, location, location_type="label"):
	df_env_summer =  loc_subset(df.loc[(df["month"]>4)&(df["month"]<9)], location, location_type)
	df_env_summer.loc[:,"Date"] = pd.to_datetime(df_env_summer['sample.sampleDateTime']).dt.date

	df_NA_summer = df_env_summer[(df_env_summer["determinand.notation"]==116)|(df_env_summer["determinand.notation"]==9943)|(df_env_summer["determinand.notation"]==111)|(df_env_summer["determinand.notation"]==119)]
	dain_summer = df_NA_summer.groupby("Date")["result"].sum().reset_index()
	date_summer = dain_summer["Date"]
	dain_summer = dain_summer["result"]
	
	
	df_env_winter =  loc_subset(df.loc[np.logical_or(df["month"]<4,df["month"]>9)], location, location_type)
	df_env_winter.loc[:,"Date"] = pd.to_datetime(df_env_winter['sample.sampleDateTime']).dt.date
		
	df_NA_winter = df_env_winter[(df_env_winter["determinand.notation"]==116)|(df_env_winter["determinand.notation"]==9943)|(df_env_winter["determinand.notation"]==111)|(df_env_winter["determinand.notation"]==119)]
	dain_winter = df_NA_winter.groupby("Date")["result"].sum().reset_index()
	date_winter = dain_winter["Date"]
	dain_winter = dain_winter["result"]
	return(date_summer, dain_summer, date_winter, dain_winter)

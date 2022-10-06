import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

def loc_subset(df, location, location_type="label"):

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
		location_condition = [x for x in locations if location.lower() in x.lower()]
		df_subset = df.loc[df['sample.samplingPoint.label'].isin(location_condition)].copy()

	if location_type == "notation":
    
		locations_notations = set(df['sample.samplingPoint.notation'])
		location_condition = [x for x in locations_notations if location.lower() in x.lower()]
		df_subset = df.loc[df['sample.samplingPoint.notation'].isin(location_condition)].copy()	
	
	return df_subset
	
	
def nutrient_time(df, location, nutrient_determinand, location_type="label", seasons=False):
	
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
	
	if seasons is False:
		df_env = loc_subset(df, location, location_type)
		df_env.loc[:,"Date"] = pd.to_datetime(df_env['sample.sampleDateTime']).dt.date
		
		time = df_env[df_env['determinand.notation'] ==nutrient_determinand].sort_values(by="Date", ascending=True)['Date']
		nutrient = df_env[df_env['determinand.notation'] ==nutrient_determinand].sort_values(by="Date", ascending=True)['result']
		return(time, nutrient)

	if seasons is True:
		df_env_summer =  loc_subset(df.loc[(df["month"]>4)&(df["month"]<9)], location, location_type)
		df_env_summer.loc[:,"Date"] = pd.to_datetime(df_env_summer['sample.sampleDateTime']).dt.date

		time_summer = df_env_summer[df_env_summer['determinand.notation'] ==nutrient_determinand].sort_values(by="Date", ascending=True)['Date']
		nutrient_summer = df_env_summer[df_env_summer['determinand.notation'] ==nutrient_determinand].sort_values(by="Date", ascending=True)['result']
		df_env_winter =  loc_subset(df.loc[np.logical_or(df["month"]<4,df["month"]>9)], location, location_type)
		df_env_winter.loc[:,"Date"] =pd.to_datetime(df_env_winter['sample.sampleDateTime']).dt.date

		time_winter = df_env_winter[df_env_winter['determinand.notation'] ==nutrient_determinand].sort_values(by="Date", ascending=True)['Date']
		nutrient_winter = df_env_winter[df_env_winter['determinand.notation'] ==nutrient_determinand].sort_values(by="Date", ascending=True)['result']		

		return(time_summer, nutrient_summer, time_winter, nutrient_winter)
		
def nutrient_time_nutrients(df, location, nutrients_list, location_type="label", seasons=False):
	
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
	
	if seasons is False:
		df_env = loc_subset(df, location, location_type)
		df_env.loc[:,"Date"] = pd.to_datetime(df_env['sample.sampleDateTime']).dt.date
		time = []
		nutrients = []
		for n in nutrients_list:

			time.append(df_env[df_env['determinand.notation'] == n].sort_values(by="Date", ascending=True)['Date'])
			nutrients.append(df_env[df_env['determinand.notation'] == n].sort_values(by="Date", ascending=True)['result'])

		return(np.concatenate(time).flatten(), np.concatenate(nutrients).flatten())

	if seasons is True:
		df_env_summer =  loc_subset(df.loc[(df["month"]>4)&(df["month"]<9)], location, location_type)
		df_env_summer.loc[:,"Date"] = pd.to_datetime(df_env_summer['sample.sampleDateTime']).dt.date
		
		
		
		time_summer = []
		nutrients_summer = []
		
		for n in nutrients_list:
			time_summer.append(df_env_summer[df_env_summer['determinand.notation'] == n].sort_values(by="Date", ascending=True)['Date'])
			nutrients_summer.append(df_env_summer[df_env_summer['determinand.notation'] == n].sort_values(by="Date", ascending=True)['result'])
			
			

		df_env_winter =  loc_subset(df.loc[np.logical_or(df["month"]<4,df["month"]>9)], location, location_type)
		df_env_winter.loc[:,"Date"] =pd.to_datetime(df_env_winter['sample.sampleDateTime']).dt.date

		time_winter = []
		nutrients_winter = []
		
		for n in nutrients_list:
			time_winter.append(df_env_winter[df_env_winter['determinand.notation'] == n].sort_values(by="Date", ascending=True)['Date'])
			nutrients_winter.append(df_env_winter[df_env_winter['determinand.notation'] == n].sort_values(by="Date", ascending=True)['result'])	
		return(np.concatenate(time_summer).flatten(), np.concatenate(nutrients_summer).flatten(), np.concatenate(time_winter).flatten(), np.concatenate(nutrients_winter).flatten())
		
def DAIN_time(df, location, seasons=False, location_type="label"):
	if seasons is False:
		df_env =  loc_subset(df,  location, location_type)
		df_env.loc[:,"Date"] = pd.to_datetime(df_env['sample.sampleDateTime']).dt.date
	
		dain_ = []
		date_ = []
		for date in np.unique(df_env["Date"].iloc[0::]):
			if (df_env[(df_env["Date"] == date)&(df_env['determinand.notation'] == 111) ]["Date"].size>0) &(df_env[(df_env["Date"] == date)&(df_env['determinand.notation'] == 116) ]["Date"].size>0):

				dain_.append(df_env[(df_env["Date"] == date)&(df_env['determinand.notation'] == 111) ]["result"].values[0]+df_env[(df_env["Date"] == date)&(df_env['determinand.notation'] == 116) ]["result"].values[0])
				date_.append(date)
				
		return(dain_, date_)
		
	if seasons is True:
		df_env_summer =  loc_subset(df.loc[(df["month"]>4)&(df["month"]<9)], location, location_type)
		df_env_summer.loc[:,"Date"] = pd.to_datetime(df['sample.sampleDateTime']).dt.date

		df_env_winter =  loc_subset(df.loc[np.logical_or(df["month"]<4,df["month"]>9)], location, location_type)
		df_env_winter.loc[:,"Date"] =pd.to_datetime(df['sample.sampleDateTime']).dt.date
		
		dain_summer = []
		date_summer = []
		for date in np.unique(df_env_summer["Date"].iloc[0::]):
			if (df_env_summer[(df_env_summer["Date"] == date)&(df_env_summer['determinand.notation'] == 111) ]["Date"].size>0) &(df_env_summer[(df_env_summer["Date"] == date)&(df_env_summer['determinand.notation'] == 116) ]["Date"].size>0):

				dain_summer.append(df_env_summer[(df_env_summer["Date"] == date)&(df_env_summer['determinand.notation'] == 111) ]["result"].values[0]+df_env_summer[(df_env_summer["Date"] == date)&(df_env_summer['determinand.notation'] == 116) ]["result"].values[0])
				date_summer.append(date)

		dain_winter = []
		date_winter = []
		for date in np.unique(df_env_winter["Date"].iloc[0::]):
			if (df_env_winter[(df_env_winter["Date"] == date)&(df_env_winter['determinand.notation'] == 111) ]["Date"].size>0) &(df_env_winter[(df_env_winter["Date"] == date)&(df_env_winter['determinand.notation'] == 116) ]["Date"].size>0):


				dain_winter.append(df_env_winter[(df_env_winter["Date"] == date)&(df_env_winter['determinand.notation'] == 111) ]["result"].values[0]+df_env_winter[(df_env_winter["Date"] == date)&(df_env_winter['determinand.notation'] == 116) ]["result"].values[0])
				date_winter.append(date)

		return(date_summer, dain_summer, date_winter, dain_winter)
		
	
	
def DAIN_time_tot(df, location, seasons=False, location_type="label"):
	if seasons is False:
		df_env =  loc_subset(df,  location, location_type)
		df_env.loc[:,"Date"] = pd.to_datetime(df_env['sample.sampleDateTime']).dt.date
	
		dain_ = []
		date_ = []
		for date in np.unique(df_env["Date"].iloc[0::]):
			for N in [116, 9686, 4925, 114, 9943]:
				for A in [9993, 111, 119]:
					if (df_env[(df_env["Date"] == date)&(df_env['determinand.notation'] == A) ]["Date"].size>0) &(df_env[(df_env["Date"] == date)&(df_env['determinand.notation'] == N) ]["Date"].size>0):

						dain_.append(df_env[(df_env["Date"] == date)&(df_env['determinand.notation'] == A) ]["result"].values[0]+df_env[(df_env["Date"] == date)&(df_env['determinand.notation'] == N) ]["result"].values[0])
				date_.append(date)
				
		return(dain_, date_)
		
	if seasons is True:
		df_env_summer =  loc_subset(df.loc[(df["month"]>4)&(df["month"]<9)], location, location_type)
		df_env_summer.loc[:,"Date"] = pd.to_datetime(df_env_summer['sample.sampleDateTime']).dt.date

		df_env_winter =  loc_subset(df.loc[np.logical_or(df["month"]<4,df["month"]>9)], location, location_type)
		df_env_winter.loc[:,"Date"] = pd.to_datetime(df_env_winter['sample.sampleDateTime']).dt.date
		
		dain_summer = []
		date_summer = []
		for date in np.unique(df_env_summer["Date"].iloc[0::]):
			for N in [116, 9686, 4925, 114, 9943]:
				for A in [9993, 111, 119]:
					if (df_env_summer[(df_env_summer["Date"] == date)&(df_env_summer['determinand.notation'] == A) ]["Date"].size>0) &(df_env_summer[(df_env_summer["Date"] == date)&(df_env_summer['determinand.notation'] == N) ]["Date"].size>0):

						dain_summer.append(df_env_summer[(df_env_summer["Date"] == date)&(df_env_summer['determinand.notation'] == A) ]["result"].values[0]+df_env_summer[(df_env_summer["Date"] == date)&(df_env_summer['determinand.notation'] == N) ]["result"].values[0])
						date_summer.append(date)

		dain_winter = []
		date_winter = []
		for date in np.unique(df_env_winter["Date"].iloc[0::]):
			for N in [116, 9686, 4925, 114, 9943]:
				for A in [9993, 111, 119]:
					if (df_env_winter[(df_env_winter["Date"] == date)&(df_env_winter['determinand.notation'] == A) ]["Date"].size>0) &(df_env_winter[(df_env_winter["Date"] == date)&(df_env_winter['determinand.notation'] == N) ]["Date"].size>0):


						dain_winter.append(df_env_winter[(df_env_winter["Date"] == date)&(df_env_winter['determinand.notation'] == A) ]["result"].values[0]+df_env_winter[(df_env_winter["Date"] == date)&(df_env_winter['determinand.notation'] == N) ]["result"].values[0])
						date_winter.append(date)

		return(date_summer, dain_summer, date_winter, dain_winter)
			
		

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
	

		

def plot_location_nutrientVStime(df, location, nutrient_determinand, ax=None, seasons=False, location_type="label"):
	
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

		if ax is None:
			ax = plt.gca()
		
		ax.plot(df_env[df_env['determinand.notation'] ==nutrient_determinand].sort_values(by="Date", ascending=True)['Date'],df_env[df_env['determinand.notation'] ==nutrient_determinand].sort_values(by="Date", ascending=True)['result'],color='teal', zorder=1,linewidth=2)
		ax.scatter(df_env[df_env['determinand.notation'] ==nutrient_determinand].sort_values(by="Date", ascending=True)['Date'],df_env[df_env['determinand.notation'] ==nutrient_determinand].sort_values(by="Date", ascending=True)['result'],edgecolor="black", facecolor="white", linewidth=2, zorder=2, s=20)
		ax.set_xlabel("time")
		ax.set_ylabel(str(df_env[df_env['determinand.notation'] ==nutrient_determinand].sort_values(by="Date",ascending=True)["determinand.definition"].iloc[0]))

	if seasons is True:
		df_env_summer = loc_subset(df.loc[(df["month"]>4)&(df["month"]<9)], location, location_type)
		df_env_summer.loc[:,"Date"] = pd.to_datetime(df_env_summer['sample.sampleDateTime']).dt.date

		df_env_winter = loc_subset(df.loc[np.logical_or(df["month"]<4,df["month"]>9)], location, location_type)
		df_env_winter.loc[:,"Date"] =pd.to_datetime(df_env_winter['sample.sampleDateTime']).dt.date

		if ax is None:
			ax = plt.gca()  
		ax.plot(df_env_summer[df_env_summer['determinand.notation'] ==nutrient_determinand].sort_values(by="Date", ascending=True)['Date'],df_env_summer[df_env_summer['determinand.notation'] ==nutrient_determinand].sort_values(by="Date", ascending=True)['result'],zorder=1, linewidth = 2, color='#EE6A50', linestyle=':')
		
		ax.scatter(df_env_summer[df_env_summer['determinand.notation'] ==nutrient_determinand].sort_values(by="Date", ascending=True)['Date'],df_env_summer[df_env_summer['determinand.notation'] ==nutrient_determinand].sort_values(by="Date", ascending=True)['result'],zorder=2, label="summer", color='orange', marker="+", s=30)

		ax.plot(df_env_winter[df_env_winter['determinand.notation'] ==nutrient_determinand].sort_values(by="Date", ascending=True)['Date'],df_env_winter[df_env_winter['determinand.notation'] ==nutrient_determinand].sort_values(by="Date", ascending=True)['result'],zorder=1, linewidth = 2, color='teal', linestyle='--')
		
		ax.scatter(df_env_winter[df_env_winter['determinand.notation'] ==nutrient_determinand].sort_values(by="Date", ascending=True)['Date'],df_env_winter[df_env_winter['determinand.notation'] ==nutrient_determinand].sort_values(by="Date", ascending=True)['result'],zorder=2, label="winter", color='blue', marker='o', s=20)
		
		ax.legend(fontsize=18)
		ax.set_xlabel("time")
		ax.set_ylabel(str(df_env_winter[df_env_winter['determinand.notation'] ==nutrient_determinand].sort_values(by="Date",ascending=True)["determinand.definition"].iloc[0]))
	return(ax)

def plot_location_nutrientVStime_customizable(df, location, nutrient_determinand, ax=None,seasons=False, location_type="label", plt_kwargs={}, sct_kwargs={},plt_kwargs_s={}, sct_kwargs_s={}, plt_kwargs_w={}, sct_kwargs_w={}, ylabel=None, plot_title=None):
	"""
	Return a plot nutrient VS time for a given location, diveded or not into winter (oct-march) and summer (apr-sept).
	The plot is customizable.
	
	input:
	df (DataFrame object)
	location (str): the location of interest, e.g. "langstone"; empty string "" return entire catalogue
	nutrient_determinand (int): the determinant of the nutrient, e.g. 118 for Nitrite (N), mg/l
	ax(Axes object)
	seasons (bool): False (no distinction in seasons); True (divided into seasons)
	location_type (str): either "label" (e.g. "langstone", "portsmouth") or "notation" (e.g. "SO-G00", "SW-Z94")
	plt_kwargs (properties, optional): to specify properties of the plot
	sct_kwargs (properties, optional): to specify properties of the scatter plot
	plt_kwargs_s (properties, optional): to specify properties of the plot, for summer data
	sct_kwargs_s (properties, optional): to specify properties of the scatter plot, for summer data
	plt_kwargs_w (properties, optional): to specify properties of the plot, for winter data
	sct_kwargs_w (properties, optional): to specify properties of the scatter plot, for winter data
	ylabel (str): label for the y-axis
	
	output:
	ax (Axes object)
	"""
	
	
	if seasons is False:
		df_env = loc_subset(df, location, location_type)
		df_env.loc[:,"Date"] = pd.to_datetime(df_env['sample.sampleDateTime']).dt.date

		if ax is None:
			ax = plt.gca()
		ax.plot(df_env[df_env['determinand.notation'] ==nutrient_determinand].sort_values(by="Date", ascending=True)['Date'],df_env[df_env['determinand.notation'] ==nutrient_determinand].sort_values(by="Date", ascending=True)['result'], zorder=1, **plt_kwargs)
		ax.scatter(df_env[df_env['determinand.notation'] ==nutrient_determinand].sort_values(by="Date", ascending=True)['Date'],df_env[df_env['determinand.notation'] ==nutrient_determinand].sort_values(by="Date", ascending=True)['result'], **sct_kwargs, zorder=2)
		ax.set_xlabel("time")
		
		if ylabel != None:
			ax.set_ylabel(str(ylabel))

	if seasons is True:
		df_env_summer = loc_subset(df.loc[(df["month"]>4)&(df["month"]<9)], location, location_type)
		df_env_summer.loc[:,"Date"] = pd.to_datetime(df_env_summer['sample.sampleDateTime']).dt.date

		df_env_winter =loc_subset(df.loc[np.logical_or(df["month"]<4,df["month"]>9)], location, location_type)
		df_env_winter.loc[:,"Date"] =pd.to_datetime(df_env_winter['sample.sampleDateTime']).dt.date

		if ax is None:
			ax = plt.gca()  
		ax.plot(df_env_summer[df_env_summer['determinand.notation'] ==nutrient_determinand].sort_values(by="Date", ascending=True)['Date'],df_env_summer[df_env_summer['determinand.notation'] ==nutrient_determinand].sort_values(by="Date", ascending=True)['result'],zorder=1,**plt_kwargs_s)
		ax.scatter(df_env_summer[df_env_summer['determinand.notation'] ==nutrient_determinand].sort_values(by="Date", ascending=True)['Date'],df_env_summer[df_env_summer['determinand.notation'] ==nutrient_determinand].sort_values(by="Date", ascending=True)['result'],zorder=2, label="summer", **sct_kwargs_s)
		ax.plot(df_env_winter[df_env_winter['determinand.notation'] ==nutrient_determinand].sort_values(by="Date", ascending=True)['Date'],df_env_winter[df_env_winter['determinand.notation'] ==nutrient_determinand].sort_values(by="Date", ascending=True)['result'],zorder=1, **plt_kwargs_w)
		ax.scatter(df_env_winter[df_env_winter['determinand.notation'] ==nutrient_determinand].sort_values(by="Date", ascending=True)['Date'],df_env_winter[df_env_winter['determinand.notation'] ==nutrient_determinand].sort_values(by="Date", ascending=True)['result'],zorder=2, label="winter",**sct_kwargs_w)
		ax.legend(fontsize=18)
		ax.set_xlabel("time")
		if ylabel != None:
			ax.set_ylabel(str(ylabel))
	return(ax)
	
def plot_location_nutrientVStime_customizable_summer(df, location, nutrient_determinand, ax=None, location_type="label", plt_kwargs_s={}, sct_kwargs_s={}, xlabel= None, ylabel=None, label_str=None, plot_title=None):
	"""
	Return a plot nutrient VS time for a given location, diveded or not into winter (oct-march) and summer (apr-sept).
	The plot is customizable.
	
	input:
	df (DataFrame object)
	location (str): the location of interest, e.g. "langstone"; empty string "" return entire catalogue
	nutrient_determinand (int): the determinant of the nutrient, e.g. 118 for Nitrite (N), mg/l
	ax(Axes object)
	seasons (bool): False (no distinction in seasons); True (divided into seasons)
	location_type (str): either "label" (e.g. "langstone", "portsmouth") or "notation" (e.g. "SO-G00", "SW-Z94")
	plt_kwargs (properties, optional): to specify properties of the plot
	sct_kwargs (properties, optional): to specify properties of the scatter plot
	plt_kwargs_s (properties, optional): to specify properties of the plot, for summer data
	sct_kwargs_s (properties, optional): to specify properties of the scatter plot, for summer data
	plt_kwargs_w (properties, optional): to specify properties of the plot, for winter data
	sct_kwargs_w (properties, optional): to specify properties of the scatter plot, for winter data
	ylabel (str): label for the y-axis
	
	output:
	ax (Axes object)
	"""

	df_env_summer = loc_subset(df.loc[(df["month"]>4)&(df["month"]<9)], location, location_type)
	df_env_summer.loc[:,"Date"] = pd.to_datetime(df_env_summer['sample.sampleDateTime']).dt.date


	if ax is None:
		ax = plt.gca()  
	ax.plot(df_env_summer[df_env_summer['determinand.notation'] ==nutrient_determinand].sort_values(by="Date", ascending=True)['Date'],df_env_summer[df_env_summer['determinand.notation'] ==nutrient_determinand].sort_values(by="Date", ascending=True)['result'],zorder=1,**plt_kwargs_s)
	ax.scatter(df_env_summer[df_env_summer['determinand.notation'] ==nutrient_determinand].sort_values(by="Date", ascending=True)['Date'],df_env_summer[df_env_summer['determinand.notation'] ==nutrient_determinand].sort_values(by="Date", ascending=True)['result'],zorder=2, **sct_kwargs_s,  label=label_str)


	if ylabel != None:
		ax.set_ylabel(str(ylabel))
	if xlabel != None:
		ax.set_xlabel(str(xlabel))
	if label_str != None:
		ax.legend(fontsize=18)
	if plot_title != None:
		ax.set_title(label=str(plot_title), fontsize=18)
	return(ax)
	
def plot_location_nutrientVStime_customizable_winter(df, location, nutrient_determinand, ax=None, location_type="label", plt_kwargs_w={}, sct_kwargs_w={}, xlabel = None, ylabel=None, label_str=None, plot_title=None):
	"""
	Return a plot nutrient VS time for a given location, diveded or not into winter (oct-march) and summer (apr-sept).
	The plot is customizable.
	
	input:
	df (DataFrame object)
	location (str): the location of interest, e.g. "langstone"; empty string "" return entire catalogue
	nutrient_determinand (int): the determinant of the nutrient, e.g. 118 for Nitrite (N), mg/l
	ax(Axes object)
	seasons (bool): False (no distinction in seasons); True (divided into seasons)
	location_type (str): either "label" (e.g. "langstone", "portsmouth") or "notation" (e.g. "SO-G00", "SW-Z94")
	plt_kwargs (properties, optional): to specify properties of the plot
	sct_kwargs (properties, optional): to specify properties of the scatter plot
	plt_kwargs_s (properties, optional): to specify properties of the plot, for summer data
	sct_kwargs_s (properties, optional): to specify properties of the scatter plot, for summer data
	plt_kwargs_w (properties, optional): to specify properties of the plot, for winter data
	sct_kwargs_w (properties, optional): to specify properties of the scatter plot, for winter data
	ylabel (str): label for the y-axis
	
	output:
	ax (Axes object)
	"""

	df_env_winter =loc_subset(df.loc[np.logical_or(df["month"]<4,df["month"]>9)], location, location_type)
	df_env_winter.loc[:,"Date"] =pd.to_datetime(df_env_winter['sample.sampleDateTime']).dt.date

	if ax is None:
		ax = plt.gca()  
	ax.plot(df_env_winter[df_env_winter['determinand.notation'] ==nutrient_determinand].sort_values(by="Date", ascending=True)['Date'],df_env_winter[df_env_winter['determinand.notation'] ==nutrient_determinand].sort_values(by="Date", ascending=True)['result'],zorder=1, **plt_kwargs_w)
	ax.scatter(df_env_winter[df_env_winter['determinand.notation'] ==nutrient_determinand].sort_values(by="Date", ascending=True)['Date'],df_env_winter[df_env_winter['determinand.notation'] ==nutrient_determinand].sort_values(by="Date", ascending=True)['result'],zorder=2, **sct_kwargs_w, label=label_str)


	if ylabel != None:
		ax.set_ylabel(str(ylabel))
	if xlabel != None:
		ax.set_xlabel(str(xlabel))
	if label_str != None:
		ax.legend(fontsize=18)
	if plot_title != None:
		ax.set_title(label=str(plot_title), fontsize=18)
	return(ax)

	




def DAIN(df, location, ax=None, seasons=False, location_type="label", plt_kwargs={}, sct_kwargs={},plt_kwargs_s={}, sct_kwargs_s={}, plt_kwargs_w={}, sct_kwargs_w={}, xlabel=None, ylabel=None, plot_title=None, label_str=None):
	if seasons is False:
		df_env = loc_subset(df,  location, location_type)
		df_env.loc[:,"Date"] = pd.to_datetime(df_env['sample.sampleDateTime']).dt.date
	
		dain_ = []
		date_ = []
		for date in np.unique(df_env["Date"].iloc[0::]):
			if (df_env[(df_env["Date"] == date)&(df_env['determinand.notation'] == 111) ]["Date"].size>0) &(df_env[(df_env["Date"] == date)&(df_env['determinand.notation'] == 116) ]["Date"].size>0):

				dain_.append(df_env[(df_env["Date"] == date)&(df_env['determinand.notation'] == 111) ]["result"].values[0]+df_env[(df_env["Date"] == date)&(df_env['determinand.notation'] == 116) ]["result"].values[0])
				date_.append(date)

		if ax is None:
			ax = plt.gca()
		ax.scatter(date_, dain_, zorder=2, **sct_kwargs)
		if ylabel != None:
			ax.set_ylabel(str(ylabel))
		if xlabel != None:
			ax.set_xlabel(str(xlabel))
		if label_str != None:
			ax.legend(fontsize=18)
		if plot_title != None:
			ax.set_title(label=str(plot_title), fontsize=18)
		
	if seasons is True:
		df_env_summer = loc_subset(df.loc[(df["month"]>4)&(df["month"]<9)], location, location_type)
		df_env_summer.loc[:,"Date"] = pd.to_datetime(df_env_summer['sample.sampleDateTime']).dt.date

		df_env_winter =loc_subset(df.loc[np.logical_or(df["month"]<4,df["month"]>9)], location, location_type)
		df_env_winter.loc[:,"Date"] =pd.to_datetime(df_env_winter['sample.sampleDateTime']).dt.date
		
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
		
		if ax is None:
			ax = plt.gca()		
		ax.scatter(date_summer, dain_summer, zorder=2, **sct_kwargs_s, label="summer")
		ax.plot(date_winter, dain_winter, zorder=1, **plt_kwargs_s)
		ax.scatter(df_env_winter[df_env_winter['determinand.notation'] == 111].sort_values(by="Date", ascending=True)['Date'], dain_winter, zorder=2, **sct_kwargs_w, label="winter")
		ax.plot(df_env_winter[df_env_winter['determinand.notation'] == 111].sort_values(by="Date", ascending=True)['Date'], dain_winter, zorder=1, **plt_kwargs_w)


		if ylabel != None:
			ax.set_ylabel(str(ylabel))
		if xlabel != None:
			ax.set_xlabel(str(xlabel))
		if label_str != None:
			ax.legend(fontsize=18)
		if plot_title != None:
			ax.set_title(label=str(plot_title), fontsize=22)
			
	return(ax)
	
	
	
def DAIN_summer(df, location, ax=None, location_type="label", plt_kwargs={}, sct_kwargs={},plt_kwargs_s={}, sct_kwargs_s={}, xlabel=None, ylabel=None, plot_title=None, label_str=None):

	df_env_summer = loc_subset(df.loc[(df["month"]>4)&(df["month"]<9)], location, location_type)
	df_env_summer.loc[:,"Date"] = pd.to_datetime(df_env_summer['sample.sampleDateTime']).dt.date
	
	dain_summer = []
	date_ = []
	for date in np.unique(df_env_summer["Date"].iloc[0::]):
		if (df_env_summer[(df_env_summer["Date"] == date)&(df_env_summer['determinand.notation'] == 111) ]["Date"].size>0) &(df_env_summer[(df_env_summer["Date"] == date)&(df_env_summer['determinand.notation'] == 116) ]["Date"].size>0):

			dain_summer.append(df_env_summer[(df_env_summer["Date"] == date)&(df_env_summer['determinand.notation'] == 111) ]["result"].values[0]+df_env_summer[(df_env_summer["Date"] == date)&(df_env_summer['determinand.notation'] == 116) ]["result"].values[0])

			date_.append(date)


	if ax is None:
		ax = plt.gca()		
	ax.scatter(date_, dain_summer, zorder=2, **sct_kwargs_s, label=label_str)
	ax.plot(date_, dain_summer, zorder=1, **plt_kwargs_s)




	if ylabel != None:
		ax.set_ylabel(str(ylabel))
	if xlabel != None:
		ax.set_xlabel(str(xlabel))
	if label_str != None:
		ax.legend(fontsize=18)
	if plot_title != None:
		ax.set_title(label=str(plot_title), fontsize=22)
	return(ax)
	
def DAIN_winter(df, location, ax=None, location_type="label", plt_kwargs={}, sct_kwargs={}, plt_kwargs_w={}, sct_kwargs_w={}, xlabel=None, ylabel=None, plot_title=None, label_str=None):

	df_env_winter = loc_subset(df.loc[np.logical_or(df["month"]<4,df["month"]>9)], location, location_type)
	df_env_winter.loc[:,"Date"] =pd.to_datetime(df_env_winter['sample.sampleDateTime']).dt.date

	dain_winter = []
	date_ = []
	for date in np.unique(df_env_winter["Date"].iloc[0::]):
		if (df_env_winter[(df_env_winter["Date"] == date)&(df_env_winter['determinand.notation'] == 111) ]["Date"].size>0) &(df_env_winter[(df_env_winter["Date"] == date)&(df_env_winter['determinand.notation'] == 116) ]["Date"].size>0):

			dain_winter.append(df_env_winter[(df_env_winter["Date"] == date)&(df_env_winter['determinand.notation'] == 111) ]["result"].values[0]+df_env_winter[(df_env_winter["Date"] == date)&(df_env_winter['determinand.notation'] == 116) ]["result"].values[0])
			date_.append(date)	
		

	
	if ax is None:
		ax = plt.gca()		


	ax.scatter(date_, dain_winter, zorder=2, **sct_kwargs_w, label=label_str)
	ax.plot(date_, dain_winter, zorder=1, **plt_kwargs_w)



	if ylabel != None:
		ax.set_ylabel(str(ylabel))
	if xlabel != None:
		ax.set_xlabel(str(xlabel))
	if label_str != None:
		ax.legend(fontsize=18)
	if plot_title != None:
		ax.set_title(label=str(plot_title), fontsize=22)
	return(ax)







import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

import WaterQualityFunction_nutrient as wqfn
	

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
		if ax is None:
			ax = plt.gca()
		time, nutrient = wqfn.nutrient_time(df, location, nutrient_determinand, location_type, seasons)

		
		ax.plot(time,nutrient,color='teal', zorder=1,linewidth=2)
		ax.scatter(time,nutrient,edgecolor="black", facecolor="white", linewidth=2, zorder=2, s=20)


	if seasons is True:
		time_summer, nutrient_summer, time_winter, nutrient_winter = wqfn.nutrient_time(df, location, nutrient_determinand, location_type, seasons)

		if ax is None:
			ax = plt.gca()  
		ax.plot(time_summer, nutrient_summer,zorder=1, linewidth = 2, color='#EE6A50', linestyle=':')
		
		ax.scatter(time_summer, nutrient_summer,zorder=2, label="summer", color='orange', marker="+", s=30)

		ax.plot(time_winter, nutrient_winter,zorder=1, linewidth = 2, color='teal', linestyle='--')
		
		ax.scatter(time_winter, nutrient_winter,zorder=2, label="winter", color='blue', marker='o', s=20)
		
		ax.legend(fontsize=18)

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
		time, nutrient = wqfn.nutrient_time(df, location, nutrient_determinand, location_type, seasons)

		if ax is None:
			ax = plt.gca()
		ax.plot(time,nutrient, zorder=1, **plt_kwargs)
		ax.scatter(time,nutrient, zorder=2, **sct_kwargs)
		
		
		if ylabel != None:
			ax.set_xlabel("time")
			ax.set_ylabel(str(ylabel))

	if seasons is True:
		time_summer, nutrient_summer, time_winter, nutrient_winter = wqfn.nutrient_time(df, location, nutrient_determinand, location_type, seasons)

		if ax is None:
			ax = plt.gca()  
		ax.plot(time_summer,nutrient_summer,zorder=1,**plt_kwargs_s)
		ax.scatter(time_summer,nutrient_summer,zorder=2, label="summer", **sct_kwargs_s)
		ax.plot(time_winter, nutrient_winter,zorder=1, **plt_kwargs_w)
		ax.scatter(time_winter, nutrient_winter,zorder=2, label="winter",**sct_kwargs_w)
		ax.legend(fontsize=18)
		ax.set_xlabel("time")
		if ylabel != None:
			ax.set_ylabel(str(ylabel))
	return(ax)
	
def plot_location_nutrientVStime_customizable_nutrients(df, location, nutrients_list, ax=None,seasons=False, location_type="label", plt_kwargs={}, sct_kwargs={},plt_kwargs_s={}, sct_kwargs_s={}, plt_kwargs_w={}, sct_kwargs_w={}, ylabel=None, plot_title=None):
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
		time, nutrient = wqfn.nutrient_time_nutrients(df, location, nutrients_list, location_type, seasons)

		if ax is None:
			ax = plt.gca()
		ax.plot(time,nutrient, zorder=1, **plt_kwargs)
		ax.scatter(time,nutrient, zorder=2, **sct_kwargs)
		
		
		if ylabel != None:
			ax.set_xlabel("time")
			ax.set_ylabel(str(ylabel))

	if seasons is True:
		time_summer, nutrient_summer, time_winter, nutrient_winter = wqfn.nutrient_time_nutrients(df, location, nutrients_list, location_type, seasons)

		if ax is None:
			ax = plt.gca()  
		ax.plot(time_summer,nutrient_summer,zorder=1,**plt_kwargs_s)
		ax.scatter(time_summer,nutrient_summer,zorder=2, label="summer", **sct_kwargs_s)
		ax.plot(time_winter, nutrient_winter,zorder=1, **plt_kwargs_w)
		ax.scatter(time_winter, nutrient_winter,zorder=2, label="winter",**sct_kwargs_w)
		ax.legend(fontsize=18)
		ax.set_xlabel("time")
		if ylabel != None:
			ax.set_ylabel(str(ylabel))
	return(ax)

	
def plot_location_nutrientVStime_customizable_summer(df, location, nutrient_determinand, seasons =True, ax=None, location_type="label", plt_kwargs_s={}, sct_kwargs_s={}, xlabel= None, ylabel=None, label_str=None, plot_title=None):
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
	time_summer = wqfn.nutrient_time(df, location, nutrient_determinand, location_type, seasons)[0]
	nutrient_summer = wqfn.nutrient_time(df, location, nutrient_determinand, location_type, seasons)[1]


	if ax is None:
		ax = plt.gca()  
	ax.plot(time_summer, nutrient_summer,zorder=1,**plt_kwargs_s)
	ax.scatter(time_summer, nutrient_summer,zorder=2, **sct_kwargs_s,  label=label_str)


	if ylabel != None:
		ax.set_ylabel(str(ylabel))
	if xlabel != None:
		ax.set_xlabel(str(xlabel))
	if label_str != None:
		ax.legend(fontsize=18)
	if plot_title != None:
		ax.set_title(label=str(plot_title), fontsize=18)
	return(ax)
	
def plot_location_nutrientVStime_customizable_winter(df, location, nutrient_determinand, seasons =True, ax=None, location_type="label", plt_kwargs_w={}, sct_kwargs_w={}, xlabel = None, ylabel=None, label_str=None, plot_title=None):
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
	time_winter = wqfn.nutrient_time(df, location, nutrient_determinand, location_type, seasons)[2]
	nutrient_winter = wqfn.nutrient_time(df, location, nutrient_determinand, location_type, seasons)[3]

	if ax is None:
		ax = plt.gca()  
	ax.plot(time_winter, nutrient_winter,zorder=1, **plt_kwargs_w)
	ax.scatter(time_winter, nutrient_winter,zorder=2, **sct_kwargs_w, label=label_str)


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
		dain_, date_ = wqfn.DAIN_time(df, location, seasons)

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
		date_summer, dain_summer, date_winter, dain_winter = wqfn.DAIN_time(df, location, seasons)
		
		if ax is None:
			ax = plt.gca()		
		ax.scatter(date_summer, dain_summer, zorder=2, **sct_kwargs_s, label="summer")
		ax.plot(date_summer, date_summer, zorder=1, **plt_kwargs_s)
		ax.scatter(date_winter, dain_winter, zorder=2, **sct_kwargs_w, label="winter")
		ax.plot(date_winter, dain_winter, zorder=1, **plt_kwargs_w)


		if ylabel != None:
			ax.set_ylabel(str(ylabel))
		if xlabel != None:
			ax.set_xlabel(str(xlabel))
		if label_str != None:
			ax.legend(fontsize=18)
		if plot_title != None:
			ax.set_title(label=str(plot_title), fontsize=22)
			
	return(ax)
	
	
	
def DAIN_summer(df, location, ax=None, seasons = True, location_type="label", plt_kwargs={}, sct_kwargs={},plt_kwargs_s={}, sct_kwargs_s={}, xlabel=None, ylabel=None, plot_title=None, label_str=None):
	date_summer = wqfn.DAIN_time(df, location, seasons)[0]
	dain_summer = wqfn.DAIN_time(df, location, seasons)[1]

	if ax is None:
		ax = plt.gca()		
	ax.scatter(date_summer, dain_summer, zorder=2, **sct_kwargs_s, label=label_str)
	ax.plot(date_summer, dain_summer, zorder=1, **plt_kwargs_s)




	if ylabel != None:
		ax.set_ylabel(str(ylabel))
	if xlabel != None:
		ax.set_xlabel(str(xlabel))
	if label_str != None:
		ax.legend(fontsize=18)
	if plot_title != None:
		ax.set_title(label=str(plot_title), fontsize=22)
	return(ax)
	
def DAIN_winter(df, location, ax=None, seasons = True, location_type="label", plt_kwargs={}, sct_kwargs={}, plt_kwargs_w={}, sct_kwargs_w={}, xlabel=None, ylabel=None, plot_title=None, label_str=None):
	date_winter = wqfn.DAIN_time(df,  location, seasons)[2]
	dain_winter = wqfn.DAIN_time(df, location, seasons)[3]
		

	
	if ax is None:
		ax = plt.gca()		


	ax.scatter(date_winter, dain_winter, zorder=2, **sct_kwargs_w, label=label_str)
	ax.plot(date_winter, dain_winter, zorder=1, **plt_kwargs_w)



	if ylabel != None:
		ax.set_ylabel(str(ylabel))
	if xlabel != None:
		ax.set_xlabel(str(xlabel))
	if label_str != None:
		ax.legend(fontsize=18)
	if plot_title != None:
		ax.set_title(label=str(plot_title), fontsize=22)
	return(ax)



def DAIN_tot(df, location, ax=None, seasons=False, location_type="label", plt_kwargs={}, sct_kwargs={},plt_kwargs_s={}, sct_kwargs_s={}, plt_kwargs_w={}, sct_kwargs_w={}, xlabel=None, ylabel=None, plot_title=None, label_str=None):
	if seasons is False:
		dain_, date_ = wqfn.DAIN_time_tot(df, location, seasons)

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
		date_summer, dain_summer, date_winter, dain_winter = wqfn.DAIN_time_tot(df, location, seasons)
		
		if ax is None:
			ax = plt.gca()		
		ax.scatter(date_summer, dain_summer, zorder=2, **sct_kwargs_s, label="summer")
		ax.plot(date_summer, date_summer, zorder=1, **plt_kwargs_s)
		ax.scatter(date_winter, dain_winter, zorder=2, **sct_kwargs_w, label="winter")
		ax.plot(date_winter, dain_winter, zorder=1, **plt_kwargs_w)


		if ylabel != None:
			ax.set_ylabel(str(ylabel))
		if xlabel != None:
			ax.set_xlabel(str(xlabel))
		if label_str != None:
			ax.legend(fontsize=18)
		if plot_title != None:
			ax.set_title(label=str(plot_title), fontsize=22)
			
	return(ax)
	
	
	
def DAIN_summer_tot(df, location, ax=None, seasons = True, location_type="label", plt_kwargs={}, sct_kwargs={},plt_kwargs_s={}, sct_kwargs_s={}, xlabel=None, ylabel=None, plot_title=None, label_str=None):
	date_summer = wqfn.DAIN_time_tot(df, location, seasons)[0]
	dain_summer = wqfn.DAIN_time_tot(df, location, seasons)[1]

	if ax is None:
		ax = plt.gca()		
	ax.scatter(date_summer, dain_summer, zorder=2, **sct_kwargs_s, label=label_str)
	ax.plot(date_summer, dain_summer, zorder=1, **plt_kwargs_s)




	if ylabel != None:
		ax.set_ylabel(str(ylabel))
	if xlabel != None:
		ax.set_xlabel(str(xlabel))
	if label_str != None:
		ax.legend(fontsize=18)
	if plot_title != None:
		ax.set_title(label=str(plot_title), fontsize=22)
	return(ax)
	
def DAIN_winter_tot(df, location, ax=None, seasons = True, location_type="label", plt_kwargs={}, sct_kwargs={}, plt_kwargs_w={}, sct_kwargs_w={}, xlabel=None, ylabel=None, plot_title=None, label_str=None):
	date_winter = wqfn.DAIN_time_tot(df, location, seasons)[2]
	dain_winter = wqfn.DAIN_time_tot(df, location, seasons)[3]
		

	
	if ax is None:
		ax = plt.gca()		


	ax.scatter(date_winter, dain_winter, zorder=2, **sct_kwargs_w, label=label_str)
	ax.plot(date_winter, dain_winter, zorder=1, **plt_kwargs_w)



	if ylabel != None:
		ax.set_ylabel(str(ylabel))
	if xlabel != None:
		ax.set_xlabel(str(xlabel))
	if label_str != None:
		ax.legend(fontsize=18)
	if plot_title != None:
		ax.set_title(label=str(plot_title), fontsize=22)
	return(ax)







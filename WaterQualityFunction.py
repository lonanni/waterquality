import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

def loc_subset(df, location):
    """
    Return a subsample of the main dataset, according to the location of interest

    input:
        df (DataFrame object)
        location (str): the location of interest, e.g. "langstone"
    output:
        df_subset (DataFrame object)

    .. warning:: 
    Performs **no** checks of the input.

    """
    
    locations = set(df['sample.samplingPoint.label'])
    location_condition = [x for x in locations if location in x.lower()]
    df_subset = df.loc[df['sample.samplingPoint.label'].isin(location_condition)]
    return df_subset

def plot_location_nutrientVStime(df, location, nutrient_determinand, ax=None, seasons=False):
    
    """
    Return a plot nutrient VS time for a given location

    input:
        df (DataFrame object)
        location (str): the location of interest, e.g. "langstone"
        nutrient_determinand (int): the determinant of the nutrient, e.g. 118 for Nitrite (N), mg/l
    output:
        ax (Axes object)

    .. warning:: 
    Performs **no** checks of the input.

    """
    if seasons is False:   
    	df_env = loc_subset(df, location)
    	df_env["date"] = pd.to_datetime(df_env['sample.sampleDateTime']).dt.date
    
		if ax is None:
			ax = plt.gca()    

    	ax.plot(df_env[df_env['determinand.notation'] == nutrient_determinand].sort_values(by="date", ascending=True)['date']
    		, df_env[df_env['determinand.notation'] == nutrient_determinand].sort_values(by="date", ascending=True)['result'], color='teal', zorder=1)
    	ax.scatter(df_env[df_env['determinand.notation'] == nutrient_determinand].sort_values(by="date", ascending=True)['date'], 
    		df_env[df_env['determinand.notation'] == nutrient_determinand].sort_values(by="date", ascending=True)['result'], edgecolor="black", facecolor="white", linewidth=3, zorder=2)


    	ax.set_xlabel("time")
    	ax.set_ylabel(str(df_env[df_env['determinand.notation'] == nutrient_determinand].sort_values(by="date", ascending=True)["determinand.definition"].iloc[0]))
    
    if seasons is True:
    	        
    	df_env_summer = loc_subset(df.loc[(df["month"]>4)&(df["month"]<9)], location)
    	df_env_summer["date"] = pd.to_datetime(df_env_summer['sample.sampleDateTime']).dt.date
    	
    	    	        
    	df_env_winter = loc_subset(df.loc[np.logical_or(df["month"]<4,df["month"]>9)], location)
    	df_env_winter["date"] = pd.to_datetime(df_env_winter['sample.sampleDateTime']).dt.date
    	
    	 if ax is None:
      	ax = plt.gca()  
    	
    ax.plot(df_env_summer[df_env_summer['determinand.notation'] == nutrient_determinand].sort_values(by="date", ascending=True)
    ['date'], df_env_summer[df_env_summer['determinand.notation'] == nutrient_determinand].sort_values(by="date", ascending=True)
    ['result'], zorder=1, linewidth = 2, color='pink', linestyle=':')
    ax.scatter(df_env_summer[df_env_summer['determinand.notation'] == nutrient_determinand].sort_values(by="date", ascending=True)
    ['date'], df_env_summer[df_env_summer['determinand.notation'] == nutrient_determinand].sort_values(by="date", ascending=True)
    ['result'], zorder=2, label="summer", color='orange', marker='+', markersize=30)
    
    ax.plot(df_env_winter[df_env_winter['determinand.notation'] == nutrient_determinand].sort_values(by="date", ascending=True)
    ['date'], df_env_winter[df_env_winter['determinand.notation'] == nutrient_determinand].sort_values(by="date", ascending=True)
    ['result'], zorder=1, linewidth = 2, color='teal', linestyle='--')
    ax.scatter(df_env_winter[df_env_winter['determinand.notation'] == nutrient_determinand].sort_values(by="date", ascending=True)
    ['date'], df_env_winter[df_env_winter['determinand.notation'] == nutrient_determinand].sort_values(by="date", ascending=True)
    ['result'], zorder=2, label="winter", color='blue', marker='o', markersize=10)
    ax.legend(fontsize=18)
    
    return(ax)


def plot_location_nutrientVStime_customizable(df, location, nutrient_determinand, ax=None, plt_kwargs={}, sct_kwargs={}):
    
    """
    
    Return a plot nutrient VS time for a given location, as function plot_location_nutrientVStime. This time, the plot is costumizable 

    input:
        df (DataFrame object)
        location (str): the location of intrest, e.g. "longstone"
        nutrient_determinand (int): the determinant of the nutrient, e.g. 118 for Nitrite (N), mg/l
        plt_kwargs (properties, optional): to specify properties of the plot
        sct_kwargs (properties, optional): to specify properties of the scatter plot
        
    output:
        ax (Axes object)

    .. warning:: 
    Performs **no** checks of the input.

    """
        
    df_env = loc_subset(df, location)
    df_env["date"] = pd.to_datetime(df_env['sample.sampleDateTime']).dt.date
    if ax is None:
        ax = plt.gca()

    ax.plot(df_env[df_env['determinand.notation'] == nutrient_determinand].sort_values(by="date", ascending=True)
    ['date'], df_env[df_env['determinand.notation'] == nutrient_determinand].sort_values(by="date", ascending=True)
    ['result'], zorder=1, **plt_kwargs)
    ax.scatter(df_env[df_env['determinand.notation'] == nutrient_determinand].sort_values(by="date", ascending=True)
    ['date'], df_env[df_env['determinand.notation'] == nutrient_determinand].sort_values(by="date", ascending=True)
    ['result'], zorder=2, **sct_kwargs)
    plt.legend(fontsize=18)
    return(ax)


def plot_location_nutrientVStime_customizable_summer(df, location, nutrient_determinand, ax=None, plt_kwargs={}, sct_kwargs={}):
    
    """
    
    Return a plot nutrient VS time for a given location, as function plot_location_nutrientVStime, for the summer months. This time, the plot is costumizable 

    input:
        df (DataFrame object)
        location (str): the location of intrest, e.g. "longstone"
        nutrient_determinand (int): the determinant of the nutrient, e.g. 118 for Nitrite (N), mg/l
        plt_kwargs (properties, optional): to specify properties of the plot
        sct_kwargs (properties, optional): to specify properties of the scatter plot
        
    output:
        ax (Axes object)

    .. warning:: 
    Performs **no** checks of the input.

    """
        
    df_env = loc_subset(df.loc[(df["month"]>4)&(df["month"]<9)], location)
    df_env["date"] = pd.to_datetime(df_env['sample.sampleDateTime']).dt.date
    if ax is None:
        ax = plt.gca()

    ax.plot(df_env[df_env['determinand.notation'] == nutrient_determinand].sort_values(by="date", ascending=True)
    ['date'], df_env[df_env['determinand.notation'] == nutrient_determinand].sort_values(by="date", ascending=True)
    ['result'], zorder=1, **plt_kwargs)
    ax.scatter(df_env[df_env['determinand.notation'] == nutrient_determinand].sort_values(by="date", ascending=True)
    ['date'], df_env[df_env['determinand.notation'] == nutrient_determinand].sort_values(by="date", ascending=True)
    ['result'], zorder=2, **sct_kwargs, label="summer")
    ax.legend(fontsize=18)
    return(ax)


def plot_location_nutrientVStime_customizable_winter(df, location, nutrient_determinand, ax=None, plt_kwargs={}, sct_kwargs={}):
    
    """
    
    Return a plot nutrient VS time for a given location, as function plot_location_nutrientVStime, for the winter months. This time, the plot is costumizable 

    input:
        df (DataFrame object)
        location (str): the location of intrest, e.g. "longstone"
        nutrient_determinand (int): the determinant of the nutrient, e.g. 118 for Nitrite (N), mg/l
        plt_kwargs (properties, optional): to specify properties of the plot
        sct_kwargs (properties, optional): to specify properties of the scatter plot
        
    output:
        ax (Axes object)

    .. warning:: 
    Performs **no** checks of the input.

    """
        
    df_env = loc_subset(df.loc[np.logical_or(df["month"]<4,df["month"]>9)], location)
    df_env["date"] = pd.to_datetime(df_env['sample.sampleDateTime']).dt.date
    if ax is None:
        ax = plt.gca()

    ax.plot(df_env[df_env['determinand.notation'] == nutrient_determinand].sort_values(by="date", ascending=True)
    ['date'], df_env[df_env['determinand.notation'] == nutrient_determinand].sort_values(by="date", ascending=True)
    ['result'], zorder=1, **plt_kwargs)
    ax.scatter(df_env[df_env['determinand.notation'] == nutrient_determinand].sort_values(by="date", ascending=True)
    ['date'], df_env[df_env['determinand.notation'] == nutrient_determinand].sort_values(by="date", ascending=True)
    ['result'], zorder=2, **sct_kwargs, label="winter")
    ax.legend(fontsize=18)
    return(ax)


def DAIN(df, location, ax=None, plt_kwargs={}, sct_kwargs={}):

    df_env = loc_subset(df, location)
    df_env["date"] = pd.to_datetime(df_env['sample.sampleDateTime']).dt.date

    dain = df_env[df_env['determinand.notation'] == 111].sort_values(by="date", ascending=True)['result'].values+df_env[df_env['determinand.notation'] == 116].sort_values(by="date", ascending=True)['result'].values
    if ax is None:
        ax = plt.gca()
    
    ax.scatter(df_env[df_env['determinand.notation'] == 111].sort_values(by="date", ascending=True)
    ['date'], dain, zorder=2, **sct_kwargs)

    ax.set_xlabel("time")
    ax.set_ylabel("DAIN")
    return(ax)






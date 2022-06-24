"""plot_total_sequences.py


"""

import geopandas as gpd
import matplotlib as mpl
import numpy as np
from argh import dispatch_command
from matplotlib import pyplot as plt

from utils import *


def plot_map(ax, polygons, locations):
    pass


def main(geoJSON: str) -> None:

    fig, axs = plt.subplots(2,2,figsize=(15,15))
    df_places = gpd.read_file(geoJSON)
    # this is where I can set values for each plot
    df_places['placeholder1']=np.random.randint(10000, size=len(df_places))
    df_places['placeholder2']=np.random.randint(10000, size=len(df_places))
    df_places['placeholder3']=np.random.randint(10000, size=len(df_places))
    df_places['placeholder4']=np.random.randint(10000, size=len(df_places))
    i = 1
    for ax in axs.flatten():
        ax = df_places.plot(column = f"placeholder{i}", cmap='cividis', ax=ax, legend=True, norm=mpl.colors.LogNorm())
    plt.show()

if __name__=="__main__":
    dispatch_command(main)


import netCDF4 as nc
import numpy as np
import matplotlib.pyplot as plt
import matplotlib
matplotlib.use('Agg')
import io

from matplotlib.backends.backend_agg import FigureCanvasAgg as FigureCanvas
from matplotlib.figure import Figure
from flask import Response
import cartopy.crs as ccrs

from flask import Flask
from netCDF4 import Dataset
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello from Python!'

@app.route('/pace')
def pace():
    file_path = 'PACE_OCI.20241005T140529.L2.OC_BGC.V2_0.NRT.nc'
    # dataset = Dataset(file_path, mode='r')

    # Open the NetCDF file
    # file_path = '/content/PACE_OCI.20241005T140529.L2.OC_BGC.V2_0.NRT.nc' #file name
    dataset = nc.Dataset(file_path)

    # Access and print variables in the 'geophysical_data' group
    geo_group = dataset.groups['geophysical_data']
    print("Variables in geophysical_data:", geo_group.variables.keys())

    # Extract chlorophyll concentration
    chlor_a = geo_group.variables['chlor_a'][:]  # Extracting chlorophyll concentration

    # Check if latitude and longitude variables are available in the navigation_data group
    nav_group = dataset.groups['navigation_data']
    lat = nav_group.variables['latitude'][:]  # Extract the latitude variable
    lon = nav_group.variables['longitude'][:]  # Extract the longitude variable

    # Now we can proceed to plot since the dimensions are compatible
    # Create a meshgrid for lat/lon if they are 1D
    if lat.ndim == 2 and lon.ndim == 2:  # If lat/lon are 2D grids
        lat = lat[:, 0]  # Take the first column (or row) if needed
        lon = lon[0, :]  # Take the first row (or column) if needed

    # # Set up a plot using Cartopy for geographical data
    # fig = plt.figure(figsize=(10, 6))
    plt.figure(figsize=(10, 6))
    ax = plt.axes(projection=ccrs.PlateCarree())
    ax.set_global()

    # Add coastlines for context
    ax.coastlines(resolution='110m')

    # Add the chlorophyll concentration data
    c = ax.pcolormesh(lon, lat, chlor_a, transform=ccrs.PlateCarree(), cmap='viridis')

    # Add colorbar
    plt.colorbar(c, label='Chlorophyll Concentration (mg/m^3)')

    # Add features like gridlines, labels
    ax.gridlines(draw_labels=True)

    # Show the plot
    plt.title('Chlorophyll Concentration')

    img = io.BytesIO()
    plt.savefig(img, format='png')
    plt.close()  # Close the figure to avoid display issues
    img.seek(0)  # Rewind the buffer

    # Return the image as a response
    return Response(img.getvalue(), mimetype='image/png')

if __name__ == '__main__':
    app.run(host='127.0.0.1', port=5000)

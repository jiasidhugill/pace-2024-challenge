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

from flask import Flask, request
from netCDF4 import Dataset
import requests
app = Flask(__name__)

from dotenv import load_dotenv
import json
from datetime import datetime
import os
import requests
import boto3
import numpy as np
import xarray as xr
import rasterio as rio
from rasterio.session import AWSSession
from rasterio.plot import show
import rioxarray
import geoviews as gv
import hvplot.xarray
import holoviews as hv
gv.extension('bokeh', 'matplotlib')

@app.route('/')
def hello_world():
    return 'Hello from Python!'

def get_temp_creds(s3_cred_endpoint):
    return requests.get(s3_cred_endpoint).json()

@app.route('/pacedata')
def pacedata(): 
    file_path = request.args.get('filepath', '')
    if (file_path == ''): 
        return 'no filepath'
    dataset = Dataset(file_path, 'r')

    # Access the observation_data and geolocation_data groups
    observation_data_group = dataset.groups['observation_data']
    geolocation_data_group = dataset.groups['geolocation_data']

    # Extract variables
    dolp = observation_data_group.variables['dolp'][:]  # Degree of Linear Polarization
    latitudes = geolocation_data_group.variables['latitude'][:]
    longitudes = geolocation_data_group.variables['longitude'][:]

    # Average over the views dimension
    dolp_mean = np.nanmean(dolp, axis=2)  # Shape (396, 519)

    # Flatten the latitudes and longitudes
    latitudes_mean = latitudes.flatten()
    longitudes_mean = longitudes.flatten()
    dolp_mean_flat = dolp_mean.flatten()

    # Create a scatter plot for DOLP using latitude and longitude
    plt.figure(figsize=(10, 6))
    scatter = plt.scatter(longitudes_mean, latitudes_mean, c=dolp_mean_flat, cmap='viridis', marker='o', alpha=0.7)
    plt.colorbar(scatter, label='Degree of Linear Polarization (DOLP)')
    plt.title('A closer look at light polarization of your ocean')
    plt.xlabel('Longitude')
    plt.ylabel('Latitude')
    plt.grid(True)
    img = io.BytesIO()
    plt.savefig(img, format='png')
    plt.close()  # Close the figure to avoid display issues
    img.seek(0)  # Rewind the buffer

    # Return the image as a response
    return Response(img.getvalue(), mimetype='image/png')

@app.route('/chlorophyll')
def chlorophyll():
<<<<<<< HEAD
    params = {
        "results_as_file": 1,
        "sensor_id": 42,
        "backdays": 1,
        "subType": 1
    }
    response = requests.post("https://oceandata.sci.gsfc.nasa.gov/api/file_search", data=params)
    print(response)
=======
    creds = get_temp_creds('https://data.lpdaac.earthdatacloud.nasa.gov/s3credentials')
    session = boto3.Session(
        aws_access_key_id=creds['accessKeyId'], 
        aws_secret_access_key=creds['secretAccessKey'],
        aws_session_token=creds['sessionToken'],
        region_name='us-west-2'
    )
    rio_env = rio.Env(
        AWSSession(session),
        GDAL_DISABLE_READDIR_ON_OPEN='EMPTY_DIR',
        GDAL_HTTP_COOKIEFILE=os.path.expanduser('~/cookies.txt'),
        GDAL_HTTP_COOKIEJAR=os.path.expanduser('~/cookies.txt')
    )
    rio_env.__enter__()

    s3_link = 's3://ob-cumulus-prod-public/PACE_OCI.20241005T203837.L2.OC_BGC.V2_0.NRT.nc'
    # hls_da = rioxarray.open_rasterio(s3_link, chuncks=True)
    # hls_da = hls_da.squeeze('band', drop=True)
    # hls_da.hvplot.image(x='x', y='y', cmap='fire', rasterize=True, width=800, height=600, colorbar=True)    # colormaps -> https://holoviews.org/user_guide/Colormaps.html

    #'s3://ob-cumulus-prod-public/PACE_OCI.20241005T203837.L2.OC_BGC.V2_0.NRT.nc'
    # new_edpt = 'ob-cumulus-prod-public.s3-us-west-2.amazonaws.com'
    # Create an S3 resource from the session
    # s3 = session.resource('s3')

    # # Access the bucket
    # bucket = s3.Bucket('ob-cumulus-prod-public')
    # List objects in the bucket
    # print(bucket.objects.all())
    # for obj in bucket.objects.all():
    #     print(obj.key)
    # response = requests.get(new_edpt)
    try: 
        hls_da = rioxarray.open_rasterio(s3_link, chuncks=True)
    except Exception as e: 
        print(e)
    # hls_da = rioxarray.open_rasterio(s3_link, chunks=True)
    # print(ds.values())
    

    # hls_da = hls_da.squeeze('band', drop=True) # change this line
    # hls_da.hvplot.image(x='x', y='y', cmap='fire', rasterize=True, width=800, height=600, colorbar=True)

    # img = io.BytesIO()
    # # plt.savefig(img, format='png')
    # hv.save(hls_da, fmt='png')
    # # plt.close()  # Close the figure to avoid display issues
    # img.seek(0)  # Rewind the buffer
    # Return the image as a response
    # return Response(img.getvalue(), mimetype='image/png')

>>>>>>> dcfa22a (added pacedata function for sonika's file access)
    return {
        'statusCode': 200,
    }

@app.route('/pace')
def pace():
    file_path = 'PACE_OCI.20241005T140529.L2.OC_BGC.V2_0.NRT.nc'
    # file_path = 'carbon/PACE_OCI.20241004.L3m.DAY.POC.V2_0.poc.0p1deg.NRT.nc'
    # file_path = 'biogeochemical/PACE_OCI.20241005T155846.L2.OC_BGC.V2_0.NRT.nc'
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

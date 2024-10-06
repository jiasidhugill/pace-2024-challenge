import netCDF4 as nc
import numpy as np
import matplotlib.pyplot as plt
import matplotlib
matplotlib.use('Agg')
import io
import cartopy.feature as cfeature

from matplotlib.backends.backend_agg import FigureCanvasAgg as FigureCanvas
from matplotlib.figure import Figure
from flask import Response
import cartopy.crs as ccrs

from flask import Flask, request
from netCDF4 import Dataset
import requests
app = Flask(__name__)

import requests
import numpy as np
import xarray as xr
import geoviews as gv
gv.extension('bokeh', 'matplotlib')

from io import BytesIO

def nc_to_png(filepath, type): # 'Rrs', two others lol
    ds = xr.open_dataset(filepath)
    ds = ds[type].sel(wavelength=443, method='nearest')

    fig = plt.figure(figsize=(15, 10))
    ax = fig.add_subplot(1, 1, 1, projection=ccrs.PlateCarree())
    ax.add_feature(cfeature.COASTLINE)
    ax.add_feature(cfeature.BORDERS)

    im = ax.imshow(ds, transform=ccrs.PlateCarree(),
               extent=[-180, 180, -90, 90],
               cmap='viridis', vmin=0, vmax=0.025)
    
    plt.colorbar(im, ax=ax, orientation='horizontal', pad=0.08)

    ax.gridlines(draw_labels=True)

    img = io.BytesIO()
    plt.savefig(img, format='png')
    plt.close()  # Close the figure to avoid display issues
    img.seek(0)  # Rewind the buffer

    # Return the image as a response
    return Response(img.getvalue(), mimetype='image/png')


@app.route('/')
def hello_world():
    return 'Hello from Python!'

@app.route('/getfile')
def get_file():
    backdays = request.args.get('backdays')
    dtid = request.args.get('dtid')
    dtids = {
        "rrs": 1750,
        "chlor": 1751,
        "carb": 1752,
    }
    url = "https://oceandata.sci.gsfc.nasa.gov/api/file_search"

    # Define the data to be sent in the request
    data = {
        "results_as_file": 1,
        "sensor_id": 42,
        "dtid": dtids[dtid],
        "backdays": backdays,
        "subType": 1,
        "addurl": 1
    }

    # Make the POST request
    data_url = requests.post(url, data=data).text.split('\n')[0]

    response = requests.get(data_url)
    # Check if the request was successful
    if response.status_code == 200:
        with open(dtid+'-'+backdays+'.nc', 'wb') as f:
            f.write(response.content)
        
    else:
        print(f"Failed to access data. Status code: {response.status_code}")

    # types = {
    #     'rrs': 'Rrs',
    #     'chlor': 'Chl',
    #     'carb': 'Carbon'
    # }
    return dtid+'-'+backdays+'.nc'#nc_to_png('{dtid}-{backdays}.nc', types[dtid])

@app.route('/getfiles')
def get_files():
    backdays = request.args.get('backdays')
    dtid = request.args.get('dtid')
    dtids = {
        "rrs": 1750,
        "chlor": 1751,
        "carb": 1752,
    }
    url = "https://oceandata.sci.gsfc.nasa.gov/api/file_search"

    # Define the data to be sent in the request
    data = {
        "results_as_file": 1,
        "sensor_id": 42,
        "dtid": dtids[dtid],
        "backdays": backdays,
        "subType": 1,
        "addurl": 1
    }

    # Make the POST request
    data_urls = requests.post(url, data=data).text.split('\n')
    
    # Check if the request was successful
    index = 0
    response_urls = []
    for url in data_urls: 
        response = requests.get(data_urls[index])
        if response.status_code == 200:
            with open(f'{dtid}-{backdays}-{index}.nc', 'wb') as f:
                f.write(response.content)
                response_urls.append(f'{dtid}-{backdays}-{index}.nc')
                index += 1
        
    else:
        print(f"Failed to access data. Status code: {response.status_code}")
    return response_urls


if __name__ == '__main__':
    app.run(host='127.0.0.1', port=5000)

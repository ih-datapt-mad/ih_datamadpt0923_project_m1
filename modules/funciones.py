import pandas as pd 
import numpy as np
import requests 
#BiciMad
def nearest(places, bicimad):
    data_list = []
    
    """ Latitud y longitud a radianes para realizar las operaciones. Luego los convierto a numpy para evitar error. """ 

    places_lat_rad = np.radians(places['location.latitude'].to_numpy())
    places_lon_rad = np.radians(places['location.longitude'].to_numpy())
    bicimad_lat_rad = np.radians(bicimad['latitude'].to_numpy())
    bicimad_lon_rad = np.radians(bicimad['longitude'].to_numpy())

    dlat = bicimad_lat_rad[:, np.newaxis] - places_lat_rad
    dlon = bicimad_lon_rad[:, np.newaxis] - places_lon_rad

    """ Fórmula de Haversine para calcular las distancias. """  """Sacas una matriz con todas las distancias"""
    
    a = np.sin(dlat / 2) ** 2 + np.cos(bicimad_lat_rad[:, np.newaxis]) * np.cos(places_lat_rad) * np.sin(dlon / 2) ** 2
    c = 2 * np.arcsin(np.sqrt(a))
    distance_matrix = c * 6371000 

    """ Cálculo del índice del resultado con menor distancia """

    min_distance_indices = np.argmin(distance_matrix, axis=0)

    """ Creación del dataframe del resultado utilizando ese índice"""

    for x in range(len(places["title"])):
        station_index = min_distance_indices[x]
        station = bicimad['name'].iloc[station_index].split('- ')[-1]
        station_address = bicimad["address"].iloc[station_index]
        place_address = places["address.street-address"][x]
        place = places["title"][x]
        min_distance = round(distance_matrix[station_index, x], 2)
        data_list.append({"place": place, "place_address": place_address, "station_name": station, "station_address": station_address,  "distance": min_distance})
        
    return pd.DataFrame(data_list)
def bicimad_final (df1):
    bicimad_df = pd.read_csv('./data/bicimad_stations.csv', sep = '\t')
    bicimad_df_clean = bicimad_df [['name', 'address', 'geometry.type', 'geometry.coordinates', 'dock_bikes']]
    split_mad = bicimad_df_clean['geometry.coordinates'].str.strip('[]').str.split(',', expand=True).astype('float64')
    split_mad.columns = ['longitude', 'latitude']
    df_concat = pd.concat([bicimad_df_clean,split_mad],axis=1)
    df2 = df_concat.drop(columns = ['geometry.coordinates', 'geometry.type']) 
    return df2

#BiciPark
def nearest_bicipark(places, bicipark):
    data_list = []
    
    """ Latitud y longitud a radianes para realizar las operaciones. Luego los convierto a numpy para evitar error. """ 

    places_lat_rad = np.radians(places['location.latitude'].to_numpy())
    places_lon_rad = np.radians(places['location.longitude'].to_numpy())
    bicimad_lat_rad = np.radians(bicipark['latitude'].to_numpy())
    bicimad_lon_rad = np.radians(bicipark['longitude'].to_numpy())

    dlat = bicimad_lat_rad[:, np.newaxis] - places_lat_rad
    dlon = bicimad_lon_rad[:, np.newaxis] - places_lon_rad

    """ Fórmula de Haversine para calcular las distancias. """  """Sacas una matriz con todas las distancias"""
    
    a = np.sin(dlat / 2) ** 2 + np.cos(bicimad_lat_rad[:, np.newaxis]) * np.cos(places_lat_rad) * np.sin(dlon / 2) ** 2
    c = 2 * np.arcsin(np.sqrt(a))
    distance_matrix = c * 6371000 

    """ Cálculo del índice del resultado con menor distancia """

    min_distance_indices = np.argmin(distance_matrix, axis=0)

    """ Creación del dataframe del resultado utilizando ese índice"""

    for x in range(len(places["title"])):
        station_index = min_distance_indices[x]
        station = bicipark['name'].iloc[station_index]
        station_address = bicipark["address"].iloc[station_index]
        place_address = places["address.street-address"][x]
        place = places["title"][x]
        min_distance = round(distance_matrix[station_index, x], 2)
        data_list.append({"place": place, "place_address": place_address, "station_name": station, "station_address": station_address,  "distance": min_distance})
        
    return pd.DataFrame(data_list)
def bicipark_final (df1):
    bicipark_df = pd.read_csv('./data/bicipark_stations.csv', sep = ';')
    bicipark_df['available_bikes'] = bicipark_df['total_places']-bicipark_df['free_places']
    bicipark_df_clean = bicipark_df [['stationName', 'address', 'geometry.type', 'zip_code', 'geometry.coordinates', 'available_bikes']]
    split_park = bicipark_df_clean['geometry.coordinates'].str.strip('[]').str.split(',', expand=True).astype('float64')
    split_park.columns = ['longitude', 'latitude']
    df_concat2 = pd.concat([bicipark_df_clean ,split_park],axis=1)
    df3 = df_concat2.drop(columns = ['geometry.coordinates', 'geometry.type', 'zip_code'])
    df3.columns = ['name', 'address', 'longitude', 'latitude', 'available_bikes'] 
    return df3

#Bicipark
def instalaciones ():
    url = ('https://datos.madrid.es/egob/catalogo/200215-0-instalaciones-deportivas.json')
    response = requests.get(url)
    json_data = response.json()
    json_datakeys = json_data['@graph']
    df = pd.json_normalize(json_datakeys) 
    df1 = df [['title','address.postal-code', 'address.street-address', 'location.latitude', 'location.longitude']]
    return df1






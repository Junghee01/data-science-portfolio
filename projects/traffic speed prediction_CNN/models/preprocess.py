#Load data file 
gdf_urban_core_gu = pd.read_csv('/content/gdf_urban_core_gu.csv')
gdf_urban_core_gu= gdf_urban_core_gu.drop(['Unnamed: 0'], axis=1)

idx = pd.date_range('2018-04-01 00:00:00','2018-04-30 23:55:00',freq='5min')
idx = idx.astype('str')

ex_core=gdf_urban_core_gu[idx.to_list()]
ex_core=ex_core.T
ex_core=ex_core.reset_index()
ex_core=ex_core.drop(['index'],axis=1)
ex_core=ex_core.T


# Extract timestamp columns
timestamp_cols = ex_core.columns
timestamps_data = ex_core.loc[:, timestamp_cols].values

# Define the number of timestamps per image and number of "Link ID"s
num_timestamps_per_image = 8
num_link_ids = timestamps_data.shape[0]

# Create spatio-temporal images
num_images = timestamps_data.shape[1] - num_timestamps_per_image +1  
spatio_temporal_images = np.array([
    timestamps_data[:, i:i+num_timestamps_per_image]
    for i in range(num_images)
])

# Shape of spatio_temporal_images: [num_images, num_link_ids, num_timestamps_per_image]

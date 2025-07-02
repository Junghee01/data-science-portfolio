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


# Create input data
temp_target =spatio_temporal_images[:, :, :2]   # 앞의 두개의 timestpamt만 남기고 두번째 부터 target 값으로 설정
final_y_data = temp_target[1:]
final_x_data =spatio_temporal_images[:-1]

# Split data into train, val, and test set
# Define the size of the test set
test_size = 0.23

# First split: Separate out the test set
X_temp, X_test_, y_temp, y_test_ = train_test_split(
    final_x_data, final_y_data, test_size=test_size, random_state=42
)

# Define the size of the validation set relative to the temporary training set
val_size = 0.07 / (1 - test_size)

# Second split: Separate out the validation set from the (temporary) training set
X_train_, X_val_, y_train_, y_val_ = train_test_split(
    X_temp, y_temp, test_size=val_size, random_state=42
)


# Apply Min-Max Scaling
X_scaler = MinMaxScaler()
X_scaler.fit(X_train_.reshape(-1,8))

y_scaler = MinMaxScaler()
y_scaler.fit(y_train_.reshape(-1,2))

scaled_X_train = X_scaler.transform(X_train_.reshape(-1,8)).reshape(X_train_.shape)
scaled_y_train = y_scaler.transform(y_train_.reshape(-1,2)).reshape(y_train_.shape)

scaled_X_test = X_scaler.transform(X_test_.reshape(-1,8)).reshape(X_test_.shape)
scaled_y_test = y_scaler.transform(y_test_.reshape(-1, 2)).reshape(y_test_.shape)

scaled_X_val = X_scaler.transform(X_val_.reshape(-1, 8)).reshape(X_val_.shape)
scaled_y_val = y_scaler.transform(y_val_.reshape(-1, 2)).reshape(y_val_.shape)


# Convert to torch tensor & Generate datasets based on partitions
X_train = torch.tensor(scaled_X_train, dtype=torch.float32)
y_train = torch.tensor(scaled_y_train, dtype=torch.float32)
X_train = X_train.unsqueeze(1)   
y_train = y_train.unsqueeze(1)

X_val = torch.tensor(scaled_X_val, dtype=torch.float32)
y_val = torch.tensor(scaled_y_val, dtype=torch.float32)
X_val = X_val.unsqueeze(1)
y_val = y_val.unsqueeze(1)

X_test = torch.tensor(scaled_X_test, dtype=torch.float32)
y_test = torch.tensor(scaled_y_test, dtype=torch.float32)
X_test = X_test.unsqueeze(1)
y_test = y_test.unsqueeze(1)


trainset = TensorDataset(X_train, y_train)
valset = TensorDataset(X_val, y_val)
testset = TensorDataset(X_test, y_test)

partition = {'train': trainset, 'val':valset, 'test':testset}

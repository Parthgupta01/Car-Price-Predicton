import pickle
import pandas as pd

# ---- Step 1: Load Preprocessor and Model ----
with open('labelencoder.pkl', 'rb') as f:
    le = pickle.load(f)
with open('columtranformer.pkl', 'rb') as f:
    preprocessor = pickle.load(f)

with open('model.pkl', 'rb') as f:
    model = pickle.load(f)

# ---- Step 2: Create New Input ----
new_data = pd.DataFrame({
    'model': ['Swift'],                 # string value (LabelEncoded in preprocessor)
    'vehicle_age': [5],
    'km_driven': [35000],
    'seller_type': ['Individual'],
    'fuel_type': ['Petrol'],
    'transmission_type': ['Manual'],
    'mileage': [19.0],
    'engine': [1197],
    'max_power': [82],
    'seats': [5]
})

# ---- Step 3: Transform new data using preprocessor ----
new_data['model'] = le.transform(new_data['model'].values)
# new_data['model'] = le.transform([new_data['model'][0]]

new_data_transformed = preprocessor.transform(new_data)

# ---- Step 4: Predict using model ----
predicted_price = model.predict(new_data_transformed)

print("Predicted Selling Price:", predicted_price[0])

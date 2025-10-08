from flask import Flask, render_template, request
import pickle
import pandas as pd

app = Flask(__name__)

# ---- Load Model & Preprocessor ----
with open('labelencoder.pkl', 'rb') as f:
    le = pickle.load(f)
with open('columtranformer.pkl', 'rb') as f:
    preprocessor = pickle.load(f)
with open('model.pkl', 'rb') as f:
    model = pickle.load(f)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    try:
        model_name = request.form['model']
        vehicle_age = float(request.form['vehicle_age'])
        km_driven = float(request.form['km_driven'])
        seller_type = request.form['seller_type']
        fuel_type = request.form['fuel_type']
        transmission_type = request.form['transmission_type']
        mileage = float(request.form['mileage'])
        engine = float(request.form['engine'])
        max_power = float(request.form['max_power'])
        seats = float(request.form['seats'])

        # Create DataFrame
        input_df = pd.DataFrame([[model_name, vehicle_age, km_driven, seller_type, fuel_type,
                                  transmission_type, mileage, engine, max_power, seats]],
                                columns=['model','vehicle_age','km_driven','seller_type','fuel_type',
                                         'transmission_type','mileage','engine','max_power','seats'])
        try:
            input_df['model'] = le.transform(input_df['model'])
        except:
            input_df['model'] = 0

        transformed_data = preprocessor.transform(input_df)
        prediction = model.predict(transformed_data)[0]

        return render_template('index.html', prediction=f"{round(prediction,2)}")

    except Exception as e:
        return render_template('index.html', prediction_text=f"Error: {str(e)}")

if __name__ == "__main__":
    app.run(debug=True)

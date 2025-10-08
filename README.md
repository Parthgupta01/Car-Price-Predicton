Car Price Predictor 🚗💰

A Machine Learning-based web application to predict the selling price of used cars. This project helps users estimate the fair price of their vehicles instantly using a simple and interactive web interface.

Features

Predicts car price based on multiple features:

Car Model

Vehicle Age

Kilometers Driven

Seller Type (Individual/Dealer/Trustmark Dealer)

Fuel Type (Petrol/Diesel/CNG/LPG)

Transmission Type (Manual/Automatic)

Mileage (km/l)

Engine (cc)

Max Power (bhp)

Seats

Built using Flask for backend and Bootstrap for responsive frontend.

Preprocessing with ColumnTransformer and LabelEncoder for handling categorical features.

Displays predicted price instantly without page reload.

Demo


Replace the above link with an actual screenshot of your app.

Installation

Clone the repository

git clone https://github.com/yourusername/car-price-predictor.git
cd car-price-predictor


Install dependencies

pip install -r requirements.txt


Run the Flask app

python app.py


Open in browser
Go to http://127.0.0.1:5000/

File Structure
car-price-predictor/
│
├─ app.py                 # Flask app
├─ templates/
│   └─ index.html         # HTML template
├─ model.pkl              # Trained ML model
├─ columtranformer.pkl    # Preprocessing pipeline
├─ labelencoder.pkl       # Label encoder for categorical features
├─ requirements.txt       # Python dependencies
└─ README.md

Future Improvements

Add more car models and features.

Deploy the app to Heroku or AWS for public access.

Integrate real-time car database APIs for dynamic data.

Add data visualization for insights on predicted prices.

Tech Stack

Python 3

Flask

Pandas & NumPy

Scikit-learn

HTML, CSS, Bootstrap

from flask import Flask,request,render_template,jsonify
import numpy as np
import pandas as pd

import pandas
# import sklearn
# import pickle
import joblib

app = Flask(__name__)
#Crop files
model_crop=joblib.load(open('model/crop/xgboost_model_c1.pkl','rb'))
le_crop=joblib.load(open('model/crop/label_encoder_c1.pkl','rb'))
le_soil=joblib.load(open('model/crop/label_encoder_soil.pkl','rb'))
minmax_crop=joblib.load(open('model/crop/minmaxr_c1.pkl','rb'))
standard_crop=joblib.load(open('model/crop/standardc_c1.pkl','rb'))

#Fertilizer files
model_ferti=joblib.load(open('model/fertilizer/xgboost_model_fertilizer.pkl','rb'))
le_ferti=joblib.load(open('model/fertilizer/label_encoder_fertilizer.pkl','rb'))
minmax_fertilizer=joblib.load(open('model/fertilizer/minmax_fertilizer.pkl','rb'))
standard_fertilizer=joblib.load(open('model/fertilizer/standard_fertilizer.pkl','rb'))

@app.route('/')
def home():
    return render_template('home_ani_update.html')

@app.route('/aboutPage')
def about():
    return render_template('aboutPage.html')

@app.route("/crop",methods=['POST','GET'])
def crop():
    if request.method == 'POST':
        try:
            # Get inputs from form
            data = request.get_json()
            soil_color = data.get("soil_color")
            N = float(data.get("n"))
            P = float(data.get("p"))
            K = float(data.get("k"))
            pH = float(data.get("ph"))
            rainfall = float(data.get("rainfall"))
            temperature = float(data.get("temperature"))

            s=le_soil.transform([soil_color])[0]

            feature_list = [s,N, P, K, pH, rainfall, temperature]
            new_data = pd.DataFrame([feature_list], columns=['Soil_color', 'Nitrogen', 'Phosphorus', 'Potassium', 'pH', 'Rainfall', 'Temperature'])

            # Apply MinMax scaling
            new_data_scaled_minmax = minmax_crop.transform(new_data)

            # Apply Standard scaling
            new_data_scaled = standard_crop.transform(new_data_scaled_minmax)

            # Predict using the trained model
            predicted_crop = model_crop.predict(new_data_scaled)

            decoded_prediction=le_crop.inverse_transform(predicted_crop)

            if decoded_prediction[0]:
                crop = decoded_prediction[0]
                result = "{} is the best crop to be cultivated right there".format(crop)
                crop_image_path = f"/static/images/crop/{crop.lower()}.jpg"  # Assuming images are named like 'sugarcane.jpg'
            else:
                result = "Sorry, we could not determine the best crop to be cultivated with the provided data."
                crop_image_path = None
        # Return JSON response for AJAX
            return jsonify({'prediction_text': result, 'crop_image': crop_image_path})
        except Exception as e:
            return jsonify({'prediction_text': f"Error: {str(e)}", 'crop_image': None})
    return render_template('crop.html')

@app.route('/ferti', methods=['GET', 'POST'])
def ferti():
    if request.method == 'POST':
        try:
            # Get inputs from form
            data = request.get_json()
            N = float(data.get("n"))
            P = float(data.get("p"))
            K = float(data.get("k"))
            pH = float(data.get("ph"))
            crop_name = data.get("crop_name")

            c=le_crop.transform([crop_name])[0]
            feature_list = [N, P, K, pH,c]
            new_data = pd.DataFrame([feature_list], columns=['Nitrogen', 'Phosphorus', 'Potassium', 'pH', 'Crop'])     
            new_data_scaled_minmax = minmax_fertilizer.transform(new_data)

            # Apply Standard scaling
            new_data_scaled = standard_fertilizer.transform(new_data_scaled_minmax)

            # Predict using the trained model
            predicted_fertilizer = model_ferti.predict(new_data_scaled)

            decoded_prediction=le_ferti.inverse_transform(predicted_fertilizer)
            if decoded_prediction[0]:
                fertilizer = decoded_prediction[0]
                result = "{} is the best fertilizer required for this field".format(fertilizer)
                fList = ['Urea', 'DAP', 'MOP', 'SSP', 'Magnesium Sulphate','Chilated Micronutrient', 'Sulphur','Ammonium Sulphate', 
                'Ferrous Sulphate','White Potash', 'Hydrated Lime']
                if fertilizer in fList:
                    fertilizer_image_path = f"/static/images/fertilizer/{fertilizer.lower()}.jpg"
                else:
                    fertilizer_image_path = f"/static/images/fertilizer/fertilizer.jpg"
            else:
                result = "Sorry, we could not determine the best fertilizer to be required with the provided data."
                fertilizer_image_path = None

            return jsonify({'prediction_text': result, 'fertilizer_image': fertilizer_image_path})

        except Exception as e:
            return jsonify({'prediction_text': f"Error: {str(e)}", 'fertilizer_image': None})
    return render_template('ferti.html')
if __name__ == "__main__":
    app.run(debug=True)

# if __name__ == "__main__":
#     port = int(os.environ.get("PORT", 5000))  # Use the PORT environment variable if available
#     app.run(host="0.0.0.0", port=port, debug=True)

from flask import Flask,request,render_template,jsonify
import numpy as np

import pandas
import sklearn
import pickle



app = Flask(__name__)

model_crop = pickle.load(open('model/cropModels/model.pkl','rb'))
sc_crop = pickle.load(open('model/cropModels/standscaler.pkl','rb'))
mx_crop = pickle.load(open('model/cropModels/minmaxscaler.pkl','rb'))

model_ferti = pickle.load(open('model/fertilizerModels/model.pkl','rb'))
sc_ferti = pickle.load(open('model/fertilizerModels/standscaler.pkl','rb'))
mx_ferti = pickle.load(open('model/fertilizerModels/minmaxscaler.pkl','rb'))

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

            soil_dict={'Black':1, 'Red':2, 'Medium Brown':3, 'Dark Brown':4, 'Light Brown':5, 'Reddish Brown':6}
            s=soil_dict[soil_color]

            feature_list = [s,N, P, K, pH, rainfall, temperature]
            single_pred = np.array(feature_list).reshape(1, -1)

            mx_features = mx_crop.transform(single_pred)
            sc_mx_features = sc_crop.transform(mx_features)
            prediction = model_crop.predict(sc_mx_features)

            crop_dict={
    1: 'Sugarcane',    2: 'Jowar',    3: 'Cotton',    4: 'Rice',    5: 'Wheat',
    6: 'Groundnut',    7: 'Maize',    8: 'Tur',    9: 'Urad',    10: 'Moong',
    11: 'Gram',    12: 'Masoor',    13: 'Soybean',    14: 'Ginger',    15: 'Turmeric',    16: 'Grapes'}
            
            if prediction[0] in crop_dict:
                crop = crop_dict[prediction[0]]
                result = "{} is the best crop to be cultivated right there".format(crop)
                crop_image_path = f"/static/images/{crop.lower()}.jpg"  # Assuming images are named like 'sugarcane.jpg'
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
            rainfall = float(data.get("rainfall"))
            temperature = float(data.get("temperature"))
            crop_name = data.get("crop_name")

            crop_dict={
    'Sugarcane':1,    'Jowar':2,    'Cotton':3,    'Rice':4,    'Wheat':5,
    'Groundnut':6,    'Maize':7,    'Tur':8,    'Urad':9,    'Moong':10,
    'Gram':11,    'Masoor':12,    'Soybean':13,    'Ginger':14,    'Turmeric':15,    'Grapes':16}
            c=crop_dict[crop_name]

            feature_list = [N, P, K, pH, rainfall, temperature,c]
            single_pred = np.array(feature_list).reshape(1, -1)             

            mx_features = mx_ferti.transform(single_pred)
            sc_mx_features = sc_ferti.transform(mx_features)
            prediction = model_ferti.predict(sc_mx_features)

            ferti_dict={
    1: 'Urea',    2: 'DAP',    3: 'MOP',    4: '10:26:26 NPK',    5: 'SSP',    6: 'Magnesium Sulphate',    7: '13:32:26 NPK',
    8: '12:32:16 NPK',    9: '50:26:26 NPK',    10: '19:19:19 NPK',    11: 'Chilated Micronutrient',    12: '18:46:00 NPK',
    13: 'Sulphur',    14: '20:20:20 NPK',    15: 'Ammonium Sulphate',    16: 'Ferrous Sulphate',    17: 'White Potash',
    18: '10:10:10 NPK',    19: 'Hydrated Lime'}
            
            if prediction[0] in ferti_dict:
                fertilizer = ferti_dict[prediction[0]]
                result = "{} is the best fertilizer required for this field".format(fertilizer)
                fertilizer_image_path = f"/static/images/fertilizer.jpg"  # Assuming images are named like 'fertilizer.jpg'
            else:
                result = "Sorry, we could not determine the best fertilizer to be required with the provided data."
                fertilizer_image_path = None

            return jsonify({'prediction_text': result, 'fertilizer_image': fertilizer_image_path})

        except Exception as e:
            return jsonify({'prediction_text': f"Error: {str(e)}", 'fertilizer_image': None})

    return render_template('ferti.html')

if __name__ == "__main__":
    app.run(debug=True)

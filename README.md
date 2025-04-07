# 🌾 Crop & Fertilizer Recommendation System
A web-based application that recommends the most suitable crop and fertilizer based on soil and environmental conditions. Built using HTML, CSS, JavaScript (Frontend) and Python with Flask (Backend), and powered by machine learning models.
🎥 [Watch Demo Video](https://youtu.be/0J3xB1wUlqU)
# 🚀 Features
🌱 Crop Prediction based on:


N, P, K values

Soil color

pH level

Temperature

Rainfall


# 🌾 Fertilizer Recommendation based on:

Selected crop

Current soil nutrients (N, P, K)

pH level

🧠 Machine learning models trained and deployed with Flask

🔗 Frontend and backend fully connected using Fetch API or AJAX

💬 Result displayed in a popup window

# 🛠️ Tech Stack
`Frontend:`
HTML5

CSS3

JavaScript

`Backend:`
Python

Flask

Pickle (for loading ML models)

# ML Libraries:
scikit-learn

pandas

numpy

# 📁 Folder Structure
```
project-root/
│
├── templates/
│   ├── home_ani_update.html
│   ├── crop.html
│   ├── ferti.html
│   ├── aboutPage.html
│
├── static/
│   ├── css/
│   │   ├── style_about.css
|   |   ├── style_crop.css
│   │   ├── style_fertilizer.css
|   |   ├── style_home_ani.css
│   │   ├── style_navigation.css
|   |
│   ├── javascript/
│   │   ├── script_crop.js
|   |   ├── script_ferti.js
│   │   ├── script_nav.js
|   |   
│   ├── images/
│   │   ├── crop/
|   |   ├── fertilizer/
│   ├── videos/
│   │   ├── video1.mp4
│
├── model/
│   ├── crop/
│   │   ├── label_encoder_c1.pkl
│   │   ├── label_encoder_soil.pkl
│   │   └── minmaxr_c1.pkl
│   │   ├── standardc_c1.pkl
│   │   └── xgboost_model_c1.pkl
│   ├── fertilizer/
│       ├── label_encoder_c1.pkl
│       ├── label_encoder_fertilizer.pkl
│       └── minmaxr_fertilizer.pkl
│       ├── standardc_fertilizer.pkl
│       └── xgboost_model_fertilizer.pkl
│
├── app.py
├── requirements.txt
```
# 🔧 How to Run the Project
`Install dependencies`
```
pip install -r requirements.txt
```
`Run Flask server`
```
python app.py
```
`Open your browser`
```
http://localhost:5000
```
# 📈 ML Model Info
Crop model trained on 4500+ data points

Fertilizer model considers nutrient imbalance

Used Label Encoding, MinMax Scaling, and Standard Scaling during preprocessing

# 📸 Snapshots
Crop prediction
![Image](https://github.com/user-attachments/assets/dda11caa-5b1f-40b6-b27a-12acb141315d)
Fertilizer recommendation
![Image](https://github.com/user-attachments/assets/53c7a9a7-0cde-4e4a-969c-24198b16b4fb)
# 👨‍💻 Author
Sayak Saha
MCA'2025, Future Institute of Engineering and Management

# 📃 License
This project is licensed under the MIT License – free to use and modify with attribution.


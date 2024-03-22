# Load the dataset
path = 'Back_end/dataset1.csv'
dataset = pd.read_csv(path)


# Load the trained model
with open('Back_end/knnModel.pkl', 'rb') as f:
    model = pickle.load(f)

# Create an instance of LabelEncoder
label_encoder = LabelEncoder()




@app.route('/career_quiz', methods=['POST'])
def career_quiz():
    #Get values from form
    init_features=[int(x) for x in request.form.values()]
    print(init_features)


    #fit the Y values to label encoder
    transformed_data = label_encoder.fit_transform(dataset['Course'].unique())
    print(transformed_data)

    #input the values to ML Model
    prediction = model.predict([init_features])
    print(prediction)
    
    #Label Encoding for prediction
    prediction = label_encoder.inverse_transform(prediction)
    print(prediction)

    
    return render_template('prediction2.html',prediction_career = prediction[0])
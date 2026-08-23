from flask import Flask, render_template, request
import pandas as pd
import pickle

app = Flask(__name__)

# Load trained pipeline
with open("model/pipeline.pkl", "rb") as file:
    pipeline = pickle.load(file)


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/predict_data", methods=["POST"])
def predict():

    new_data = pd.DataFrame([{
        "Location": request.form["Location"],
        "Cuisine": request.form["Cuisine"],
        "Rating": float(request.form["Rating"]),
        "Seating Capacity": int(request.form["Seating_Capacity"]),
        "Average Meal Price": float(request.form["Average_Meal_Price"]),
        "Marketing Budget": float(request.form["Marketing_Budget"]),
        "Social Media Followers": int(
            request.form["Social_Media_Followers"]
        ),
        "Chef Experience Years": int(
            request.form["Chef_Experience_Years"]
        ),
        "Number of Reviews": int(
            request.form["Number_of_Reviews"]
        ),
        "Avg Review Length": float(
            request.form["Avg_Review_Length"]
        ),
        "Ambience Score": float(
            request.form["Ambience_Score"]
        ),
        "Service Quality Score": float(
            request.form["Service_Quality_Score"]
        ),
        "Parking Availability": request.form[
            "Parking_Availability"
        ],
        "Weekend Reservations": int(
            request.form["Weekend_Reservations"]
        ),
        "Weekday Reservations": int(
            request.form["Weekday_Reservations"]
        )
    }])

    prediction = pipeline.predict(new_data)[0]

    return render_template(
        "index.html",
        result=round(prediction, 2)
    )



if __name__ == "__main__":
    app.run(debug=True)
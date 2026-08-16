from flask import Flask, render_template, request

app = Flask(__name__)


# -----------------------------------
# CAMPUS QUEUE DATA
# -----------------------------------

queue_data = {

    "Canteen": {
        "people": 42,
        "crowd": "High",
        "wait": 24,
        "recommendation": "Avoid the current rush. Try visiting after 15 minutes.",
        "best_time": "2:30 PM - 3:00 PM"
    },

    "Library": {
        "people": 8,
        "crowd": "Low",
        "wait": 5,
        "recommendation": "Low crowd right now. This is a good time to visit.",
        "best_time": "Now"
    },

    "Xerox": {
        "people": 18,
        "crowd": "Medium",
        "wait": 12,
        "recommendation": "Moderate crowd. You can visit now or wait a little.",
        "best_time": "3:00 PM - 3:30 PM"
    },

    "Admin Office": {
        "people": 31,
        "crowd": "High",
        "wait": 31,
        "recommendation": "High crowd detected. Consider visiting later.",
        "best_time": "4:00 PM - 4:30 PM"
    }
}


# -----------------------------------
# HOME PAGE
# -----------------------------------

@app.route("/")
def home():
    return render_template(
        "index.html",
        queue_data=queue_data
    )


# -----------------------------------
# QUEUE PAGE
# -----------------------------------

@app.route("/queue")
def queue():

    facility = request.args.get("facility")

    selected_data = None

    if facility in queue_data:
        selected_data = queue_data[facility]

    return render_template(
        "queue.html",
        queue_data=queue_data,
        facility=facility,
        data=selected_data
    )


# -----------------------------------
# START APPLICATION
# -----------------------------------

if __name__ == "__main__":
    app.run(debug=True)
from flask import Flask, request
import pickle

app = Flask(__name__)

# load model
with open('classifier.pkl', 'rb') as f:
    model = pickle.load(f)

@app.route("/")
def home():
    return "<h1>Hello World</h1>"

@app.route("/ping")
def ping():
    return "hey there"

@app.route("/predict", methods=['GET', 'POST'])
def predict():
    if request.method == 'GET':
        return "I will make the predictions"
    else:
        loan_req = request.get_json()
        
        if loan_req['Gender'] == "Male":
            Gender = 0
        else:
            Gender = 1

        if loan_req['Married'] == "No":
            Married = 0
        else:
            Married = 1

        ApplicantIncome = loan_req['ApplicantIncome']
        LoanAmount = loan_req['LoanAmount']
        Credit_History = loan_req['Credit_History']

        input_data = [Gender, Married, ApplicantIncome, LoanAmount, Credit_History]
        result = model.predict([input_data])

        if result == 0:
            pred = "Rejected"
        else:
            pred = "Approved"

        return {"loan_approval_status": pred}

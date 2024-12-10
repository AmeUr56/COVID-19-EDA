from flask import Flask,request,jsonify,make_response

app = Flask(__name__)
app.secret_key = "0123456789"

raw_data = None
processed_data = None

@app.route("/raw_data",methods=["GET","POST"])
def raw_data():
    if request.method == "POST":
        global raw_data
        raw_data = request.get_json()
                    
        if not raw_data:
            response = make_response("Raw Data not provided.",400)

        response = make_response("Raw Data Uploaded Succefully.",201)
        return response
    
    if raw_data is None:
        return jsonify({"error": "No raw data available."}), 404
    
    return raw_data

@app.route("/processed_data",methods=["GET","POST"])
def processed_data():
    if request.method == "POST":
        global processed_data
        processed_data = request.get_json()
        
        if not processed_data:
            response = make_response("Processed Data not provided.",400)
            return response
        
        response = make_response("Processed Data Uploaded Succefully.",201)
        return response
    
    if processed_data is None:
        return jsonify({"error": "No processed data available."}), 404
    
    return processed_data
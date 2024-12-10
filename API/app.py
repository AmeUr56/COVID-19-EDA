from flask import Flask,request,jsonify,make_response

app = Flask(__name__)
app.secret_key = "0123456789"

@app.route("/raw_data",methods=["GET","POST"])
def raw_data():
    global raw_data
    
    if request.method == "POST":
        raw_data = request.form.get("raw_data")
        if not raw_data:
            response = make_response("Raw Data not provided.",400)

        response = make_response("Raw Data Uploded Succefully.",201)
        return response
    
    if processed_data is None:
        return jsonify({"error": "No raw data available."}), 404
    
    return jsonify({"raw_data": raw_data})

@app.route("/processed_data",methods=["GET","POST"])
def processed_data():
    global processed_data
    
    if request.method == "POST":
        processed_data = request.form.args.get("processed_data")
        if not processed_data:
            response = make_response("Processed Data not provided.",400)
            return response
        
        response = make_response("Processed Data Uploaded Succefully.",201)
        return response
    
    if processed_data is None:
        return jsonify({"error": "No processed data available."}), 404
    
    return jsonify({"processed_data":processed_data})
from flask import Flask, request, jsonify

app = Flask(__name__)

# Data to simulate marks
marks_list = [{"name":"Gx2DsTy","marks":32},{"name":"jiNl2Mz7j","marks":29},{"name":"bq","marks":90},{"name":"ZI1BXkeB","marks":20},{"name":"Anlp","marks":21},{"name":"I","marks":2},{"name":"g9","marks":17},{"name":"rAIgr","marks":40},{"name":"Vg6CmcSWcE","marks":41},{"name":"XRdSMBZVd","marks":84},{"name":"1MYi66YI","marks":26},{"name":"KkVK","marks":12},{"name":"Ty87mXFY","marks":68},{"name":"v3AMhAP","marks":41},{"name":"Z","marks":53},{"name":"NZwjM","marks":25},{"name":"vewL","marks":63},{"name":"Tl7VrH","marks":95},{"name":"hlpOfjq","marks":21},{"name":"g07pP","marks":8},{"name":"odq2u","marks":26},{"name":"FG","marks":45},{"name":"vybrsWW","marks":73},{"name":"yL7tGB","marks":75},{"name":"RPseF5","marks":12},{"name":"tv4tVlD8","marks":46},{"name":"DqXI7","marks":77},{"name":"lWfCenix","marks":33},{"name":"3","marks":94},{"name":"rlxT9e","marks":62},{"name":"R","marks":51},{"name":"X8T193Jpuj","marks":88},{"name":"w5nZ85LeK","marks":3},{"name":"iTkG","marks":72},{"name":"Y9whcs","marks":88},{"name":"x37AFHufM5","marks":70},{"name":"72aLG","marks":46},{"name":"fUHxIk","marks":45},{"name":"WkF","marks":68},{"name":"zY","marks":72},{"name":"tgR","marks":96},{"name":"kt","marks":15},{"name":"rjxjE","marks":19},{"name":"9mDco","marks":99},{"name":"CbiOAb","marks":42},{"name":"18","marks":80},{"name":"Qy6cwoQAwd","marks":9},{"name":"FpEMifYG","marks":95},{"name":"29reI","marks":4},{"name":"NjG","marks":53},{"name":"DUpEh9","marks":40},{"name":"fOC2","marks":37},{"name":"SEzx","marks":32},{"name":"LuPFzwrjZk","marks":77},{"name":"VVqVH0","marks":92},{"name":"wyJ0X","marks":60},{"name":"zxaGUFUky","marks":28},{"name":"2GqxlSLgvp","marks":9},{"name":"A5icjra2Uf","marks":72},{"name":"69pBf6o","marks":0},{"name":"BWiDQ8lr","marks":34},{"name":"1iR0b","marks":24},{"name":"LW3","marks":64},{"name":"qu","marks":76},{"name":"FAi0D","marks":79},{"name":"5","marks":53},{"name":"NA","marks":48},{"name":"MbKEJ1d5Y","marks":99},{"name":"aSZrTzusW","marks":4},{"name":"CtV","marks":99},{"name":"94zhrcfl","marks":10},{"name":"YB","marks":68},{"name":"9is4yz","marks":15},{"name":"schAV3","marks":86},{"name":"nu","marks":35},{"name":"YnlvVdv","marks":85},{"name":"0Ap","marks":4},{"name":"p1kvN0","marks":15},{"name":"f","marks":72},{"name":"9HcM8nBpXb","marks":29},{"name":"cmzJHN2","marks":75},{"name":"Y","marks":39},{"name":"kIsps","marks":13},{"name":"jsXEbkzxOl","marks":94},{"name":"1SPAEu","marks":42},{"name":"9nXK","marks":83},{"name":"J","marks":48},{"name":"9","marks":78},{"name":"3dsdWB6cW","marks":92},{"name":"KlqT7Uf8n1","marks":98},{"name":"EtCeRurU","marks":17},{"name":"mg1","marks":85},{"name":"R6JVcr","marks":43},{"name":"WY9V1zvA","marks":64},{"name":"qers5kERa5","marks":68},{"name":"MeEvXuiB","marks":28},{"name":"zINjk5quHW","marks":76},{"name":"bWtch706","marks":92},{"name":"PMY","marks":5},{"name":"ObRq","marks":97}]
# Helper function to find marks by name
def find_marks(name):
    for entry in marks_list:
        if entry["name"] == name:
            return entry["marks"]
    return 0  # Default if name is not found

@app.route('/api', methods=['GET'])
def get_marks():
    # Extract 'name' parameters from query string
    names = request.args.getlist('name')

    # Find marks for each name
    marks = [find_marks(name) for name in names]

    # Enable CORS by adding the necessary headers
    response = jsonify({"marks": marks})
    response.headers.add("Access-Control-Allow-Origin", "*")
    return response
   

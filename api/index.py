from flask import Flask, request, jsonify

app = Flask(__name__)

# Data to simulate marks
marks_list = [{"name":"Sp","marks":83},{"name":"NlWE8LA7U","marks":66},{"name":"r6i","marks":92},{"name":"iGP9B","marks":31},{"name":"IpG5Sa","marks":7},{"name":"fOwD4i2ykR","marks":75},{"name":"uJFvkA","marks":39},{"name":"wQ","marks":70},{"name":"SC","marks":81},{"name":"bckF","marks":32},{"name":"yWZ","marks":42},{"name":"vRtaxJw8uu","marks":26},{"name":"O0","marks":86},{"name":"HIK3ywY","marks":70},{"name":"WppKGuJEwH","marks":96},{"name":"CkkmMv","marks":29},{"name":"BD","marks":5},{"name":"P","marks":36},{"name":"LJh5aoT","marks":79},{"name":"p","marks":25},{"name":"vrCp","marks":26},{"name":"56","marks":22},{"name":"qM9","marks":79},{"name":"wDvwBtXrtD","marks":4},{"name":"e295","marks":19},{"name":"E","marks":31},{"name":"jiO","marks":37},{"name":"fgr6yS4k","marks":41},{"name":"zY02tLBw","marks":55},{"name":"B4CL8V","marks":33},{"name":"5ELkW","marks":43},{"name":"web","marks":82},{"name":"bCPT","marks":65},{"name":"KPwlifY","marks":43},{"name":"AW","marks":99},{"name":"v","marks":43},{"name":"aLFbwpTNTp","marks":21},{"name":"32jGYc8f4a","marks":41},{"name":"i5zN1BT","marks":92},{"name":"ijJcfAEF3","marks":95},{"name":"HZerG","marks":78},{"name":"nrZ1knuize","marks":46},{"name":"oS4","marks":29},{"name":"c","marks":32},{"name":"hS75","marks":68},{"name":"yrvn14r","marks":4},{"name":"POm","marks":27},{"name":"jvK6","marks":29},{"name":"acDLy7eYf","marks":96},{"name":"hjPfOMX","marks":51},{"name":"chn","marks":3},{"name":"deLr","marks":90},{"name":"9","marks":31},{"name":"4tO","marks":91},{"name":"iyF0rczD","marks":68},{"name":"nq","marks":41},{"name":"CDoOV","marks":48},{"name":"HHmCUmZ5","marks":15},{"name":"bsb","marks":77},{"name":"4x76MX1","marks":32},{"name":"JnH0","marks":23},{"name":"aQO","marks":39},{"name":"fT","marks":72},{"name":"3dv3AMO","marks":84},{"name":"oNrStb","marks":79},{"name":"K6Gb","marks":1},{"name":"xYjakVA","marks":75},{"name":"e","marks":39},{"name":"6cm","marks":34},{"name":"3GiXJ8S","marks":19},{"name":"w1bbpZt5","marks":81},{"name":"WucY","marks":90},{"name":"wFnfki","marks":31},{"name":"eFc0XKKO","marks":28},{"name":"lfild","marks":8},{"name":"HnbbRFfA8","marks":68},{"name":"AF0","marks":63},{"name":"ir","marks":23},{"name":"hgKnhDcC1","marks":40},{"name":"R","marks":46},{"name":"2K0u8V2","marks":63},{"name":"4LkQXVOlW","marks":37},{"name":"pMc1GNr","marks":62},{"name":"LH","marks":90},{"name":"Un33K","marks":40},{"name":"xzs2g","marks":95},{"name":"Bg","marks":17},{"name":"nfM","marks":45},{"name":"DrhwblNzLL","marks":65},{"name":"48bew9","marks":13},{"name":"cGUuj","marks":16},{"name":"1JZoLD","marks":27},{"name":"Dl","marks":59},{"name":"BG3rD5Lx","marks":83},{"name":"2mG9uGy7Xi","marks":81},{"name":"jxi68fc","marks":14},{"name":"Xdgi","marks":98},{"name":"WOm4Vqys8H","marks":43},{"name":"ZEVmw1a","marks":87},{"name":"B","marks":96}]

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

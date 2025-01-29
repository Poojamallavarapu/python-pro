from flask import Flask, request, jsonify

app = Flask(__name__)

# Data to simulate marks
marks_list = [{"name":"Gx2DsTy","marks":81},{"name":"iNl2Mz","marks":95},{"name":"KbqvZI","marks":86},{"name":"X","marks":58},{"name":"BVAnl","marks":66},{"name":"I","marks":16},{"name":"9YrAIg","marks":70},{"name":"Vg6CmcSWcE","marks":87},{"name":"RdSM","marks":2},{"name":"Vdu1M","marks":39},{"name":"66YIXK","marks":59},{"name":"KtTy","marks":97},{"name":"mXFYnv3AMh","marks":1},{"name":"BZe","marks":22},{"name":"wjMTv","marks":49},{"name":"LfTl7VrH","marks":62},{"name":"lpOfjq","marks":49},{"name":"07pPbo","marks":46},{"name":"2uJFGpv","marks":80},{"name":"rsWWj","marks":81},{"name":"7t","marks":10},{"name":"h","marks":28},{"name":"seF","marks":92},{"name":"tv4tVlD8","marks":46},{"name":"q","marks":38},{"name":"7t","marks":60},{"name":"fCen","marks":56},{"name":"E3irlxT9","marks":49},{"name":"R","marks":98},{"name":"8T19","marks":90},{"name":"pu","marks":57},{"name":"w5nZ85LeK","marks":30},{"name":"TkGiY9","marks":78},{"name":"cs7x37","marks":0},{"name":"H","marks":75},{"name":"M5Z72a","marks":18},{"name":"kf","marks":32},{"name":"xI","marks":58},{"name":"WkF","marks":10},{"name":"YOtgRKktc","marks":70},{"name":"xjEZ9m","marks":5},{"name":"oEZgC","marks":44},{"name":"OAbJ18","marks":95},{"name":"y6c","marks":78},{"name":"QAwdsFp","marks":7},{"name":"ifY","marks":10},{"name":"29reI","marks":27},{"name":"jGi","marks":6},{"name":"pEh9","marks":39},{"name":"OC2TSE","marks":83},{"name":"7LuPFzwrj","marks":40},{"name":"jVVqVH","marks":84},{"name":"wyJ0X","marks":87},{"name":"xaGUFUky8","marks":88},{"name":"qx","marks":60},{"name":"Lgv","marks":67},{"name":"A5icjra2Uf","marks":66},{"name":"9pBf6osBWi","marks":6},{"name":"8lr","marks":40},{"name":"iR0bQLW3H","marks":68},{"name":"aFAi0DC5","marks":16},{"name":"A0M","marks":44},{"name":"EJ","marks":86},{"name":"5Y0aS","marks":40},{"name":"TzusWPC","marks":73},{"name":"x94z","marks":53},{"name":"cflJYBj","marks":99},{"name":"s4yzks","marks":45},{"name":"AV3Gnu","marks":66},{"name":"nlvVd","marks":76},{"name":"0Ap","marks":58},{"name":"1kvN0Ef","marks":97},{"name":"HcM8nBpXbo","marks":45},{"name":"zJHN2BY","marks":42},{"name":"Isps6j","marks":71},{"name":"Ebkz","marks":79},{"name":"lj1","marks":29},{"name":"AEu","marks":35},{"name":"nXKAJC903d","marks":71},{"name":"WB6cW","marks":94},{"name":"lq","marks":32},{"name":"Uf8n1sEtCe","marks":28},{"name":"rUOmg1fR","marks":94},{"name":"Vc","marks":69},{"name":"WY9V1zvA","marks":92},{"name":"ers5kER","marks":42},{"name":"vMeEvXuiB8","marks":82},{"name":"Nj","marks":59},{"name":"quHWxbWtch","marks":96},{"name":"6MPMYUObR","marks":68},{"name":"S4MN","marks":2},{"name":"ZZ","marks":84},{"name":"HqZ","marks":53},{"name":"n7N","marks":8},{"name":"ctu","marks":12},{"name":"vU6mg","marks":88},{"name":"s","marks":88},{"name":"ccqs8JL9","marks":42},{"name":"F7ChYXUv5","marks":60},{"name":"FtA","marks":34}]

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
   

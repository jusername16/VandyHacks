import urllib, json,requests
def main():
    UsherLocation = "Kissam College Hall".replace(" ", "+")
    EchoLocation = "The Wondry".replace(" ", "+")
    API_KEY = "AIzaSyAJTw_aMHrgAt9uBBIOGoZnAjWtdKu_kVw"
    requestURL = "https://maps.googleapis.com/maps/api/distancematrix/json?units=imperial&origins=" + EchoLocation + "&destinations=" + UsherLocation + "&key=AIzaSyAJTw_aMHrgAt9uBBIOGoZnAjWtdKu_kVw"
    r = requests.get(requestURL)
    jdata = r.json()
    distanceBetween = jdata['rows'][0]['elements'][0]['distance']['text']
    if "ft" in distanceBetween:
        distanceBetween = float(distanceBetween.replace(" ft", "")) * 0.000189393939
    distanceBetween = str(distanceBetween).replace(" mi", "")
    if float(distanceBetween) < 1:
        print "You're In"
    else:
        print "You're not Verified"

if  __name__ =='__main__':
    main()

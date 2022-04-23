from flask import Flask,render_template,request,make_response
import subprocess
import os
import connect

app = Flask(__name__)
    
@app.route("/")
def landing():
    essid = os.popen('sudo iw wlan0 scan | egrep \'SSID\'', 'r')
    essid = essid.read()
    essid = essid.split('\n')
    essid = ["this is the 1st wifi", "this is the 2nd wifi", "this is the 3rd wifi"]
    return render_template('index.html', essid = essid)

@app.route("/connect", methods=["POST"])
def repeaterConf():    
    ssid = request.form['essid']
    print(ssid)
    password = request.form['pass']
    scheme = connect.SchemeWPA('wlan1', ssid, {"ssid": ssid,"psk": password})
    scheme.save()
    
    subprocess.Popen(['shutdown','-r','now'])
    
if __name__=="__main__":
    app.run(debug=True, host='0.0.0.0', port=81)
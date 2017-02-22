import requests
import time
import thread
import threading
from flask import Flask, render_template
from sites import *

urls= adrs


def serverCheck():
    while True:
        for url in urls:
            
            try:
                #Send a request to the URL and set status code to dict
                s = requests.get("http://"+url)
                urls.__setitem__(url,s.status_code)
            except:
                #If site doesn't exist
                urls.__setitem__(url,"Error")

        #Wait 60 seconds
        print("Waiting before refresh...")
        time.sleep(60)
    
servChk = threading.Thread(target=serverCheck)

app = Flask(__name__)

@app.route('/')
def hello():
    return render_template("index.html", urls = urls)    

if __name__ == '__main__':
    servChk.start()
    app.run(port=1025) #debug=True
    #app.run(host='0.0.0.0', port=1025, debug=False, **options)

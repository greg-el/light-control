from flask import Flask
from flask import render_template, redirect
from rpi_rf import RFDevice
app = Flask(__name__)

TRANSMIT_PIN = 2
ON_MAIN = 70741
ON_SEC = 83029
OFF_MAIN = 70740
OFF_SEC = 83028
TRANS_LENGTH = 350
PROTOCOL = 1


@app.route("/")
def main_page():
    return render_template("main.html")

@app.route("/allon")
def all_on():
    trans = RFDevice(TRANSMIT_PIN)
    trans.enable_tx()
    trans.tx_repeat = 10
    trans.tx_code(ON_MAIN, PROTOCOL, TRANS_LENGTH, 24)
    trans.tx_code(ON_SEC, PROTOCOL, TRANS_LENGTH, 24)
    trans.cleanup()
    return redirect("/")

@app.route("/alloff")
def all_off():
    trans = RFDevice(TRANSMIT_PIN)
    trans.enable_tx()
    trans.tx_repeat = 10
    trans.tx_code(OFF_MAIN, PROTOCOL, TRANS_LENGTH, 24)
    trans.tx_code(OFF_SEC, PROTOCOL, TRANS_LENGTH, 24) 
    trans.cleanup()
    return redirect("/")

@app.route("/mainon")
def main_on():
    trans = RFDevice(TRANSMIT_PIN)
    trans.enable_tx()
    trans.tx_repeat = 10
    trans.tx_code(ON_MAIN, PROTOCOL, TRANS_LENGTH, 24)
    trans.cleanup()
    return redirect("/")

@app.route("/mainoff")
def main_off():
    trans = RFDevice(TRANSMIT_PIN)
    trans.enable_tx()
    trans.tx_repeat = 10
    trans.tx_code(OFF_MAIN, PROTOCOL, TRANS_LENGTH, 24)
    trans.cleanup()
    return redirect("/")

@app.route("/secon")
def sec_on():
    trans = RFDevice(TRANSMIT_PIN)
    trans.enable_tx()
    trans.tx_repeat = 10
    trans.tx_code(ON_SEC, PROTOCOL, TRANS_LENGTH, 24)
    trans.cleanup()
    return redirect("/")

@app.route("/secoff")
def sec_off():
    trans = RFDevice(TRANSMIT_PIN)
    trans.enable_tx()
    trans.tx_repeat = 10
    trans.tx_code(OFF_SEC, PROTOCOL, TRANS_LENGTH, 24)
    trans.cleanup()
    return redirect("/")
    

if __name__ == "__main__":
    app.run(host="0.0.0.0")


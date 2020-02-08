import config
import threading
from flask import Flask
from flask import render_template, redirect
from rpi_rf import RFDevice
app = Flask(__name__)

TRANSMIT_PIN = 2
ON_MAIN = 70741
ON_SEC = 83029
OFF_MAIN = 70740
OFF_SEC = 83028
ON_LAMP = 86101
OFF_LAMP = 86100
TRANS_LENGTH = 350
PROTOCOL = 1

@app.route("/")
def main_page():
    return render_template("main.html")

@app.route("/allon")
def all_on():
    threads.append(x)
    trans = RFDevice(TRANSMIT_PIN)
    trans.enable_tx()
    trans.tx_repeat = 10
    #trans.tx_code(ON_MAIN, PROTOCOL, TRANS_LENGTH, 24)
    #trans.tx_code(ON_SEC, PROTOCOL, TRANS_LENGTH, 24)
    #trans.tx_code(ON_LAMP, PROTOCOL, TRANS_LENGTH, 24)
    main_thread = threading.Thread(target=lambda: tratrans.tx_code(ON_MAIN, PROTOCOL, TRANS_LENGTH, 24)).start()
    sec_thread = threading.Thread(target=lambda:trans.tx_code(ON_SEC, PROTOCOL, TRANS_LENGTH, 24)).start()
    lamp_thread = threading.Thread(target=lambda:trans.tx_code(ON_LAMP, PROTOCOL, TRANS_LENGTH, 24)).start()
    config.main_state = 1
    config.sec_state = 1
    config.lamp_state = 1
    trans.cleanup()
    return redirect("/")

@app.route("/alloff")
def all_off():
    trans = RFDevice(TRANSMIT_PIN)
    trans.enable_tx()
    trans.tx_repeat = 10
    #trans.tx_code(OFF_MAIN, PROTOCOL, TRANS_LENGTH, 24)
    #trans.tx_code(OFF_SEC, PROTOCOL, TRANS_LENGTH, 24)
    #trans.tx_code(OFF_LAMP, PROTOCOL, TRANS_LENGTH, 24)
    main_thread = threading.Thread(target=lambda:tratrans.tx_code(OFF_MAIN, PROTOCOL, TRANS_LENGTH, 24)).start()
    sec_thread = threading.Thread(target=lambda:trans.tx_code(OFF_SEC, PROTOCOL, TRANS_LENGTH, 24)).start()
    lamp_thread = threading.Thread(target=lambda:trans.tx_code(OFF_LAMP, PROTOCOL, TRANS_LENGTH, 24)).start()
    config.main_state = 0
    config.sec_state = 0
    config.lamp_state = 0 
    trans.cleanup()
    return redirect("/")


@app.route("/maintoggle")
def main_toggle():
    if config.main_state == 0:
        return redirect("/mainon")
    else:
        return redirect("/mainoff")


@app.route("/mainon")
def main_on():
    trans = RFDevice(TRANSMIT_PIN)
    trans.enable_tx()
    trans.tx_repeat = 10
    trans.tx_code(ON_MAIN, PROTOCOL, TRANS_LENGTH, 24)
    trans.cleanup()
    config.main_state = 1
    return redirect("/")

@app.route("/mainoff")
def main_off():
    trans = RFDevice(TRANSMIT_PIN)
    trans.enable_tx()
    trans.tx_repeat = 10
    trans.tx_code(OFF_MAIN, PROTOCOL, TRANS_LENGTH, 24)
    trans.cleanup()
    config.main_state = 0
    return redirect("/")

@app.route("/sectoggle")
def sec_toggle():
    if config.sec_state == 0:
        return redirect("/secon")
    else:
        return redirect("/secoff")

@app.route("/secon")
def sec_on():
    trans = RFDevice(TRANSMIT_PIN)
    trans.enable_tx()
    trans.tx_repeat = 10
    trans.tx_code(ON_SEC, PROTOCOL, TRANS_LENGTH, 24)
    trans.cleanup()
    config.sec_state = 1
    return redirect("/")

@app.route("/secoff")
def lamp_off():
    trans = RFDevice(TRANSMIT_PIN)
    trans.enable_tx()
    trans.tx_repeat = 10
    trans.tx_code(OFF_SEC, PROTOCOL, TRANS_LENGTH, 24)
    trans.cleanup()
    config.sec_state = 0
    return redirect("/")

@app.route("/lamptoggle")
def lamp_toggle():
    if config.lamp_state == 0:
        return redirect("/lampon")
    else:
        return redirect("/lampoff")

@app.route("/lampon")
def lamp_on():
    trans = RFDevice(TRANSMIT_PIN)
    trans.enable_tx()
    trans.tx_repeat = 10
    trans.tx_code(ON_LAMP, PROTOCOL, TRANS_LENGTH, 24)
    trans.cleanup()
    config.lamp_state = 1
    return redirect("/")

@app.route("/lampoff")
def sec_off():
    trans = RFDevice(TRANSMIT_PIN)
    trans.enable_tx()
    trans.tx_repeat = 10
    trans.tx_code(OFF_LAMP, PROTOCOL, TRANS_LENGTH, 24)
    trans.cleanup()
    config.lamp_state = 0
    return redirect("/")
    

if __name__ == "__main__":
    app.run(host="0.0.0.0")


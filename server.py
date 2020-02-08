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
main_state = 0
sec_state = 0
lamp_state = 0


@app.route("/")
def main_page():
    return render_template("main.html")

@app.route("/allon")
def all_on():
    global main_state
    global sec_state 
    global lamp_state
    trans = RFDevice(TRANSMIT_PIN)
    trans.enable_tx()
    trans.tx_repeat = 10
    trans.tx_code(ON_MAIN, PROTOCOL, TRANS_LENGTH, 24)
    trans.tx_code(ON_SEC, PROTOCOL, TRANS_LENGTH, 24)
    trans.tx_code(ON_LAMP, PROTOCOL, TRANS_LENGTH, 24)
    main_state = 1
    sec_state = 1
    lamp_state = 1
    trans.cleanup()
    return redirect("/")

@app.route("/alloff")
def all_off():
    global main_state
    global sec_state 
    global lamp_state
    trans = RFDevice(TRANSMIT_PIN)
    trans.enable_tx()
    trans.tx_repeat = 10
    trans.tx_code(OFF_MAIN, PROTOCOL, TRANS_LENGTH, 24)
    trans.tx_code(OFF_SEC, PROTOCOL, TRANS_LENGTH, 24)
    trans.tx_code(OFF_LAMP, PROTOCOL, TRANS_LENGTH, 24)
    main_state = 0
    sec_state = 0
    lamp_state = 0 
    trans.cleanup()
    return redirect("/")


@app.route("/maintoggle")
def main_toggle():
    global main_state
    if main_state == 0:
        main_on()
        main_state = 1
    else:
        main_off()
        main_state = 0

@app.route("/mainon")
def main_on():
    global main_state
    trans = RFDevice(TRANSMIT_PIN)
    trans.enable_tx()
    trans.tx_repeat = 10
    trans.tx_code(ON_MAIN, PROTOCOL, TRANS_LENGTH, 24)
    trans.cleanup()
    main_state = 1
    return redirect("/")

@app.route("/mainoff")
def main_off():
    global main_state
    trans = RFDevice(TRANSMIT_PIN)
    trans.enable_tx()
    trans.tx_repeat = 10
    trans.tx_code(OFF_MAIN, PROTOCOL, TRANS_LENGTH, 24)
    trans.cleanup()
    main_state = 0
    return redirect("/")

@app.route("/sectoggle")
def sec_toggle():
    global sec_state
    if sec_state == 0:
        sec_on()
        sec_state = 1
    else:
        sec_off()
        sec_state = 0

@app.route("/secon")
def sec_on():
    global sec_state
    trans = RFDevice(TRANSMIT_PIN)
    trans.enable_tx()
    trans.tx_repeat = 10
    trans.tx_code(ON_SEC, PROTOCOL, TRANS_LENGTH, 24)
    trans.cleanup()
    sec_state = 1
    return redirect("/")

@app.route("/secoff")
def lamp_off():
    global sec_state
    trans = RFDevice(TRANSMIT_PIN)
    trans.enable_tx()
    trans.tx_repeat = 10
    trans.tx_code(OFF_SEC, PROTOCOL, TRANS_LENGTH, 24)
    trans.cleanup()
    sec_state = 0
    return redirect("/")

@app.route("/lamptoggle")
def lamp_toggle():
    global lamp_state
    if lamp_state == 0:
        lamp_on()
        lamp_state = 1
    else:
        lamp_off()
        lamp_state = 0

@app.route("/lampon")
def lamp_on():
    global lamp_state
    trans = RFDevice(TRANSMIT_PIN)
    trans.enable_tx()
    trans.tx_repeat = 10
    trans.tx_code(ON_LAMP, PROTOCOL, TRANS_LENGTH, 24)
    trans.cleanup()
    lamp_state = 1
    return redirect("/")

@app.route("/lampoff")
def sec_off():
    global lamp_state
    trans = RFDevice(TRANSMIT_PIN)
    trans.enable_tx()
    trans.tx_repeat = 10
    trans.tx_code(OFF_LAMP, PROTOCOL, TRANS_LENGTH, 24)
    trans.cleanup()
    lamp_state = 0
    return redirect("/")
    

if __name__ == "__main__":

    app.run(host="0.0.0.0")


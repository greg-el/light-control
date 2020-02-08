import config
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

def transmit(job_list=[]):
    trans = RFDevice(TRANSMIT_PIN)
    trans.enable_tx()
    trans.tx_repeat = 10
    for job in job_list:
        trans.tx_code(job, PROTOCOL, TRANS_LENGTH, 24)
        if job == ON_MAIN:
            config.main_state = 1
        elif job == OFF_MAIN:
            config.main_state = 0
        elif job == ON_SEC:
            config.sec_state = 1
        elif job == OFF_SEC:
            config.sec_state = 0
        elif job == ON_LAMP:
            config.lamp_state = 1
        elif job == OFF_LAMP:
            config.lamp_state = 0

    trans.cleanup()
        

@app.route("/")
def main_page():
    return render_template("main.html")

@app.route("/allon")
def all_on():
    transmit([ON_MAIN, ON_SEC, ON_LAMP])
    return redirect("/")

@app.route("/alloff")
def all_off():
    transmit([OFF_MAIN, OFF_SEC, OFF_LAMP])
    return redirect("/")


@app.route("/maintoggle")
def main_toggle():
    if config.main_state == 0:
        return redirect("/mainon")
    else:
        return redirect("/mainoff")


@app.route("/mainon")
def main_on():
    transmit([ON_MAIN])
    return redirect("/")

@app.route("/mainoff")
def main_off():
    transmit([OFF_MAIN])
    return redirect("/")

@app.route("/sectoggle")
def sec_toggle():
    if config.sec_state == 0:
        return redirect("/secon")
    else:
        return redirect("/secoff")

@app.route("/secon")
def sec_on():
    transmit([ON_SEC])
    return redirect("/")

@app.route("/secoff")
def lamp_off():
    transmit([OFF_SEC])
    return redirect("/")

@app.route("/lamptoggle")
def lamp_toggle():
    if config.lamp_state == 0:
        return redirect("/lampon")
    else:
        return redirect("/lampoff")

@app.route("/lampon")
def lamp_on():
    transmit([ON_LAMP])
    return redirect("/")

@app.route("/lampoff")
def sec_off():
    transmit([OFF_LAMP])
    return redirect("/")
    

if __name__ == "__main__":
    app.run(host="0.0.0.0")


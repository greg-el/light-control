import argparse
from rpi_rf import RFDevice

TRANSMIT_PIN = 2
ON_MAIN = 70741
ON_SEC = 83029
OFF_MAIN = 70740
OFF_SEC = 83028
ON_LAMP = 86101
OFF_LAMP = 86100
TRANS_LENGTH = 350
PROTOCOL = 2

trans = RFDevice(TRANSMIT_PIN)
trans.enable_tx()
trans.tx_repeat = 10

parser = argparse.ArgumentParser()
parser.add_argument("--on")
parser.add_argument("--off")

args = parser.parse_args()

print(args)

if args.on:
    if args.on == "main":
        trans.tx_code(ON_MAIN, PROTOCOL, TRANS_LENGTH, 24)
        trans.cleanup()
    elif args.on == "sec":
        trans.tx_code(ON_SEC, PROTOCOL, TRANS_LENGTH, 24)
        trans.cleanup()
    elif args.on == "lamp":
        trans.tx_code(ON_LAMP, PROTOCOL, TRANS_LENGTH, 24)
    elif args.on == "all":
        trans.tx_code(ON_MAIN, PROTOCOL, TRANS_LENGTH, 24)
        trans.tx_code(ON_SEC, PROTOCOL, TRANS_LENGTH, 24)
        trans.tx_code(ON_LAMP, PROTOCOL, TRANS_LENGTH, 24)
        trans.cleanup()

if args.off:
    if args.off == "main":
        trans.tx_code(OFF_MAIN, PROTOCOL, TRANS_LENGTH, 24)
        trans.cleanup()
    elif args.off == "sec":
        trans.tx_code(OFF_SEC, PROTOCOL, TRANS_LENGTH, 24)
        trans.cleanup()
    elif args.off == "all":
        trans.tx_code(OFF_MAIN, PROTOCOL, TRANS_LENGTH, 24)
        trans.tx_code(OFF_SEC, PROTOCOL, TRANS_LENGTH, 24)
        trans.tx_code(OFF_LAMP, PROTOCOL, TRANS_LENGTH, 24)
        trans.cleanup()






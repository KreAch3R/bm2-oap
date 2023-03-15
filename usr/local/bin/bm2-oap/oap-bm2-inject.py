#!/usr/bin/python3
#
#  Copyright (C) BlueWave Studio - All Rights Reserved
#
#  Modified by KreAch3R to support BM2
#

# Import common functions
import sys
import threading
import time
import common.Api_pb2 as oap_api
from common.Client import Client, ClientEventHandler
import paho.mqtt.subscribe as subscribe

# Set global and tracking variables
CLIENT_NAME = "OAP BM2 OBD INJECT"
t_injecting_active = True
logging = False


###############################################################
# CONNECTING TO MQTT Battery Monitor 2 Publisher

def get_mtqq_message():
    # https://stackoverflow.com/a/66766208/4008886
    msg = subscribe.simple("bm2")
    battery_voltage = msg.payload.decode()
    #print("Voltage:",battery_voltage, flush=True)
    print("Voltage:{}".format(battery_voltage), end="\r", flush=True)
    return float(battery_voltage)

###############################################################
# ACTUAL INJECTING INTO API

def inject_obd_gauge_formula_value(client):
    obd_inject_gauge_formula_value = oap_api.ObdInjectGaugeFormulaValue()

    while t_injecting_active:

        for formula in [("getPidValue(9)")]:
            obd_inject_gauge_formula_value.formula = formula
            obd_inject_gauge_formula_value.value = get_mtqq_message()

            client.send(oap_api.MESSAGE_OBD_INJECT_GAUGE_FORMULA_VALUE, 0,
                        obd_inject_gauge_formula_value.SerializeToString())
            if logging:
                print("sent to OAP!", flush=True)

        time.sleep(2)


###############################################################
# OBD INJECT OFFICIAL OAP CODE - HELPER FUNCTIONS AND MAIN LOOP

class EventHandler(ClientEventHandler):

    def on_hello_response(self, client, message):
        threading.Thread(target=inject_obd_gauge_formula_value,
                         args=(client, )).start()


def main():
    event_handler = EventHandler()
    oap_client = Client(CLIENT_NAME)
    oap_client.set_event_handler(event_handler)
    oap_client.connect('127.0.0.1', 44405)

    print("Starting injection...", flush=True)
    active = True
    while active:
        try:
            active = oap_client.wait_for_message()
            if logging:
                print("waiting for api connection", flash=True)
        except KeyboardInterrupt:
            break

    global t_injecting_active
    t_injecting_active = False

    oap_client.disconnect()


if __name__ == "__main__":
    main()

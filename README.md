# BM2-OAP
Battery Monitor 2 (BM2) - OpenAuto for RPI integration

Connect your BM2 (Battery Monitor 2) car battery monitor to your raspberry pi running OpenAuto and use the OBD2 injection service to display the car battery voltage in the Dashboards section:

[Google Play](https://play.google.com/store/apps/details?id=com.dc.battery.monitor2&hl=en)

![image](https://user-images.githubusercontent.com/2224376/225339521-3d725866-8085-41ea-b497-c8f8aea415ba.png)

<a href="https://www.paypal.com/donate/?business=R9V8AAFPNV684&no_recurring=0&currency_code=EUR">
<img src="https://raw.githubusercontent.com/stefan-niedermann/paypal-donate-button/master/paypal-donate-button.png" alt="Donate with PayPal" width="300">
</a>

# Acknowledgement

* **HUGE** thank you to https://github.com/KrystianD because he reverse-engineered the bluetooth connection between the Android app and the BM2 monitor. He did half and the most important work.

* Also, thank you to user "**JonLB"** in the BlueWave forums for the OBDInject example here: https://bluewavestudio.io/community/thread-3634.html. Great proof of concept. 

# Requirements

1. [https://github.com/KrystianD/bm2-battery-monitor](bm2-battery-monitor)
2. [https://bluewavestudio.io/shop/openauto-pro-car-head-unit-solution/](OpenAuto)
3. The monitor device

# Installation Requirements

My ["NaviPi USB Update"](https://github.com/KreAch3R/navipi-usb-update) solution is supposed to be used, this is how this repository is structured. I have also included the necessary dependencies in the `bm2-oap_update.sh` file.

But you can always do it manually, install the files, enable the services, etc.

**IMPORTANT**:
1. Add your BM2 Bluetooth device MAC address in the `bm2_mqtt.service`. You can find it using the Android App.
2. The services are expecting a log folder location at `~/Logs`. If you don't want that, change it.

# Confirming the install

After running both services, the expected output for `bm2_mqtt` service is:
```
[2023-03-15 16:38:12] Performing forceful device disconnection
[2023-03-15 16:38:20] Connected
```
And for `openauto_obd_inject`:
```
Starting injection...
Voltage: 12.35V
```

# The End Result: 

<img src="https://user-images.githubusercontent.com/2224376/225339687-71e9e841-73b2-48fc-91aa-b1ed3c5147ab.jpg" width="800" height="500">

# Future To-Do

* Convince OAP developers that a `lowerLimit` key needs to be added into Dashboards Gauges, so that there is a safe _lower_ limit for the car battery. 
* Add a percentage indicator


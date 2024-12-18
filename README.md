# USB-picoducky
convert your raspberry pi pico into a USB-rubberducky or Bad-Usb

how to install

1.delete all the files in your pi pico by holding the bootsel boton on your pi and copying the file called "flash_nuke.uf2" to it
![Picture1](https://github.com/user-attachments/assets/9926801f-526b-44c8-9af4-f6385d44e13f)
![Picture2](https://github.com/user-attachments/assets/525eca39-98e1-4f3e-84e3-53f224f58b66)

2.it should disconnect and reconnect to your pc

3.install circuit_python by copying the file called "adafruit-circuitpython-raspberry_pi_pico-en_US-7.2.3.uf2" to the pi
![Picture3](https://github.com/user-attachments/assets/88ccb823-a481-4c44-bdfd-284210af6c5c)

4.again this will make your pi disconnect and reconnect to your pc

5.it should look like this
![Captura de pantalla 2024-12-18 170010](https://github.com/user-attachments/assets/29099abd-cfe9-4a08-940f-c12b69e62435)

6.copy the adafruit_hid to the lib folder in your pi 
![Picture4](https://github.com/user-attachments/assets/8dc5290d-25e2-43a4-b7f7-0dbaa2da5b51)


7.move the code_xx.py file in the repo depending of your keyboard layout to the main directory in the pi
![Picture5](https://github.com/user-attachments/assets/046d1377-eac6-4a28-947c-6cfedfdecd48)
8.rename the file as code.py

9.enjoy your rubberducky

how to enter a payload

1.open code.py in the editor of your choice
![Captura de pantalla 2024-12-18 174539](https://github.com/user-attachments/assets/0583d5b1-3c9a-4d1f-94b5-0dde3f6f7f26)

2.go to the function payload()
![Captura de pantalla 2024-12-18 174923](https://github.com/user-attachments/assets/97092b60-e8b7-4e57-8543-8ffa084969ab)

3.enter your payload if you dont know how to create one consult docs.txt for futher information or use example.txt

how to edit the payload once you already upload one

1.put a jumper between 3.3 volts and pin GP0 this will block the payload from executing
![Picture6](https://github.com/user-attachments/assets/ac126014-c93c-4699-a39c-461fb84c7239)

2.follow the guide "how to enter a payload"

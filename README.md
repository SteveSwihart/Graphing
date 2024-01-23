# Graphing
## Description
These 2 folders are for 2 different brands of UV LEDs I did lifetime testing on, in my garage, during the pandemic.

![UV_LED_Testing_inGarage](https://github.com/SteveSwihart/Graphing/assets/26351884/48d44ff4-9aec-4f3f-8087-1bf6ec908dc6)

There is a large heat sink in each box, and an array of LEDs on a metal fab. Each box has a camera and a fiber near the camera to allow LED output spectrum to be measured periodically. There are thermocouples in the room, in the box (upper left of image), and on bonded to the fab for temp data. Voltage, current and temp are recorded to a text file which is read by the python file each time new data is taken and saved (data points added). Here is the Eotron setup and a closup

![EotronBoxOpenXSmall](https://github.com/SteveSwihart/Graphing/assets/26351884/eb457268-2782-4969-8b35-d92fd2ab9aec) ![EotronUV_LED_Closeup(282Tall)](https://github.com/SteveSwihart/Graphing/assets/26351884/9c9722ce-c61c-45bc-9625-2bd30f11e9d6)



Eotron was my first significant python graphing task. I learned from it.

Violumas started a few months later.

## Files
for Eotron, run "Eotron, All Charts.py", and have "EotronDataAferPoint245.txt", "Spectral Scan, 1-Jul-20,270-290.txt" and "Fiber Spec Scan After 640 Hrs, 1 sec.txt" present. First txt is the starting LED spectra, and Those are all that's needed.

for Violumas, run "ViolumasTriColorV3.1_Graphs.py", and have "ViolumasTriColorV3.1Data.txt" and "Violumas3_1_LED_Spectral_Data.txt" present.


## Output
### Eotron dashboard
![Graph image](https://github.com/SteveSwihart/Graphing/blob/master/EotronUV_LEDs/Eotron%20Graphs%20as%20of%204005%20hrs.png)

### Violumas dashboard
![Graph image](https://github.com/SteveSwihart/Graphing/blob/master/ViolumasUV_LEDs/Violumas%203.1%20Tri%20Color%20Plots%20%40%201467%20hrs.png)

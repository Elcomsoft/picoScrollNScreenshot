# picoScrollNScreenshot
A solution to emulate a keyboard for scrolling the screen and taking screenshots

### Installation
1) Flash circuitpython to your Raspberry Pi Pico  
1.1) Press and hold BOOTSEL button  
1.2) Connect the USB cable to your computer  
1.3) Copy the **.uf2** file onto the newly detected drive called `RPI-RP2`   
1.4) The drive will re-attach with the new name `CIRCUITPY`
2) Install the code   
2.1) Delete all files on the `CIRCUITPY` drive   
2.2) Copy the `lib` directory to the `CIRCUITPY` drive   
2.3) Copy the `code.py` file to the `CIRCUITPY` drive  
3) Done


### Usage 
Every time you plug the Raspberry Pi Pico into the computer (or iPhone), it will wait 15 seconds. During this time you can delete the `code.py` file on the `CIRCUITPY` drive to disable keyinjection. After the 15 seconds, the device will inject the keystrokes `PAGE_DOWN` to scroll down and `SHIT+CMD+3` to take a screenshot in an infinite loop until you unplug the device.
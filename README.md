# gesture-multimedia
Using mediapipe to recognize gestures and control the computer's multimedia keys.



### NOTE: 
OS: EndeavourOS 6.8.2 (Linux) 
If you are on Linux, you might need to give admin permissions to run the code due to a library.
In addition, I cannot guarentee your keycode for the multimedia controls are the same as mine. 
This has not been tested on Windows or MacOS. 
This coul definitely be better. 

## Issues known: 
Model might just stop detecting gestures for awhile. \
Program has no real method to delay input key being sent without possibly affecting gesture detection.\
Dataset is not the best for this task; You should probably make your own dataset (with MediaPipe Hand Landmarks Detection).\
It just messy. 







# An example:

![](https://github.com/TrungBien/gesture-multimedia/blob/main/other/example.GIF)


Stay safe and happy folks.

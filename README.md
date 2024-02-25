# Gaze AutoScroll

This Project is built on a modified version of Antoine Lamé's Gaze Tracking demo version and has the added functionality of detecting gazes in vertical direction to simulate a Mouse Scroll. 

# Gaze Tracking

![made-with-python](https://img.shields.io/badge/Made%20with-Python-1f425f.svg)
![Open Source Love](https://badges.frapsoft.com/os/v1/open-source.svg?v=103)
![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)
[![GitHub stars](https://img.shields.io/github/stars/antoinelame/GazeTracking.svg?style=social)](https://github.com/antoinelame/GazeTracking/stargazers)

This is a Python (2 and 3) library that provides a **webcam-based eye tracking system**. It gives you the exact position of the pupils and the gaze direction, in real time.

[![Demo](https://i.imgur.com/WNqgQkO.gif)](https://youtu.be/YEZMk1P0-yw)

_🚀 Quick note: I'm looking for job opportunities as a software developer, for exciting projects in ambitious companies. Anywhere in the world. Send me an email!_

## Installation

Clone this project:

```shell
git clone https://github.com/antoinelame/GazeTracking.git
```

### For Pip install
Install these dependencies (NumPy, OpenCV, Dlib, Plyer, Mouse, Keyboard):

```shell
pip install -r requirements.txt
```

> The Dlib library has four primary prerequisites: Boost, Boost.Python, CMake and X11/XQuartx. If you doesn't have them, you can [read this article](https://www.pyimagesearch.com/2017/03/27/how-to-install-dlib/) to know how to easily install them.


### For Anaconda install
Install these dependencies (NumPy, OpenCV, Dlib):

```shell
conda env create --file environment.yml
#After creating environment, activate it
conda activate GazeTracking
```


### Verify Installation

Run the demo:

```shell
python example.py
```

## Simple Demo

```python
import cv2
from gaze_tracking import GazeTracking

gaze = GazeTracking()
webcam = cv2.VideoCapture(0)

while True:
    _, frame = webcam.read()
    gaze.refresh(frame)

    new_frame = gaze.annotated_frame()
    text = ""

    if gaze.is_right():
        text = "Looking right"
    elif gaze.is_left():
        text = "Looking left"
    elif gaze.is_center():
        text = "Looking center"

    cv2.putText(new_frame, text, (60, 60), cv2.FONT_HERSHEY_DUPLEX, 2, (255, 0, 0), 2)
    cv2.imshow("Demo", new_frame)

    if cv2.waitKey(1) == 27:
        break
```

## Documentation

In the following examples, `gaze` refers to an instance of the `GazeTracking` class.

### Refresh the frame

```python
gaze.refresh(frame)
```

Pass the frame to analyze (numpy.ndarray). If you want to work with a video stream, you need to put this instruction in a loop, like the example above.

### Position of the left pupil

```python
gaze.pupil_left_coords()
```

Returns the coordinates (x,y) of the left pupil.

### Position of the right pupil

```python
gaze.pupil_right_coords()
```

Returns the coordinates (x,y) of the right pupil.

### Looking to the left

```python
gaze.is_left()
```

Returns `True` if the user is looking to the left.

### Looking to the right

```python
gaze.is_right()
```

Returns `True` if the user is looking to the right.

### Looking at the center

```python
gaze.is_center()
```

Returns `True` if the user is looking at the center.

### Horizontal direction of the gaze

```python
ratio = gaze.horizontal_ratio()
```

Returns a number between 0.0 and 1.0 that indicates the horizontal direction of the gaze. The extreme right is 0.0, the center is 0.5 and the extreme left is 1.0.

### Vertical direction of the gaze

```python
ratio = gaze.vertical_ratio()
```

Returns a number between 0.0 and 1.0 that indicates the vertical direction of the gaze. The extreme top is 0.0, the center is 0.5 and the extreme bottom is 1.0.

### Blinking

```python
gaze.is_blinking()
```

Returns `True` if the user's eyes are closed.

### Webcam frame

```python
frame = gaze.annotated_frame()
```

Returns the main frame with pupils highlighted.

## Usage

Run Main.py to start the program.
When the program starts, a faint black Eye icon appears near the top of the screen. 
Click it to bring the program into focus and press 'q' to start Gaze Tracking. 
The icon stays opaque if it can detect a user otherwise it fades out. 
Place the cursor where You'd like to the program to scroll for you (For example:on a webpage) and the program will scroll for you by detecting your gaze. 
To exit, click on the Eye icon again to bring it to focus and press q again to exit the program. 

## Important
For best accuracy , Have your head be on the same level as your screen.
If Accuracy issues persists, calibrate the conditional values in Main.py according to your liking:

```if type(br)==float:
        root.attributes("-alpha",1.0)
        if br > 3.73:                       #Keep changing 3.73 by 0.1 to adjust at scrolling down sensitivity 
            mouse.wheel(-2)
        elif br < 3.17:                     #Keep changing 3.17 by 0.1 to adjust at scrolling up sensitivity
            mouse.wheel(2)
```
Front Camera Viewport window has been disabled (commented out) in the function run().
To enable simply remove the comment tag from:

``` 
#cv2.imshow("Demo", frame)
```

To

``` 
cv2.imshow("Demo", frame)
```


## You want to help?

Your suggestions, bugs reports and pull requests are welcome and appreciated. You can also starring ⭐️ the project!

If the detection of your pupils is not completely optimal, you can send me a video sample of you looking in different directions. I would use it to improve the algorithm.

## Licensing

This project is released by Antoine Lamé under the terms of the MIT Open Source License. View LICENSE for more information.


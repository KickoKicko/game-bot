import mss
import numpy as np
import cv2
import time
from pathlib import Path

with mss.mss() as sct:
    monitor = sct.monitors[1]  # full screen
    #frame = np.array(screenshot)
    #frame = cv2.cvtColor(frame, cv2.COLOR_BGRA2BGR)
    #sct.save(1,"testt", self)
    #filename = sct.save()
    #print(next(filename))
    #print(next(filename))
    BASE_DIR = Path(__file__).resolve().parent
    SCREENSHOT_DIR = BASE_DIR / "Screenshots"
    SCREENSHOT_DIR.mkdir(exist_ok=True)


    for i in range(30):
        screenshot = sct.grab(monitor)
        filename = SCREENSHOT_DIR / f"screenshot_{i+1}.png"
        mss.tools.to_png(screenshot.rgb, screenshot.size, output=filename)
        frame = np.array(screenshot)
        frame = cv2.cvtColor(frame, cv2.COLOR_BGRA2BGR)
        print(f"Saved {filename}")
        time.sleep(1)
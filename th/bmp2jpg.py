import os, sys
import Image
import time
import threading
from random import randint

Image.open(filename).save(name+"/"+filename[:-4]+".jpg")
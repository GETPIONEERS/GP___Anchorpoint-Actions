from typing_extensions import Self
from datetime import date
import os
import anchorpoint as ap


apc = ap.Context.instance() # setup anchorpoint context
ui = ap.UI() # setup UI

date = date.today()
parentDirectory = apc.path
directoryToCreate = parentDirectory + "/" + str(date)

mode = 0o666
exist_ok = True
os.makedirs(directoryToCreate, mode, exist_ok)
print("Directory " + directoryToCreate + " created")

ui.show_info("Folder successfully created.", "", 2500)
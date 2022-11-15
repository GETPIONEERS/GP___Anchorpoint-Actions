from typing_extensions import Self
import os
import pathlib
import string
import anchorpoint
import apsync

apc = anchorpoint.Context.instance() # setup anchorpoint context
ui = anchorpoint.UI() # setup UI

projectPath = str(pathlib.Path(apc.project_path))
folderPath = apc.folder
filePath = apc.path
fileName = apc.filename.rstrip(string.digits).rstrip("-,.")
# fileNameNew = str.replace(filePath, ".mov", ".mp4")

# --------------------------------------
# UI Buttons, Dropdowns, etc. functions
# --------------------------------------
def button_test(value):
    pass

def dropdown_quality(dialog, value):
    dialog.hide_row("input_customQuality", value != "Custom")
    dialog.hide_row("info_quality_crf", value != "Custom")
    dialog.hide_row("info_quality", value == "Custom")
    check_button_encode()

def input_customQuality(dialog):
    pass

def switch_resolution(dialog, value):
    dialog.hide_row("dropdown_resolution", value == True)
    check_button_encode()

def dropdown_resolution(dialog, value):
    check_button_encode()

# function for enablding / disabling encode button
def check_button_encode():
    if (dialog.get_value("dropdown_quality")) != "Select Quality": # is quality set
        if (dialog.get_value("switch_resolution")) == True: # is switch enabled
            dialog.set_enabled("button_encode", True)
        elif (dialog.get_value("dropdown_resolution")) != "Select Resolution": # is resolution set
            dialog.set_enabled("button_encode", True)
        else:
            dialog.set_enabled("button_encode", False)

# ----------------------
# Function for encoding
# ----------------------
def button_encode(dialog):
    # get all relevant values from the interface
    quality = dialog.get_value("dropdown_quality")
    customQuality = dialog.get_value("input_customQuality")
    resolution = dialog.get_value("dropdown_resolution")

    # set up encoding quality
    encodingQuality = None
    if quality != "Custom":
        if quality == "Very High":
            encodingQuality = 17
        elif quality == "High":
            encodingQuality = 20
        elif quality == "Medium":
            encodingQuality = 25
        elif quality == "Low":
            encodingQuality = 35
    else:
        encodingQuality = customQuality
    
    print("encodingQuality:", encodingQuality)
    print("fileName:", fileName)
    print("folderPath: ", folderPath)
    print("filePath:", filePath)

    outputPath = folderPath + "/" + fileName + "_QuickEncode" + ".mp4"

    print("outputPath:", outputPath)
    
    # encode video
    os.system("ffmpeg -i " + filePath + " -c:v libx264 -crf " + str(encodingQuality) + " -preset medium -b:v 0 " + outputPath)

    dialog.close()
    ui.show_info("Video is being encoded...", "", 2500)

# ---------------------------------
# Function for closing the dialoge
# ---------------------------------
def button_close(dialog: anchorpoint.Dialog):
    dialog.close()

# --------------
# Dialog Window 
# --------------

dropdownQualityValues = ["Very High", "High", "Medium", "Low", "Custom"]
dropdownResolutionValues = ["75%", "50%", "25%"]

dialog = anchorpoint.Dialog()

dialog.title ="Quick Encode Video"
dialog.add_text("Quality: ").add_dropdown("Select Quality", dropdownQualityValues, callback = dropdown_quality, var = "dropdown_quality")
dialog.add_text("Custom CRF:").add_input("30", callback = input_crf, var = "input_customQuality")
dialog.add_info("Default Quality settings are set with CRF values as follows:<br>Very High: 17 | High: 20 | Medium: 25 | Low: 35", var = "info_quality")
dialog.add_info("The range of the CRF scale is 0-51, where 0 is lossless.<br>Sane values are 17-28. ~17 is visually nearly lossless.", var = "info_quality_crf")
dialog.add_switch(True, callback = switch_resolution, var = "switch_resolution").add_text("Keep Resolution")
dialog.add_text("Resolution: ").add_dropdown("Select Resolution", dropdownResolutionValues, callback = dropdown_resolution, var = "dropdown_resolution")
dialog.add_button("Encode", callback = button_encode, var = "button_encode", enabled = False)
# dialog.add_button("TEST", callback = button_test)

dialog.show()
dialog.hide_row("input_customQuality")
dialog.hide_row("info_quality_crf")
dialog.hide_row("dropdown_resolution")



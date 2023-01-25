import anchorpoint as ap
import apsync as aps
from sys import platform
import subprocess
import random
import string
import os

ui = ap.UI()
ctx = ap.Context.instance()

def create_random_text():
    ran = "".join(random.choices(string.ascii_uppercase + string.digits, k=10))    
    return str(ran)

def render_blender(blender_path, selected_files, yaml_dir):
    
    # show progress
    progress = ap.Progress("Blender Preview", "Rendering Images", infinite = True, cancelable = len(selected_files) > 1)

    for file in selected_files:
        output = (file[:file.rfind(".")])
        
        # delete old files if they exist
        os.remove((file[:file.rfind(".")]) + ".jpg")

        if progress.canceled:
            for file in ctx.selected_files:
                ui.finish_busy(file)
            return

        subprocess.run(
            [
                blender_path,
                "-b", file,
                "-E", "BLENDER_EEVEE",
                "-F", "JPEG",
                "-P", f"{yaml_dir}/make_blender_preview_eevee_settings.py",
                "-o", f"{output}#",
                "-f", "0",
            ]
        )

    # rename files after render due to blender command line always inserting frame number into the file name
    for file in selected_files:
        os.rename((file[:file.rfind(".")]) + "0" + ".jpg", (file[:file.rfind(".")]) + ".jpg")

    ui.show_success("Renders Successful")

# First, check if the tool can be found on the machine
if "blender" in ctx.inputs:
    blender_path = ctx.inputs["blender"]

    if blender_path.lower().endswith("blender.app"):
        blender_path = os.path.join(blender_path, "Contents/MacOS/Blender")

    if ap.check_application(blender_path, f"Path to Blender is not correct, please try again", "blender"):
        # Tell the UI that these files are being processed
        for file in ctx.selected_files:
            ui.show_busy(file)
        
        # Render the thumbnail
        # We don't want to block the Anchorpoint UI, hence we run on a background thread
        ctx.run_async(render_blender, blender_path, ctx.selected_files, ctx.yaml_dir)
    else:
        # Remove the path to blender from the action settings so that the user must provide it again
        settings = aps.Settings()
        if settings:
            settings.remove("blender")
            settings.store()
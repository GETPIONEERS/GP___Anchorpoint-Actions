# GETPIONEERS Anchorpoint Actions

## General Information

Anchorpoint API / Documentation: _https://docs.anchorpoint.app_

List of icons: _./icons_

## List of Scripts

#### create_folder_custom

Creates folder with custom name like the current date, current date and time, ...

#### create_folder_template

Creates default GETPIONEERS project folders

#### make_blender_preview

Creates a seperate preview jpeg (not a thumbnail) from a \*.blend file

#### quick_encode_video

Re-encodes videos for preview purposes or other uses

#### mount_cloud_drive_marketing

Mounts the Marketing Cloud Drive Bucket

#### mount_cloud_drive_hr

Mounts the HR Cloud Drive Bucket

#### mount_cloud_drive_accounting

Mounts the Accounting Cloud Drive Bucket

## Q&A between GETPIONEERS and Anchorpoint

#### Discord 1

a few words on distributing actions via git:

1. We currently only support Github public repositories. The branch name does not matter

2. The menu only shows packaged actions. A package of actions is just another yaml file that describes and bundles multiple actions into one user facing package. "Loose" actions will still work, they will still show up in your context menus etc. Have a look at our documentation how to create your own package: https://docs.anchorpoint.app/docs/5-Actions/packages/packages/

3. if you want to debug your installed actions, Anchorpoint installs them to: C:/Users/YOUR_USER/Documents/Anchorpoint/actions/SOME_ID
   Action Packages
   You can package a set of actions in an action package. Action packages have 2 main advantages: They can be distributed using the Action Distribution System, They can be enabled and disabled for the...
   Image
   The advantage of packages is that you can easily turn an entire set of actions on and off. If you just want to distribute a set of actions with the team, there is no need to bundle them in a package

#### Discord 2

Q:
Is it currently possible to set folder icons / colors via python action? The only thing remotely related in the documentation that I could find was changing dialog icon and color

A:
Hey, yes it's possible. I recently added this to the python API but did not yet manage to update the documentation.
Check how the git actions do it:

https://github.com/Anchorpoint-Software/ap-actions/blob/b031402ad3580d068e09f49b3ec1037782ee57db/versioncontrol/actions/git_repository_helper.py#L39

The fork from @mel has a nice overview of built-in icons:
https://github.com/melMass/ap-actions/commit/a429e83d0da2727923ad8992126b1a88d53d6036

But you also add a local file if you want
GitHub
feat: 📝 adds the list of builtin icons · melMass/ap-actions@a429e83
GitHub
ap-actions/git_repository_helper.py at b031402ad3580d068e09f49b3ec1...
Actions are extensions of Anchorpoint. This can be pipeline integrations or features that improve the artist&#39;s daily workflow. - ap-actions/git_repository_helper.py at b031402ad3580d068e09f...

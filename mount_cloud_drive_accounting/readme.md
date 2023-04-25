# This is a copy of Anchorpoints native cloud drive integration, but with some modifications. It is used for the Accounting Drive.

- changed the "identification variables" ("rclone_accounting" instead of "rclone" and "AnchorpointCloudMount_accounting" instead of "AnchorpointCloudMount") so that the copy has it's own "save slot" on the anchorpoint backend.
- hardcoded drive letter and skipping the drive letter prompt (mountAccounting.py Line 166)
- disabled auto batch creation for the mounting

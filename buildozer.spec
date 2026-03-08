[app]
# (Required) Title of your application
title = MindHand

# (Required) Package name
package.name = mindhand

# (Required) Package domain (needed for android packaging)
package.domain = org.allen

# (Required) Source code where the main.py lives
source.dir = .

# (Required) Source files to include (let's include everything)
source.include_exts = py,png,jpg,kv,atlas

# (Required) Application version
version = 0.1

# --- CRITICAL: REQUIREMENTS ---
# This is what tells the builder to download Kivy and OpenCV
requirements = python3,kivy==2.3.0,opencv-python,numpy,sdl2,sdl2_image,sdl2_mixer,sdl2_ttf

# (Required) Permissions for the camera
android.permissions = CAMERA, WRITE_EXTERNAL_STORAGE, READ_EXTERNAL_STORAGE

# (Optional) Orientation
orientation = portrait

# (Optional) Android API (33 is standard for 2026)
android.api = 33
android.minapi = 21


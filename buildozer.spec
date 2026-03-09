[app]
# (Required) Title of your application
title = MindHand

# (Required) Package name
package.name = mindhand

# (Required) Package domain
package.domain = org.allen

# (Required) Source code where the main.py lives
source.dir = .

# (Required) Source files to include
source.include_exts = py,png,jpg,kv,atlas

# --- FIX 1: EXCLUSIONS (The OOM Fix) ---
# This stops Buildozer from zipping up the build folders inside the app
source.exclude_dirs = tests, bin, venv, .venv, .buildozer, .git, .mindhand, __pycache__
source.exclude_patterns = license, .DS_Store, *.pyc, *.zip, *.tgz

# (Required) Application version
version = 0.1

# --- FIX 2: REQUIREMENTS ---
# Use 'opencv' instead of 'opencv-python' for the optimized Android recipe
requirements = python3,kivy==2.3.0,opencv,numpy,sdl2,sdl2_image,sdl2_mixer,sdl2_ttf

# (Required) Permissions
android.permissions = CAMERA, WRITE_EXTERNAL_STORAGE, READ_EXTERNAL_STORAGE

# (Optional) Orientation
orientation = portrait

# --- FIX 3: STABLE BUILD TOOLS ---
# Forcing stable versions helps avoid Java/Gradle version conflicts
android.api = 34
android.minapi = 21
android.build_tools_version = 34.0.0

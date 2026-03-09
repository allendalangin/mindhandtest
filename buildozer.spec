[app]
title = MindHand
package.name = mindhand
package.domain = org.allen
source.dir = .
source.include_exts = py,png,jpg,kv,atlas

# This prevents the "Out of Memory" error by ignoring huge build folders
source.exclude_dirs = tests, bin, venv, .venv, .buildozer, .git, .mindhand, __pycache__
source.exclude_patterns = license, .DS_Store, *.pyc, *.zip, *.tgz

version = 0.1

# 'opencv' is the correct recipe name for Kivy-Android builds
requirements = python3,kivy==2.3.0,opencv,numpy,sdl2,sdl2_image,sdl2_mixer,sdl2_ttf

android.permissions = CAMERA, WRITE_EXTERNAL_STORAGE, READ_EXTERNAL_STORAGE
orientation = portrait

# Stable API 34 matches our Java 17 setup perfectly
android.api = 34
android.minapi = 21
android.build_tools_version = 34.0.0




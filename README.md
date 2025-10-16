# openmm-build-wheels

This repository contains the infrastructure for building Python wheels for OpenMM.  To create packages for a new
release, follow these steps.

1. Edit `.github/workflows/BuildWheels.yml`.  Set `GIT_REVISION` to the revision the packages should be built from.
   For prerelease versions set `VERSION_SUFFIX` to the suffix that will be added to the version number, for example
   `beta` or `rc1`.  For releases, it should be an empty string.
2. Create a pull request.  Once all builds are passing, merge it.
3. Packages will be built automatically.  Assuming they succeed, a green checkmark will appear on the repository's main
   page.  Click it, then select any build.  Look in the browser's URL bar and find the long number immediately after the
   word `runs`.  This is the run ID.
4. Download the zipped packages by running the `download.py` script.  Pass the run ID as an argument, for example
   `python download.py 18048086452`.  Rather than downloading them directly, the script asks your default browser to
   download them.  This is to avoid needing to create and manage Github access tokens.  As long as you are logged into
   Github, your browser will be able to download them.  They will be placed in your default download directory.
5. Move the files to the `unpack` directory.  `cd` into it, then run `python unpack.py`.  This creates a directory
   called `wheels`, extracts all the wheels from the zip files, and places them into it.
6. Upload the packages with `twine upload wheels/*`.

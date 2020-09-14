:: Script for Windows to publish the package to Pypi
:: Made by August (https://augu.dev)

:: Set the path to the current directory
set current=%cd%

echo Now publishing...

:: Check if Python is installed
python --version
if errorlevel 1 goto notInstalled

:: Python is installed, we do the publishing process
if exist %current%\azurlane.egg-info rmdir %current%\azurlane.egg-info /q /s 
if exist %current%\dist rmdir %current%\dist /q /s
echo Creating dist and egginfo directories...
python setup.py sdist

:: Now we check if `twine` is installed
python -c "import twine"
if errorlevel 1 goto twineNotInstalled

:: Now we actually publish!
echo Now uploading!
twine upload ../dist/*

:: Were done with the script, so we won't execute the `notInstalled` section
goto:eof

:: Well, we reached a "notInstalled" state, might as well tell the user!
:notInstalled
echo Error^: Python is not installed on your machine!

:: Well, `twine` is not installed, now we install it using pip!
:twineNotInstalled
echo Warning^: Twine was not installed with pip! Installing...
pip install twine
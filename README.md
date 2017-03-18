# Robot-test-software
Recoded with python from matlab algrithm

platform: windows 10+anaconda+eric6

Calibration algrithm and parts of ISO 9283 

Work for RPRRRR structure ,Two function right now with simple GUI,need numpy,pyqt4 previously before run it.

Tips

You can use pyinstaller to wrap it which will make it run on other platform without python.

When I use pyinstaller and run the .exe file ,it warn 'cannot find windows plague blabla..',

so the solution is do not use -F code and copy  '\Lib\site-packages\PyQt4\plugins\platform' file to generated file '\qt4_plugins'.

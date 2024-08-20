@echo off
setlocal

set "SCRIPT_DIR=%~dp0"
set "EXE_PATH=%SCRIPT_DIR%infiltr8_server.exe"

set "STARTUP_FOLDER=%APPDATA%\Microsoft\Windows\Start Menu\Programs\Startup"

set "SHORTCUT_PATH=%STARTUP_FOLDER%\infiltr8_server.lnk"
powershell "$s=(New-Object -COM WScript.Shell).CreateShortcut('%SHORTCUT_PATH%');$s.TargetPath='%EXE_PATH%';$s.WorkingDirectory='%SCRIPT_DIR%';$s.Save()"

endlocal

start infiltr8_v8.exe
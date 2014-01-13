@echo off 
rmdir build /s /q
pause
setup_cxfreeze.py build

@echo 接下來要壓縮亂數程式
pause
cd build\exe.win43-2.7
"C:\Program Files\7-Zip\7z.exe" a -tzip ..\loosen.zip *
@echo 接下來要製作安裝檔案

@echo
rem "C:\Program Files (x86)\Inno Setup 5\Compil32.exe" /cc "C:\Users\Aaron\Documents\random_choice_portable_Ramdisk.iss"

@echo
@echo 接下來要連線到 ftp
pause

rem "C:\Program Files (x86)\FileZilla FTP Client\filezilla.exe" --site="0D99 manager"
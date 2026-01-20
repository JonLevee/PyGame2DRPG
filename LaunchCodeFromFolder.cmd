echo off
setlocal
set currentDir="%CD%
for /F "usebackq tokens=*" %%i in (`where code.cmd`) do set codeExePath=%%~dpi\..
pushd "%codeExePath%"
set codeExe="%CD%\code.exe"
set codeCli="%CD%\resources\app\out\cli.js"
popd

set VSCODE_DEV=
set ELECTRON_RUN_AS_NODE=1
echo start "" %codeExe% %codeCli% %currentDir%
start "" %codeExe% %codeCli% %currentDir%
exit

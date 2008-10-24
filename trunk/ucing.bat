set UC="C:\Python25\pyuic4.bat"
FOR /R %%I IN (*.ui) DO (
    %UC% -o "%%~dpnI.py" "%%I"
)
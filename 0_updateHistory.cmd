call _echo.cmd

echo Updating History...

::cd RSU-135

    set targetFile=History.txt
    set tempFile=~History.txt
    
    :: создание копии во временном файле
    copy %targetFile% %tempFile%
    
    :: создание новой записи в новом файле
    date /t > %targetFile%
    git log --max-count=200 --pretty=format:"    %%s" >> %targetFile%
    echo. >> %targetFile%
    echo. >> %targetFile%

    :: использование временного файла и его удаление
    type %tempFile% >> %targetFile%
    DEL %tempFile%
    
    %targetFile%
    
::cd ..

call _pause.cmd
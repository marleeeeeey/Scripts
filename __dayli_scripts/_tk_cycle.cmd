@echo off

if exist %exist_file% (
    If Exist "%volume%:\" (
        call %tk% /d%volume% %dismount_flags%
    ) Else (
        call %tk% /v %image% /l%volume%  /p%pass% /k%key_file% %mount_flags%
    )
) else (
    If Exist "%volume%:\" (
        call %tk% /d%volume% %dismount_flags%
    ) 
)

::pause

@echo off

call _kill_all_process_not_force.cmd

Set tk="c:\Program Files\TrueCrypt\TrueCrypt.exe"
Set image="h:\_archives\2017-07-31 0002 WRK kub_NO_g"
Set key_file=""
Set exist_file=%tk%
Set volume=g
Set mount_flags=/a /b /q
Set dismount_flags=/a /b /q
Set pass=

call _tk_cycle.cmd

::pause

echo Start Power Off ...
echo %POWER_FLAGS%

call _kill_all_process.cmd
call _ccleaner_auto.cmd
call QKD_vagrant_suspend.cmd
call _tk_dm_all.cmd
call _flash_unmount.cmd
call shutdown %POWER_FLAGS%
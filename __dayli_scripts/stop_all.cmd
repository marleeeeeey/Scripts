@echo off
echo Start Stop All ...

call _kill_all_process.cmd
call QKD_vagrant_suspend.cmd
call _tk_dm_all.cmd
call _flash_unmount.cmd
call _ccleaner_auto.cmd
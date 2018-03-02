:: How to use:
:: remote_copy.cmd source_file dest_folder user pass  

SET source_file=%1
SET dest_folder=%2
SET username=%3
SET password=%4

echo Remote Copy: '%source_file%' to '%dest_folder%'
net use "%dest_folder%" %password% /user:domain\%username%
xcopy "%source_file%" "%dest_folder%" /Y

:: For more information visit:
:: https://stackoverflow.com/questions/14578175/xcopy-with-credentials-on-remote-machine

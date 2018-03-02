SET username=user
SET password=***
SET target_folder=\\WIN7STYULENEV\styulenev_shared
SET target_file=$(TargetPath)

echo Remote Copy: '$(TargetPath)' to '%target_folder%'
net use "%target_folder%" %password% /user:domain\%username%
xcopy "%target_file%" "%target_folder%" /Y

::For more information visit:
::https://stackoverflow.com/questions/14578175/xcopy-with-credentials-on-remote-machine

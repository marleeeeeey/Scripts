@echo off
echo Start Kill All Process ...

TaskkillFlags=""

call Taskkill /IM   chrome.exe                   /F
call Taskkill /IM   openvpn.exe                  %TaskkillFlags%    
call Taskkill /IM   openvpn-gui.exe              %TaskkillFlags%
call Taskkill /IM   utorrent.exe                 %TaskkillFlags%    
call Taskkill /IM   ManicTime.exe                %TaskkillFlags%
call Taskkill /IM   ManicTimeClient.exe          %TaskkillFlags%    
call Taskkill /IM   picpick.exe                  %TaskkillFlags%
call Taskkill /IM   ONENOTE.exe                  %TaskkillFlags%  
call Taskkill /IM   firefox.exe                  %TaskkillFlags%  
call Taskkill /IM   SumatraPDF.exe               %TaskkillFlags%  
call Taskkill /IM   devenv.exe                   %TaskkillFlags%  
call Taskkill /IM   smartgit.exe                 %TaskkillFlags%  
call Taskkill /IM   oCam.exe                     %TaskkillFlags%  
call Taskkill /IM   oCam_Portable.exe            %TaskkillFlags%  
call Taskkill /IM   Archivarius3000.exe          %TaskkillFlags% 
call Taskkill /IM   umbrello.exe                 %TaskkillFlags% 
call Taskkill /IM   notepad++.exe                %TaskkillFlags% 
call Taskkill /IM   AAM Updates Notifier.exe     %TaskkillFlags% 
call Taskkill /IM   Bonus.ScreenshotReader.exe   %TaskkillFlags% 
call Taskkill /IM   Telegram.exe                 %TaskkillFlags% 
call Taskkill /IM   MobaXterm.exe                %TaskkillFlags%

::pause
#include <Constants.au3>
#include <ScreenCapture.au3>

Func takeScreenshot($lbl = "")
	$screenshotsDir = "screenshots"
	DirCreate($screenshotsDir)
	$screenshotName = $screenshotsDir & "\" & curTime() & "_" & $lbl & ".jpg"	
	appendToLog("Taking screenshot " & $screenshotName)	
	$isScreenshotReady = _ScreenCapture_Capture($screenshotName)
	If $isScreenshotReady == True Then
		appendToLog("screenshot saved")
	Else
		appendToLog("WARNING: can't save screenshot " & $screenshotName)
	Endif	
EndFunc

Func curTime()
    return (@YEAR & "_" & @MON & "_" & @MDAY & "_" & @HOUR & "_" & @MIN & "_" & @SEC)
EndFunc

Func appendToLog($msg)      
	$logFilePath = ".\script_log.txt"	
	$hLogFile = FileOpen($logFilePath, $FO_APPEND)
	;If $hLogFile = -1 Then
	;	MsgBox($MB_SYSTEMMODAL, "", "Cannot open log file " & $logFilePath)
	;	Exit
	;EndIf
	FileWriteLine($hLogFile, curTime() & " " & $msg)	
	FileClose($hLogFile)
EndFunc

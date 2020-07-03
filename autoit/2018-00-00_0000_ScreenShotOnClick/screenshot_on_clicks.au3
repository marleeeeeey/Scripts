#include <Constants.au3>
#include <my_shared.au3>
#include <Misc.au3>

appendToLog("Start script 'screenshot_on_clicks.au3'")	

$pauseBetweenChecks = 10

Local $hDLL = DllOpen("user32.dll")

While True
	; 01 - left_mouse_click
    If _IsPressed("01", $hDLL) Then  
        takeScreenshot("left_mouse_click_01press")              
        While _IsPressed("01", $hDLL)
            Sleep($pauseBetweenChecks)
        WEnd
        takeScreenshot("left_mouse_click_02release")
    EndIf
    Sleep($pauseBetweenChecks)
WEnd

DllClose($hDLL)
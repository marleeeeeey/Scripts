@echo off

:: using this varables!
:: INVITE_USER_STRING
:: USER_INPUT_STRING

IF "%INVITE_USER_STRING%"=="" (
    set INVITE_USER_STRING=Please input string
)

Set /P USER_INPUT_STRING=%INVITE_USER_STRING%: || Set USER_INPUT_STRING=Nothing_Inputed

::echo %USER_INPUT_STRING%
::pause

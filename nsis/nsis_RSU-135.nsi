!include "WinMessages.nsh"
!include "MUI2.nsh"
!include "LogicLib.nsh"

!define PATH_TO_OUT            "g:\_back_up\_nsis\"
!define PATH_TO_BIN_FILE       "g:\Programming\_bin\RSU-135\"
!define PATH_TO_INFO           "g:\Programming\Work\RSU-135\"

SetCompressor /SOLID lzma
!define /date MyTIMESTAMP      "%Y-%m-%d_%H%M"
!define /date My_VERSION_TIME  "%Y.%m.%d.%H.%M"
!define MY_VERSION             "2.2"

!define CHEAT_INSTALL_MSG      "cheat_install"
!define CHEAT_INSTALL_CMD      "cheat_install"
!define PRODUCT_NAME           "RSU-135"
!define ACCORD_LNK_NAME        "${PRODUCT_NAME} accord mode"
!define ACCORD_LNK_COMMANDS    "accord accord_ip:0.0.0.0 accord_port:0 ${CHEAT_INSTALL_CMD}"
!define NO_ACCORD_LNK_COMMANDS "${CHEAT_INSTALL_CMD}"
!define PRODUCT_COMMENT        "Программа для имитации ИУС"
!define EXE_NAME               "RSU-135.exe"
!define PRODUCT_VERSION        "${MY_VERSION}.${My_VERSION_TIME}"
!define HISTORY_TXT            "History.txt"
!define PLATFORMS_DIR          "platforms"   
!define PRODUCT_VENDOR         "АО $\"НИИП$\""
!define REG_KEY                "Software\${PRODUCT_VENDOR}\${PRODUCT_NAME}"
!define REG_NAME               "Start Menu Folder"
!define UNINSTALL_NAME         "Uninstall"
!define UNINSTALL_LNK_NAME     "Удаление ${PRODUCT_NAME}"
                               
!define PRODUCT_VERSION_HEX    0x02160527
!define PRODUCT_UID            "{D0AD7F55-947B-456D-9EA3-7E36211D3565}"
!define VCREDIST_UID           "{b55f7208-e02b-4828-ac78-59c73ddf5bc7}"

!define UNINST_ROOT            "HKLM"
!define UNINST_KEY             "Software\Microsoft\Windows\CurrentVersion\Uninstall"
!define PRODUCT_UNINST_ROOT    "${UNINST_ROOT}"
!define PRODUCT_UNINST_KEY     "${UNINST_KEY}\${PRODUCT_UID}"
!define VCREDIST_UNINST_ROOT   "${UNINST_ROOT}"
!define VCREDIST_UNINST_KEY    "${UNINST_KEY}\${VCREDIST_UID}"

!define MUI_ABORTWARNING
!define MUI_HEADERIMAGE
!define MUI_HEADERIMAGE_BITMAP                  "${NSISDIR}\Contrib\Graphics\Header\orange.bmp"
!define MUI_ICON                                "${NSISDIR}\Contrib\Graphics\Icons\orange-install.ico"
!define MUI_UNICON                              "${NSISDIR}\Contrib\Graphics\Icons\orange-uninstall.ico"
!define MUI_WELCOMEFINISHPAGE_BITMAP            "${NSISDIR}\Contrib\Graphics\Wizard\orange.bmp"
!define MUI_UNWELCOMEFINISHPAGE_BITMAP          "${NSISDIR}\Contrib\Graphics\Wizard\orange.bmp"
!define MUI_STARTMENUPAGE_REGISTRY_ROOT         "HKLM"
!define MUI_STARTMENUPAGE_REGISTRY_KEY          "Software\${PRODUCT_NAME}"
!define MUI_STARTMENUPAGE_REGISTRY_VALUENAME    "Start Menu Folder"
!define MUI_COMPONENTSPAGE_NODESC    
!define MUI_FINISHPAGE_RUN                      "$INSTDIR\${EXE_NAME}"
!define MUI_FINISHPAGE_RUN_NOTCHECKED 
!define MUI_FINISHPAGE_SHOWREADME               "$INSTDIR\${HISTORY_TXT}"
!define MUI_FINISHPAGE_SHOWREADME_NOTCHECKED         


Name                "${PRODUCT_NAME}"
Caption             "${PRODUCT_NAME} ${PRODUCT_VERSION}" 
OutFile             "${PATH_TO_OUT}${MyTIMESTAMP} ${PRODUCT_NAME}_install(${CHEAT_INSTALL_MSG}).exe"
InstallDir          "$PROGRAMFILES\${PRODUCT_NAME}"
VIProductVersion    "${PRODUCT_VERSION}"  
BrandingText        "${PRODUCT_VENDOR}"
ShowInstDetails     show        ;показывать детали установки программы
SilentInstall       normal
SilentUnInstall     normal


Var StartMenuFolder
Var IsVCRedistInstalled
Var ProductInstalledVersion
Var ProductInstalledVersionHex
Var ProductInstalledUninstStr
Var OnInitWarnStr

!insertmacro MUI_PAGE_WELCOME    
!insertmacro MUI_PAGE_COMPONENTS  
!insertmacro MUI_PAGE_DIRECTORY         
!insertmacro MUI_PAGE_STARTMENU Application $StartMenuFolder      
!insertmacro MUI_PAGE_INSTFILES
!insertmacro MUI_PAGE_FINISH
!insertmacro MUI_UNPAGE_CONFIRM
!insertmacro MUI_UNPAGE_INSTFILES
!insertmacro MUI_UNPAGE_FINISH


#--------------------------------------------------------------------------------
!define MUI_CUSTOMFUNCTION_GUIINIT myGuiInit

Function myGuiInit
    ReadRegDWORD $ProductInstalledVersionHex ${PRODUCT_UNINST_ROOT} "${PRODUCT_UNINST_KEY}" "Version"
    ReadRegStr $ProductInstalledVersion ${PRODUCT_UNINST_ROOT} "${PRODUCT_UNINST_KEY}" "DisplayVersion"

    ${If} $ProductInstalledVersionHex = ${PRODUCT_VERSION_HEX}
        StrCpy $OnInitWarnStr "${PRODUCT_NAME} версии $ProductInstalledVersion уже установлена\
                               на этом компьютере. Продолжить установку?"
    ${ElseIf} $ProductInstalledVersionHex > ${PRODUCT_VERSION_HEX}
        StrCpy $OnInitWarnStr "${PRODUCT_NAME} более поздней версии ($ProductInstalledVersion)\
                               уже установлена на этом компьютере. Продолжить установку?"
    ${else}
        Goto RmInstalled
    ${EndIf}

    MessageBox MB_YESNO $OnInitWarnStr /SD IDYES IDNO AbortInstallation
        Goto RmInstalled
AbortInstallation:
        Abort

RmInstalled:

FunctionEnd
#--------------------------------------------------------------------------------

!insertmacro MUI_LANGUAGE "Russian"


Section "${PRODUCT_NAME} v${PRODUCT_VERSION}" secRSU135
        
    SectionIn RO    ; галочка не снимается    
    SetShellVarContext all  ;для всех пользователей в системе
    
    
    ReadRegStr $ProductInstalledUninstStr ${PRODUCT_UNINST_ROOT} "${PRODUCT_UNINST_KEY}" "UninstallString"
    StrCmp $ProductInstalledUninstStr "" ContinueInstallation
    DetailPrint "Удаление установленной версии программы"
    ExecWait "$ProductInstalledUninstStr /S"

  ContinueInstallation:

    ReadRegDWORD $IsVCRedistInstalled ${VCREDIST_UNINST_ROOT} "${VCREDIST_UNINST_KEY}" "Installed"
    ${if} $IsVCRedistInstalled = 0
        SetOutPath $TEMP\${PRODUCT_NAME}
        File "${PATH_TO_BIN_FILE}vcredist_x86.exe"
        DetailPrint "Установка Visual Studio 2013 redistributable package"
        ExecWait "$TEMP\${PRODUCT_NAME}\vcredist_x86.exe"
        Delete "$TEMP\${PRODUCT_NAME}\vcredist_x86.exe"
    ${EndIf}    
    
    SetOutPath  "$INSTDIR"                          
    FILE        "${PATH_TO_BIN_FILE}*.*"  
    FILE        "${PATH_TO_INFO}\${HISTORY_TXT}"            
    SetOutPath  "$INSTDIR\${PLATFORMS_DIR}"   
    FILE        "${PATH_TO_BIN_FILE}${PLATFORMS_DIR}\*.*"       
    SetOutPath  "$INSTDIR"       
       
    WriteUninstaller "$INSTDIR\${UNINSTALL_NAME}.exe"
    
    ExecWait "$INSTDIR\${EXE_NAME} pwoz2912"
    
    !insertmacro MUI_STARTMENU_WRITE_BEGIN Application    
        CreateDirectory "$SMPROGRAMS\$StartMenuFolder"
        CreateShortcut  "$SMPROGRAMS\$StartMenuFolder\${UNINSTALL_LNK_NAME}.lnk" "$INSTDIR\${UNINSTALL_NAME}.exe"      
        CreateShortcut  "$SMPROGRAMS\$StartMenuFolder\${PRODUCT_NAME}.lnk" "$INSTDIR\${EXE_NAME}" "${NO_ACCORD_LNK_COMMANDS}" 
        CreateShortcut  "$SMPROGRAMS\$StartMenuFolder\${ACCORD_LNK_NAME}.lnk" "$INSTDIR\${EXE_NAME}" "${ACCORD_LNK_COMMANDS}"        
    !insertmacro MUI_STARTMENU_WRITE_END    
    
    CreateShortcut "$SMPROGRAMS\$StartMenuFolder\${PRODUCT_NAME}.lnk" "$INSTDIR\${EXE_NAME}" "${NO_ACCORD_LNK_COMMANDS}" 
    CreateShortcut "$SMPROGRAMS\$StartMenuFolder\${ACCORD_LNK_NAME}.lnk" "$INSTDIR\${EXE_NAME}" "${ACCORD_LNK_COMMANDS}" 
    
    WriteRegStr   ${PRODUCT_UNINST_ROOT} "${PRODUCT_UNINST_KEY}" "DisplayName"     "${PRODUCT_NAME}"
    WriteRegStr   ${PRODUCT_UNINST_ROOT} "${PRODUCT_UNINST_KEY}" "DisplayIcon"     "$INSTDIR\${EXE_NAME}"
    WriteRegStr   ${PRODUCT_UNINST_ROOT} "${PRODUCT_UNINST_KEY}" "UninstallString" "$INSTDIR\${UNINSTALL_NAME}.exe"
    WriteRegStr   ${PRODUCT_UNINST_ROOT} "${PRODUCT_UNINST_KEY}" "DisplayVersion"  "${PRODUCT_VERSION}"
    WriteRegStr   ${PRODUCT_UNINST_ROOT} "${PRODUCT_UNINST_KEY}" "Publisher"       "${PRODUCT_VENDOR}"
    WriteRegStr   ${PRODUCT_UNINST_ROOT} "${PRODUCT_UNINST_KEY}" "Comments"        "${PRODUCT_COMMENT}"
    WriteRegDWORD ${PRODUCT_UNINST_ROOT} "${PRODUCT_UNINST_KEY}" "Version"         ${PRODUCT_VERSION_HEX}
    
SectionEnd


# Section "Autoplay ${PRODUCT_NAME}" secAutoplay
# 
#     CreateShortcut "$SMSTARTUP\${PRODUCT_NAME}.lnk" "$INSTDIR\${EXE_NAME}"        
# 
# SectionEnd    
    
Section "Uninstall"  
    
    SetShellVarContext all  ;для всех пользователей в системе
    !insertmacro MUI_STARTMENU_GETFOLDER Application $StartMenuFolder
    
    Delete "$INSTDIR\*.*"
    Delete "$INSTDIR\${PLATFORMS_DIR}\*.*"    
    RMDir "$INSTDIR\${PLATFORMS_DIR}"
    RMDir "$INSTDIR"  
    
    Delete "$SMPROGRAMS\$StartMenuFolder\${UNINSTALL_LNK_NAME}.lnk"
    Delete "$SMPROGRAMS\$StartMenuFolder\${PRODUCT_NAME}.lnk"
    Delete "$SMPROGRAMS\$StartMenuFolder\${ACCORD_LNK_NAME}.lnk"
    RMDir  "$SMPROGRAMS\$StartMenuFolder"
    
    Delete "$DESKTOP\${PRODUCT_NAME}.lnk"
    Delete "$DESKTOP\${ACCORD_LNK_NAME}.lnk"
#    Delete "$SMSTARTUP\${PRODUCT_NAME}.lnk" 
    
    RMDir /r "$TEMP\${PRODUCT_NAME}"
    
    DeleteRegKey ${PRODUCT_UNINST_ROOT} "${PRODUCT_UNINST_KEY}"
    
SectionEnd


#include "ServerApplication.h"
#include "ServerGraphicSystem.h"
#include "ServerCore.h"
#include "StdPlus/StdPlus.h"
#include "QtPlus/QtPlus.h"

ServerApplication::ServerApplication(int argc, char ** argv) 
    : QApplication(argc, argv)
{
    qtplus::qtConsoleOn();  // must be before all prints
    
    m_core = new ServerCore();
    m_gui = new ServerGraphicSystem();

    // TODO init. Read settings...

    m_core->start();

    m_timerId = startTimer(0);
}

ServerApplication::~ServerApplication()
{
    if (m_timerId) killTimer(m_timerId);

    delete m_gui;
    delete m_core;
}

void ServerApplication::timerEvent(QTimerEvent *event)
{
    ServerSettings serverSettings = m_gui->getSettings();

    m_core->setSettings(serverSettings);

    ServerActivity serverActivity = m_core->getActivity();

    m_gui->setActivity(serverActivity);    
}

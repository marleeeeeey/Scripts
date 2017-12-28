#include "ServerGraphicSystem.h"
#include "ServerMainWindow.h"


ServerGraphicSystem::ServerGraphicSystem()
{
    m_mainWindow = new ServerMainWindow(nullptr);
    m_mainWindow->show();
}

ServerGraphicSystem::~ServerGraphicSystem()
{
    delete m_mainWindow;
}

ServerSettings ServerGraphicSystem::getSettings() const
{
    // TODO
    return ServerSettings();
}

void ServerGraphicSystem::setSettings(const ServerSettings & val)
{

}

void ServerGraphicSystem::setActivity(const ServerActivity & val)
{
    m_mainWindow->setActivity(val);
}

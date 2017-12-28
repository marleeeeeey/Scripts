#pragma once

#include "ServerSettings.h"
#include "ServerActivity.h"

class ServerMainWindow;
class ServerActivity;
class ServerSettings;

class ServerGraphicSystem
{
public:
    ServerGraphicSystem();
    ~ServerGraphicSystem();

    ServerSettings getSettings() const;
    void setSettings(const ServerSettings & val);

    void setActivity(const ServerActivity & val);

private:
    ServerMainWindow * m_mainWindow = nullptr;
};


#pragma once

#include <QObject>
#include "ServerSettings.h"
#include "ServerActivity.h"

class ServerCore : QObject
{
    Q_OBJECT

public:
    ServerCore();
    ~ServerCore();

    void start();
    void stop();
    
    ServerSettings getSettings() const;
    void setSettings(ServerSettings val);

    ServerActivity getActivity() const;

protected:
    virtual void timerEvent(QTimerEvent *event) override;

private:

    int            m_timerId = 0;
    ServerSettings m_settings;
    ServerActivity m_activity;
};


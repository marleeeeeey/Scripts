#pragma once

#include <QtWidgets/QMainWindow>
#include <map>
#include "ServerActivity.h"


namespace Ui
{
    class ServerMainWindowClass;
}

class ServerActivity;
class QListWidgetItem;

class ServerMainWindow : public QMainWindow
{
    Q_OBJECT

public:
    ServerMainWindow(QWidget *parent = 0);
    ~ServerMainWindow();

    void setActivity(const ServerActivity & val) { m_serverActivity = val; }

protected:
    virtual void timerEvent(QTimerEvent *event) override;

private:

    int m_timerId = 0;
    Ui::ServerMainWindowClass *      m_ui = nullptr;    
    std::map<int, QListWidgetItem *> m_usersItemById;
    ServerActivity                   m_serverActivity;
};


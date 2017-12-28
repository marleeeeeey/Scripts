#pragma once

#include <QtWidgets/QApplication>
#include <iosfwd>   // std::ofstream

class ServerGraphicSystem;
class ServerCore;

class ServerApplication : public QApplication
{
    Q_OBJECT

public:
    ServerApplication(int argc, char ** argv);
    ~ServerApplication();

protected:
    virtual void timerEvent(QTimerEvent *event) override;

private:
    ServerGraphicSystem * m_gui = nullptr;
    ServerCore *          m_core = nullptr;
    int                   m_timerId = 0;
    std::ofstream *       m_logFile = nullptr;

};


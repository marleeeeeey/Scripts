#include "ServerCore.h"
#include "StdPlus/StdPlus.h"



ServerCore::ServerCore()
{

}

ServerCore::~ServerCore()
{
    stop();
}

void ServerCore::start()
{   
    m_timerId = startTimer(0);
}

void ServerCore::stop()
{
    if (m_timerId)
        killTimer(m_timerId);

    m_timerId = 0;
}

ServerSettings ServerCore::getSettings() const
{
    return m_settings;
}

void ServerCore::setSettings(ServerSettings val)
{
    m_settings = val;
}

ServerActivity ServerCore::getActivity() const
{    
    return m_activity;
}

void ServerCore::timerEvent(QTimerEvent *event)
{
    AFUN;

    m_activity.messages = { "msg1", "msg2", "msg3" };

    const static std::vector<std::string> userNames = { "vasya", "petya", "masha", "dasha" };
    
    static int maxSize = 10;

    if (m_activity.users.size() < maxSize)
    {
        int indexNewUser = stdplus::getRandom<int>(0, userNames.size() - 1);
        m_activity.users.emplace_back(userNames.at(indexNewUser));
    }
    else
    {
        m_activity.users.clear();
    }


    static int counter = 0;
    counter++;

    if (counter % 800 == 0)
    {
        maxSize += stdplus::getRandom<int>(-3, 3);
    }
}

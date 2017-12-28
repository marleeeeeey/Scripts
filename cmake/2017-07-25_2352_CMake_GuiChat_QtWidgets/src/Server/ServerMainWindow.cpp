#include "ServerMainWindow.h"
#include "ui_ServerMainWindow.h"
#include "ServerActivity.h"
#include "StdPlus/MacrosPlus.hpp"

ServerMainWindow::ServerMainWindow(QWidget *parent)
    : QMainWindow(parent)
{
    m_ui = new Ui::ServerMainWindowClass();
    m_ui->setupUi(this);

    m_timerId = startTimer(0);
}

ServerMainWindow::~ServerMainWindow()
{
    if (m_timerId)
        killTimer(m_timerId);

    delete m_ui;
}

void ServerMainWindow::timerEvent(QTimerEvent * )
{
    QListWidget * listWidget = m_ui->listWidgetUsers;
    
    std::vector<int> chechedID;

    for (auto & user : m_serverActivity.users)
    {
        QListWidgetItem * userItem = nullptr;

        try
        {
            userItem = m_usersItemById.at(user.id);
        }
        catch (std::out_of_range & )
        {
            QString label = 
                QString::fromStdString(user.name + "(" + stdplus::to_string(user.id) + ")");

            userItem = new QListWidgetItem(label);
            m_usersItemById[user.id] = userItem;
            listWidget->addItem(userItem);
        }        

        chechedID.push_back(user.id);
    }


    std::vector<int> allId;

    for (auto & p : m_usersItemById)
    {
        allId.push_back(p.first);
    }

    std::vector<int> removeId(allId.size());

    std::sort(allId.begin(), allId.end());
    std::sort(chechedID.begin(), chechedID.end());

    auto it = std::set_difference(allId.begin(), allId.end(),
        chechedID.begin(), chechedID.end(), removeId.begin());

    removeId.resize(it - removeId.begin()); 

    for (auto & id : removeId)
    {
        delete m_usersItemById[id];
        m_usersItemById.erase(id);
    }

}

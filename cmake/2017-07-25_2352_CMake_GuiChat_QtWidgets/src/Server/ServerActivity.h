#pragma once

#include "StdPlus/StdInclude.h"

using Msg = std::string;

class User
{
public:
    User(const std::string & in_name)
    {
        static int currentId = 0;
        currentId++;

        id = currentId;
        name = in_name;
    }

    int id;
    std::string name;
};


class ServerActivity
{
public:
    std::vector<User> users;
    std::vector<Msg>  messages;
};


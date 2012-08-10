#include <cetty/log/config/LogConfigParser.h>

#include <cstdlib>
#include <cstring>
#include <cstdio>
#include <fstream>
#include <iostream>
#include <queue>


#include <cetty/log/type.h>

#define CONFIG_MAX_LEN  50

namespace cetty {
namespace log {
namespace config {


std::map<std::string,std::vector<int> >  LogConfigParser::ConfMap;
std::vector<std::string> LogConfigParser::fieldSeq;
bool LogConfigParser::parseConfig(int logType) {
    std::string filename;

    switch (logType) {
    case SYSLOG:
        filename = "syslog.conf";
        break;

    case NGINX:
        filename = "nginx.conf";
        break;

    case VARNISH:
        filename = "varnish.conf";
        break;

    case POI:
        filename = "poi.conf";
        break;

    default:
        printf("logType not found,please check you param!\n");
        return false;
    }

    char data[CONFIG_MAX_LEN];
    char* key;
    std::string keyName;
    char* value;
    std::ifstream ifs;
    ifs.open(filename.c_str(),std::ifstream::in);

    while (ifs.good()&& !ifs.eof() && !ifs.bad() && !ifs.fail()) {
        std::vector<int> vec;
        ifs.getline(data,CONFIG_MAX_LEN);
        key = strtok(data," ");

        if (key != NULL) {
            keyName = key;
            printf("%s\n",key);
            value = strtok(NULL, " ");

            //if not set the map-field
            if (NULL == value) {
                vec.push_back(0);
            }

            while (NULL != value) {
                vec.push_back(atoi(value));
                value = strtok(NULL," ");
            }

            fieldSeq.push_back(keyName);
            ConfMap.insert(std::pair<std::string,std::vector<int> >(keyName,vec));
        }
    }

    //debug begin
    std::map<std::string,std::vector<int> >::iterator iter;
    std::vector<int>::iterator iter2;

    for (iter = ConfMap.begin(); iter != ConfMap.end(); iter++) {
        std::cout<< iter->first;

        for (iter2 = iter->second.begin(); iter2 != iter->second.end(); iter2++) {
            std::cout << " " <<  *iter2;
        }

        std::cout << std::endl;
    }

    //debug end

}

bool LogConfigParser::reParseLogConfig(int type,std::string filename) {
    ConfMap.clear();
    parseConfig(type);
}

}
}
}
#include <cetty/log/config/FilterConfigParser.h>

#include <fstream>
#include <cstring>
#include <cstdio>


#include <cetty/log/type.h>

#define CONFIG_MAX_LEN  20

namespace cetty {
namespace log {
namespace config {
FilterConfigParser* FilterConfigParser::parser = NULL;

FilterConfigParser* FilterConfigParser::getInstance() {
    if (NULL == parser) {
        parser = new FilterConfigParser();
    }

    return parser;
}

bool FilterConfigParser::parseConfig(int logType) {
    std::string filename;

    switch (logType) {
    case SYSLOG:
        filename = "syslogFilter.conf";
        break;

    case NGINX:
        filename = "nginxFilter.conf";
        break;

    case VARNISH:
        filename = "varnishFilter.conf";
        break;

    case POI:
        filename = "poiFilter.conf";
        break;

    default:
        printf("logType not found,please check you param!\n");
        return false;
    }

    char data[CONFIG_MAX_LEN];
    char* key;
    char* value;
    std::ifstream ifs;
    ifs.open(filename.c_str(),std::ifstream::in);

    while (!ifs.bad() && !ifs.fail() && !ifs.eof()) {
        ifs.getline(data,CONFIG_MAX_LEN);
        key = strtok(data," ");

        if (key != NULL) {
            printf("%s\n",key);
            value = strtok(NULL, " ");
            printf("%s\n",value);
        }

        ConfMap[logType].insert(std::pair<std::string,std::string>(key,value));
    }

    return true;
}

bool FilterConfigParser::reParseLogConfig(int type) {
    ConfMap.clear();
    parseConfig(type);
}

}
}
}

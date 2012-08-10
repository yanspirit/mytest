#ifndef __CONFIGPARSER_H__
#define __CONFIGPARSER_H__
/*
 * Copyright (c) 2010-2012 berek yan (berek yan at gmail dot com)
 *
 * Distributed under under the Apache License, version 2.0 (the "License").
 *
 */
#include <string>
#include <map>



namespace cetty {
namespace log {
namespace config {

class FilterConfigParser {
public:
    FilterConfigParser() {}
    ~FilterConfigParser() {}

    static FilterConfigParser* getInstance();
    bool parseConfig(int type);
    bool reParseLogConfig(int type);

    std::map<std::string,std::string>& getNginxConfMap() {
        return ConfMap[2];
    }
    std::map<std::string,std::string>& getVarnishConfMap() {
        return ConfMap[3];
    }
    std::map<std::string,std::string>& getSyslogConfMap() {
        return ConfMap[1];
    }
    std::map<std::string,std::string>& getPOIConfMap() {
        return ConfMap[4];
    }


public:
    static FilterConfigParser*  parser;
private:
    /**
     *to map the unified field to the log-type special field
     *i.e: hostname  3  means that hostname is consistent with the third field of the special log
     *
     *key 1£ºSyslog  2£ºNginx  3£ºvarnish   4; POI
    */
    std::map<int,std::map<std::string,std::string> >ConfMap;


};


}
}
}

#endif //_6ee6f205_e373_4405_b3eb_241b39746268__CONFIGPARSER_H__
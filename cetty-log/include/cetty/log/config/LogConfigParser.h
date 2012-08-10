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
#include <vector>
#include <cetty/log/type.h>

namespace cetty {
namespace log {
namespace config {

class LogConfigParser {
public:
    LogConfigParser() {}
    ~LogConfigParser() {}

    static bool parseConfig(int logType);
    static bool reParseLogConfig(int type,std::string filename);


    /**map<fieldnum,map<fieldName,mapValues> >
      *to map the unified field to the log-type special field
      *i.e: hostname  3  means that hostname is consistent with the third field of the special log
      *
     */
    static std::map<std::string,std::vector<int> > ConfMap;
    static std::vector<std::string>fieldSeq;
};
}
}
}

#endif //__CONFIGPARSER_H__
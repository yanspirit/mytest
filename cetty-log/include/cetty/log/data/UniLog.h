#ifndef __UNILOG_H__
#define __UNILOG_H__


#include <cetty/log/data/LogDetail.h>

#include <string>
#include <map>

namespace cetty {
namespace log {
namespace data {

class UniLog {
public:
    UniLog(){}
    virtual ~UniLog() {}

    std::map<std::string,std::string>& getFieldMap() {
        return fieldMap;
    }


    std::string combineFields();
    //static const std::string getDetailDelimter()
    //{
    //    return detailDelimter;
    //}

    //const std::string getUniDelimter()
    //{
    //    return uniDelimter;
    //}
    static const std::string detailDelimter;
    static const std::string uniDelimter;

private:
    
    //map<fieldName,fieldValue>
    std::map<std::string,std::string>fieldMap;
    typedef std::map<std::string,std::string>::iterator  FieldMapIter;
    //std::string pri;
    ////struct tm  time;
    //std::string time;
    //std::string host;
    //int pid;
    //std::string source;
    //std::string filename;
    //int lineno;
    //LogDetail*  logDetail;
};
}
}
}
#endif //__UNIFIEDLOG_H__

//std::string getPri() {
//    return pri;
//}

//void setPri(std::string pri) {
//    pri = pri;
//}


//std::string getTime() {
//    return time;
//}

//void setTime(std::string pri) {
//    time = time;
//}


//std::string getHost() {
//    return host;
//}

//void setHost(std::string host) {
//    host = host;
//}


//int getPid() {
//    return pid;
//}

//void setPid(int pid) {
//    pid = pid;
//}
//std::string getSource() {
//    return source;
//}

//void setSource(std::string source) {
//    source = source;
//}


//std::string getFilename() {
//    return source;
//}

//void setFilename(std::string filename) {
//    filename = filename;
//}

//int getLineno() {
//    return lineno;
//}

//void setLineno(int lineno) {
//    lineno = lineno;
//}

//LogDetail* getLogDetail() {
//    return logDetail;
//}

//void setLogDetail(LogDetail* logDetail) {
//    logDetail = logDetail;
//}
//typedef boost::function1<std::string,std::string>;

//void setLogDetail(LogDetail* logDetail) {
//    logDetail = logDetail;
//}
//typedef boost::function1<std::string,std::string>;
#ifndef __UNILOG_DECODER_H__
#define __UNILOG_DECODER_H__


#include <string>

#include <cetty/log/data/UniLog.h>

namespace cetty {
namespace log {
namespace codec {
using namespace cetty::log::data;
class  UniLogDecoder {
public:
    virtual ~UniLogDecoder() {}
    int strsplit(const std::string,char delim,std::vector<std::string>* elems);
    int decode(int logType,const std::string& msg,UniLog* log);

};

}
}
}

#endif
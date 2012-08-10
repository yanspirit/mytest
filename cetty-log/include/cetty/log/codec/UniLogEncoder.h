#ifndef __UNILOG_ENCODER_H__
#define __UNILOG_ENCODER_H__

#include <cetty/log/data/UniLog.h>
#include <string>

namespace cetty {
namespace log {
namespace codec {
using namespace cetty::log::data;

class  UniLogEncoder {
public:
    UniLogEncoder() {}
    ~UniLogEncoder() {}

    int encode(UniLog* log,std::string& destMsg);
};

}
}
}
#endif
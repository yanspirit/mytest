#include <cetty/log/codec/UniLogEncoder.h>

namespace cetty {
namespace log {
namespace codec {

using namespace cetty::log::data;

int UniLogEncoder::encode(UniLog* log,std::string& destMsg) {
    destMsg = log->combineFields();
    return 0;
}

}
}
}

#include <cetty/log/codec/UniLogDecoder.h>

#include <vector>
#include <string>
#include <assert.h>

#include <cetty/log/config/LogConfigParser.h>
#include <cetty/util/StringUtil.h>

namespace cetty {
namespace log {
namespace codec {
using namespace cetty::log::data;
using namespace cetty::log::config;
using namespace cetty::util;


int UniLogDecoder::strsplit(const std::string,char delim,std::vector<std::string>* elems)
{
    assert(elems);
    elems->clear();
    std::string::const_iterator it = str.begin();
    std::string::const_iterator pv = it;
    while (it != str.end()) {
        if (*it == delim  && ) {
            boost::algorithm::trim(srcMsg,);
            std::string col(pv, it);
            elems->push_back(col);
            pv = it + 1;
        }
        ++it;
    }
    std::string col(pv, it);
    elems->push_back(col);
    return elems->size();
}



int UniLogDecoder::decode(int logType,const std::string& msg,UniLog* log) {
    std::vector<std::string> srcFields;


    strsplit(msg," ",&srcFields);

    std::map<std::string,std::vector<int> >::iterator iter;

    for (iter = LogConfigParser::ConfMap.begin(); iter != LogConfigParser::ConfMap.end(); iter++) {
        std::vector<int>::iterator vecIter;
        std::string fieldVal;

        for (vecIter = iter->second.begin(); vecIter != iter->second.end(); vecIter++) {
            if (0 == *vecIter) {
                //if there is no field,print '*'
                fieldVal = "*";
                break;
            }
            else if (iter->second.size() == 1) {
                fieldVal.append(srcFields[*vecIter-1]);
            }
            else {
                fieldVal.append(srcFields[*vecIter-1]).append(UniLog::detailDelimter);
            }
        }

        log->getFieldMap().insert(std::pair<std::string,std::string>(iter->first,fieldVal));
    }
}


}
}
}
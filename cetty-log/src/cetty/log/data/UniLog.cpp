#include <cetty/log/data/UniLog.h>
#include <cetty/log/type.h>
#include <cetty/log/config/LogConfigParser.h>


namespace cetty{namespace log{namespace data{

    using namespace cetty::log::config;
    const std::string UniLog::detailDelimter = "|";
    const std::string UniLog::uniDelimter = " ";

    std::string UniLog::combineFields()
    {
        std::string ret;
        std::string keyName;
        FieldMapIter iter;
        for(int i = 0;i < LogConfigParser::fieldSeq.size(); i++)
        {
            keyName = LogConfigParser::fieldSeq[i];
            if((iter = fieldMap.find(keyName)) != fieldMap.end())
            {
                ret.append(iter->second).append(uniDelimter);
            }
        }
        return ret;
    }

} } }


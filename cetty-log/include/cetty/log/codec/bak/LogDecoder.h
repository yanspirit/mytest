#ifndef __LOG_DECODER_H__
#define __LOG_DECODER_H__


#include <string>

namespace cetty{namespace log{namespace codec{
    class  LogDecoder
    {
    public:
        virtual ~LogDecoder(){}

        int decode(std::string msg) = 0;
    };


}}}

#endif
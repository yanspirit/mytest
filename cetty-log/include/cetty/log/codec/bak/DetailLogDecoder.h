#ifndef __DETAIL_LOG_DECODER_H__
#define __DETAIL_LOG_DECODER_H__


#include <string>

namespace cetty{namespace log{namespace codec{
    class  DetailLogDecoder:public LogDecoder
    {
    public:
        virtual ~DetailLogDecoder(){}
        virtual int decode(std::string msg){}
    };


}}}

#endif
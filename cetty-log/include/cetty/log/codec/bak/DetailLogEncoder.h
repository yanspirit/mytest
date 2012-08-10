#ifndef __DETAIL_LOG_ENCODER_H__
#define __DETAIL_LOG_ENCODER_H__

#include <string>

namespace cetty{namespace log{namespace codec{
    class  DetailLogEncoder:public LogEncoder
    {
    public:
        DetailLogEncoder(){}
        virtual ~DetailLogEncoder(){}

        virtual int encode(std::string msg){}
    };

}}}
#endif
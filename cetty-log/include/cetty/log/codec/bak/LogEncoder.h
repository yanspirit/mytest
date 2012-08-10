#ifndef __LOG_ENCODER_H__
#define __LOG_ENCODER_H__

#include <string>

namespace cetty{namespace log{namespace codec{
    class  LogEncoder
    {
    public:
        virtual ~LogEncoder(){}

        int encode(std::string msg) = 0;
    };

}}}
#endif
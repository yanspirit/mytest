#ifndef __NGINXLOG_FILTER_H__
#define __NGINXLOG_FILTER_H__
#include <cetty/log/filter/FieldFilter.h>

class TimeFilter: public FieldFilter
{
public:
    virtual ~TimeFilter(){}

    void logFilter();
};

#endif
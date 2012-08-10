#ifndef __SYSLOG_FILTER_H__
#define __SYSLOG_FILTER_H__

#include <cetty/log/filter/FieldFilter.h>
class HostFilter: public FieldFilter
{
public:
    virtual ~HostFilter(){}

    void logFilter();
};
#endif
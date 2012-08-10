#ifndef __POILOG_FILTER_H__
#define __POILOG_FILTER_H__
#include <cetty/log/filter/FieldFilter.h>

class PriFilter: public FieldFilter
{
public:
    virtual ~PriFilter(){}

    void logFilter();
};

#endif
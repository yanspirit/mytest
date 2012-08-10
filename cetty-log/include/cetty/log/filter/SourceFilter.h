#ifndef __VARNISHLOG_FILTER_H__
#define __VARNISHLOG_FILTER_H__

#include <cetty/log/filter/FieldFilter.h>
class SourceFilter: public FieldFilter
{
public:
    virtual ~SourceFilter(){}

    void logFilter();
};

#endif
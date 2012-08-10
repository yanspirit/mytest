#ifndef __UNILOG_FILTER_H__
#define __UNILOG_FILTER_H__

class FieldFilter
{
public:
    virtual ~FieldFilter(){}

    void logFilter() = 0;
};

#endif
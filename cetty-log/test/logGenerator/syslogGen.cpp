#include <syslog.h>

int main()
{
    openlog("POI", LOG_CONS | LOG_PID, 0);
    int i = 0;
    while(i<5)
    {
        syslog(LOG_INFO,"this is a syslog info");
        syslog(LOG_WARNING,"this is a syslog warn");
        i++;
    }
    closelog();
    return 0;
}
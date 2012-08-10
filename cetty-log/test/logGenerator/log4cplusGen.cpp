#include <log4cplus/logger.h>
#include <log4cplus/fileappender.h>
#include <log4cplus/consoleappender.h>
//#include <conio.h>
#include <iostream>
#include <log4cplus/configurator.h>
#include <log4cplus/loggingmacros.h>

#include <boost/shared_ptr.hpp>
#include <iomanip>


using namespace std;
using namespace log4cplus;
//typedef boost::shared_ptr<RollingFileAppender>  SharedAppenderPtr;



static Logger logger1 = Logger::getInstance(LOG4CPLUS_TEXT("TRACE_MSG"));
static Logger logger2 = Logger::getInstance(LOG4CPLUS_TEXT("log"));


void printDebug(){    
/*    LOG4CPLUS_TRACE(logger, "::printDebug()");    
    LOG4CPLUS_DEBUG(logger, "This is a DEBUG message");    
    LOG4CPLUS_INFO(logger, "This is a INFO message");    
    LOG4CPLUS_WARN(logger, "This is a WARN message");   
    LOG4CPLUS_ERROR(logger, "This is a ERROR message");    
    LOG4CPLUS_FATAL(logger, "This is a FATAL message");
    */

    LOG4CPLUS_TRACE(logger1, "::printDebug()"); 
}


int main()
{
   /* BasicConfigurator config;
    config.configure();*/
    PropertyConfigurator::doConfigure("urconfig.properties");


    Logger root = Logger::getRoot();
    LOG4CPLUS_FATAL(root,"for root msg  all_msg.log!");


    Logger logger1 = Logger::getInstance(LOG4CPLUS_TEXT("TRACE_MSGS"));

    int i = 0;
    while(i<100)
    {
        LOG4CPLUS_TRACE(logger1,"hello-ysp  trace_msg.log");
        i++;
    }
    

/*
    Logger logger = Logger::getInstance("main");
    LOG4CPLUS_WARN(logger, "Hello, World!");*/
    return 0;
}
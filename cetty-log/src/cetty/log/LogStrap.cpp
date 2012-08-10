#include <string>

#include <cetty/log/scribeUtils/common.h>
#include <cetty/log/scribeUtils/scribe_wrapper.h>
#include <cetty/log/scribeUtils/scribe_tail.h>

#include <cetty/log/LogStrap.h>
#include <cetty/log/type.h>
#include <cetty/log/data/UniLog.h>

//#include <cetty/log/config/FilterConfigParser.h>
#include <cetty/log/config/LogConfigParser.h>


namespace cetty {
namespace log {

using namespace cetty::log::config;
using namespace cetty::log::codec;
using namespace cetty::log::data;

void LogStrap::logMain(int argc, char** argv) {
    std::string host;
    unsigned long port;
    unsigned int timeout;
    bool debug;
    std::string log;
    std::string category;
    /*std::string message;*/
    std::string filename;
    int logType;

    try {
        boost::program_options::options_description desc("Usage: scribe_tail [OPTION]");
        desc.add_options()
        ("help", "Print help")
        ("host", boost::program_options::value<std::string>(&host)->default_value("127.0.0.1"), "Scribe hostname")
        ("port", boost::program_options::value<unsigned long>(&port)->default_value(1463), "Scribe port")
        ("timeout", boost::program_options::value<unsigned int>(&timeout)->default_value(30), "timeout")
        ("debug", boost::program_options::value<bool>(&debug)->default_value(false), "Enable debug mode")
        ("log", boost::program_options::value<std::string>(&log)->default_value("/tmp/scribewrapper.log"), "Path to scribe log file")
        ("category", boost::program_options::value<std::string>(&category)->default_value("default"), "Scribe category")
        ("file", boost::program_options::value<std::string>(&filename), "Log file to listen")
        ("type", boost::program_options::value<int>(&logType), "Log file type,syslog=1 nginx=2 varnish=3 poi=4")
        ;
        boost::program_options::variables_map vm;
        boost::program_options::store(boost::program_options::parse_command_line(argc, argv, desc), vm);
        boost::program_options::notify(vm);

        if (vm.count("help")) {
            std::cout << desc << std::endl;
            return;
            //return 1;
        }

        if (!vm.count("file")) {
            std::cout << "Log file to listen is missing" << std::endl;
            std::cout << std::endl << desc << std::endl;
            return;
            //return 1;
        }
    }
    catch (boost::program_options::error& e) {
        std::cerr << e.what() << std::endl;
        return;
        //return 1;
    }

    initConf(logType);
    tailLoop(filename,logType,host, port, timeout, category, debug, log);
}

void LogStrap::tailLoop(const std::string& filename,int logType,const std::string& host,
                        unsigned long port, unsigned int timeout, const std::string& category, bool debug,const std::string& log) {
    std::string srcMsg;
    std::string destMsg;
    scribeTail tail(filename);
    scribeWrapper client(host, port, timeout, category, debug, log);

    tail.open();

    while (tail.getLine(srcMsg)) {
        boost::algorithm::trim(srcMsg);

        if (srcMsg.empty()) {
            continue;
        }

        //at this pointer to add the logic of log-handle
        handleLog(logType,srcMsg,destMsg);

        if (client.send(destMsg) == -1) {
            std::cout << "Error! Please check logs" << std::endl;
            //return 1;
        }
    }
    tail.pop();
    client.close();
}

void LogStrap::initConf(int logType) {
    LogConfigParser::parseConfig(logType);
    //filterConfigParser.parseConfig(logType);
}

void LogStrap::handleLog(int logType,const std::string& srcMsg,std::string& destMsg) {
    UniLog logObj;
    std::string encodedMsg;
    //decoder
    decoder.decode(logType,srcMsg,&logObj);

    //filters


    //encoder
    encoder.encode(&logObj,destMsg);
    //send

}
}
}

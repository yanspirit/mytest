#include <cetty/log/scribeUtils/common.h>
#include <cetty/log/scribeUtils/scribe_wrapper.h>
#include <cetty/log/scribeUtils/scribe_tail.h>


//#include <cetty/log/codec/LogDecoder.h>
//#include <cetty/log/data/UniLog.h>
//#include <cetty/log/LogStrap.h>
//#include <cetty/log/type.h>


using std::string;
using boost::shared_ptr;

//using namespace cetty::log;
//using namespace cetty::log;


scribeTail::scribeTail(const std::string& filename, const int& sleep_var, const int& reopen_count)
    : filename(filename), sleep_var(sleep_var), reopen_count(reopen_count) {
    boost::iostreams::file_source file(filename.c_str(), std::ios::in);
    in.push(file);
    stat(filename.c_str(), &pstat);
    cstat = pstat;
}

void scribeTail::open() {
    boost::iostreams::seek(in, std::ios_base::beg, BOOST_IOS::end);
}

void scribeTail::stillGood() {
    stat(filename.c_str(), &cstat);

    if (cstat.st_ino != pstat.st_ino) {
        in.reset();
        boost::iostreams::file_source file(filename.c_str());
        in.push(file);
    }
    else if (cstat.st_size < pstat.st_size) {
        boost::iostreams::seek(in, 0, BOOST_IOS::beg);
    }
}

bool scribeTail::getLine(std::string& message) {
    while (true) {
        stillGood();
        std::getline(in, message);

        if (in.eof()) {
            in.clear();
        }

        return true;
    }
}

void scribeTail::pop() {
    in.pop();
}


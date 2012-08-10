# Static versions of Cetty libraries.  We build them using more
# strict warnings than what are used for other targets, to ensure that
# cetty can be compiled by a user aggressive about warnings.
AUX_SOURCE_DIRECTORY(cetty/log LOG_DIR)
AUX_SOURCE_DIRECTORY(cetty/log/codec LOG_CODEC_DIR)
AUX_SOURCE_DIRECTORY(cetty/log/data LOG_DATA_DIR)
AUX_SOURCE_DIRECTORY(cetty/log/scribeUtils LOG_SCRIBE_DIR)
AUX_SOURCE_DIRECTORY(cetty/log/config LOG_CONFIG_DIR)
AUX_SOURCE_DIRECTORY(cetty/log/filter LOG_FILTER_DIR)
SET(libsources ${LOG_DIR} ${LOG_CODEC_DIR} ${LOG_DATA_DIR} ${LOG_SCRIBE_DIR}
${LOG_CONFIG_DIR} ${LOG_FILTER_DIR})

SET(LIBRARY_OUTPUT_PATH ${PROJECT_BINARY_DIR}/lib)

add_definitions("-g")
#add_library(log STATIC ${libsources})
include_directories(/usr/include/log /usr/local/include/thrift /usr/local/include/thrift/fb303 /usr/local/boost/include)

add_library(log STATIC ${libsources})

#link_directories(/usr/local/boost/lib /usr/local/lib)

#cxx_static_library(log "${cxx_default}" ${libsources})

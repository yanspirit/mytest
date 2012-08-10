SET(EXECUTABLE_OUTPUT_PATH ${PROJECT_BINARY_DIR}/bin)

#find_package(Protobuf REQUIRED)
#include_directories(${PROTOBUF_INCLUDE_DIRS})
#LINK_DIRECTORIES(${PROTOBUF_LIB_DIRS})

#add_executable(server  "server.cpp" "echo.pb.cc")
#set_target_properties(server PROPERTIES COMPILE_FLAGS "${cxx_default}")
#target_link_libraries(server protobufservice cettyservice cettyconfig cetty ${PROTOBUF_LIBRARIES})

#add_executable(client  "client.cpp" "echo.pb.cc")
#set_target_properties(client PROPERTIES COMPILE_FLAGS "${cxx_default}")
#target_link_libraries(client protobufservice cettyservice cettyconfig cetty ${PROTOBUF_LIBRARIES})
include_directories(/usr/include/log /usr/local/include/thrift /usr/local/include/thrift/fb303 /usr/local/boost/include)
link_directories(/usr/local/boost/lib /usr/local/lib /usr/lib)

add_definitions("-g")
#scribewrapper
SET(SAMPLE_DEPENDENCIES log scribe thrift fb303 pthread cetty boost_program_options boost_iostreams)

add_executable(logTest logTest.cpp)
#cxx_executable_current_path_no_link(logTest)
target_link_libraries(logTest ${SAMPLE_DEPENDENCIES})

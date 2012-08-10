cmake_minimum_required(VERSION 2.6)

ADD_SUBDIRECTORY(src)
option(BUILD_CETTY_LOG_TEST "Build sample programs." ON)
########################################################################
#
# Samples on how to link user tests with gtest or gtest_main.
#
# They are not built by default.  To build them, set the
# build_gtest_samples option to ON.  You can do it by running ccmake
# or specifying the -Dbuild_gtest_samples=ON flag when running cmake.
#option(BUILD_CETTY_REDIS_EXAMPLES "Build example programs." OFF)
if (BUILD_CETTY_LOG_TEST)
	MESSAGE(STATUS "BUILDING SAMPLES...")
	ADD_SUBDIRECTORY(test)
endif()

function(cxx_library_with_type name type cxx_flags)
  # type can be either STATIC or SHARED to denote a static or shared library.
  # ARGN refers to additional arguments after 'cxx_flags'.
  add_library(${name} ${type} ${ARGN})
  set_target_properties(${name}
    PROPERTIES
    COMPILE_FLAGS "${cxx_flags}")
    if (CMAKE_USE_PTHREADS_INIT)
      target_link_libraries(${name} ${CMAKE_THREAD_LIBS_INIT}
${Boost_LIBRARIES})
        elseif (CMAKE_USE_PTHREADS_INIT)
          target_link_libraries(${name} ${Boost_LIBRARIES})
    endif()
endfunction()

function(cxx_static_library name cxx_flags)
  cxx_library_with_type(${name} STATIC "${cxx_flags}" ${ARGN})
endfunction()

function(cxx_shared_library name cxx_flags)
  cxx_library_with_type(${name} SHARED "${cxx_flags}" ${ARGN})
endfunction()

function(cxx_executable_with_flags name cxx_flags lib)
  add_executable(${name} ${ARGN})
  if (cxx_flags)
    set_target_properties(${name}
      PROPERTIES
      COMPILE_FLAGS "${cxx_flags}")
  endif()
  target_link_libraries(${name} ${lib})
endfunction()

function(cxx_executable_with_flags_no_link name cxx_flags)
  add_executable(${name} ${ARGN})
  if (cxx_flags)
    set_target_properties(${name}
      PROPERTIES
      COMPILE_FLAGS "${cxx_flags}")
  endif()
endfunction()

function(cxx_executable name dir lib)
  cxx_executable_with_flags(
    ${name} "${cxx_default}" ${lib} "${dir}/${name}.cpp" ${ARGN})
endfunction()

function(cxx_executable_current_path name lib)
  cxx_executable_with_flags(
    ${name} "${cxx_default}" ${lib} "${name}.cpp" ${ARGN})
endfunction()

function(cxx_executable_current_path_no_link name)
  cxx_executable_with_flags_no_link(
    ${name} "${cxx_default}" "${name}.cpp" ${ARGN})
endfunction()


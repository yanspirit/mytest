# CMAKE generated file: DO NOT EDIT!
# Generated by "Unix Makefiles" Generator, CMake Version 2.6

#=============================================================================
# Special targets provided by cmake.

# Disable implicit rules so canoncical targets will work.
.SUFFIXES:

# Remove some rules from gmake that .SUFFIXES does not remove.
SUFFIXES =

.SUFFIXES: .hpux_make_needs_suffix_list

# Suppress display of executed commands.
$(VERBOSE).SILENT:

# A target that is always out of date.
cmake_force:
.PHONY : cmake_force

#=============================================================================
# Set environment variables for the build.

# The shell in which to execute make rules.
SHELL = /bin/sh

# The CMake executable.
CMAKE_COMMAND = /usr/bin/cmake

# The command to remove a file.
RM = /usr/bin/cmake -E remove -f

# The program to use to edit the cache.
CMAKE_EDIT_COMMAND = /usr/bin/ccmake

# The top-level source directory on which CMake was run.
CMAKE_SOURCE_DIR = /root/opensource/cetty-log

# The top-level build directory on which CMake was run.
CMAKE_BINARY_DIR = /root/opensource/cetty-log/logBuild

# Include any dependencies generated for this target.
include test/CMakeFiles/logTest.dir/depend.make

# Include the progress variables for this target.
include test/CMakeFiles/logTest.dir/progress.make

# Include the compile flags for this target's objects.
include test/CMakeFiles/logTest.dir/flags.make

test/CMakeFiles/logTest.dir/logTest.cpp.o: test/CMakeFiles/logTest.dir/flags.make
test/CMakeFiles/logTest.dir/logTest.cpp.o: ../test/logTest.cpp
	$(CMAKE_COMMAND) -E cmake_progress_report /root/opensource/cetty-log/logBuild/CMakeFiles $(CMAKE_PROGRESS_1)
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Building CXX object test/CMakeFiles/logTest.dir/logTest.cpp.o"
	cd /root/opensource/cetty-log/logBuild/test && /usr/bin/c++   $(CXX_DEFINES) $(CXX_FLAGS) -o CMakeFiles/logTest.dir/logTest.cpp.o -c /root/opensource/cetty-log/test/logTest.cpp

test/CMakeFiles/logTest.dir/logTest.cpp.i: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Preprocessing CXX source to CMakeFiles/logTest.dir/logTest.cpp.i"
	cd /root/opensource/cetty-log/logBuild/test && /usr/bin/c++  $(CXX_DEFINES) $(CXX_FLAGS) -E /root/opensource/cetty-log/test/logTest.cpp > CMakeFiles/logTest.dir/logTest.cpp.i

test/CMakeFiles/logTest.dir/logTest.cpp.s: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Compiling CXX source to assembly CMakeFiles/logTest.dir/logTest.cpp.s"
	cd /root/opensource/cetty-log/logBuild/test && /usr/bin/c++  $(CXX_DEFINES) $(CXX_FLAGS) -S /root/opensource/cetty-log/test/logTest.cpp -o CMakeFiles/logTest.dir/logTest.cpp.s

test/CMakeFiles/logTest.dir/logTest.cpp.o.requires:
.PHONY : test/CMakeFiles/logTest.dir/logTest.cpp.o.requires

test/CMakeFiles/logTest.dir/logTest.cpp.o.provides: test/CMakeFiles/logTest.dir/logTest.cpp.o.requires
	$(MAKE) -f test/CMakeFiles/logTest.dir/build.make test/CMakeFiles/logTest.dir/logTest.cpp.o.provides.build
.PHONY : test/CMakeFiles/logTest.dir/logTest.cpp.o.provides

test/CMakeFiles/logTest.dir/logTest.cpp.o.provides.build: test/CMakeFiles/logTest.dir/logTest.cpp.o
.PHONY : test/CMakeFiles/logTest.dir/logTest.cpp.o.provides.build

# Object files for target logTest
logTest_OBJECTS = \
"CMakeFiles/logTest.dir/logTest.cpp.o"

# External object files for target logTest
logTest_EXTERNAL_OBJECTS =

bin/logTest: test/CMakeFiles/logTest.dir/logTest.cpp.o
bin/logTest: lib/liblog.a
bin/logTest: test/CMakeFiles/logTest.dir/build.make
bin/logTest: test/CMakeFiles/logTest.dir/link.txt
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --red --bold "Linking CXX executable ../bin/logTest"
	cd /root/opensource/cetty-log/logBuild/test && $(CMAKE_COMMAND) -E cmake_link_script CMakeFiles/logTest.dir/link.txt --verbose=$(VERBOSE)

# Rule to build all files generated by this target.
test/CMakeFiles/logTest.dir/build: bin/logTest
.PHONY : test/CMakeFiles/logTest.dir/build

test/CMakeFiles/logTest.dir/requires: test/CMakeFiles/logTest.dir/logTest.cpp.o.requires
.PHONY : test/CMakeFiles/logTest.dir/requires

test/CMakeFiles/logTest.dir/clean:
	cd /root/opensource/cetty-log/logBuild/test && $(CMAKE_COMMAND) -P CMakeFiles/logTest.dir/cmake_clean.cmake
.PHONY : test/CMakeFiles/logTest.dir/clean

test/CMakeFiles/logTest.dir/depend:
	cd /root/opensource/cetty-log/logBuild && $(CMAKE_COMMAND) -E cmake_depends "Unix Makefiles" /root/opensource/cetty-log /root/opensource/cetty-log/test /root/opensource/cetty-log/logBuild /root/opensource/cetty-log/logBuild/test /root/opensource/cetty-log/logBuild/test/CMakeFiles/logTest.dir/DependInfo.cmake --color=$(COLOR)
.PHONY : test/CMakeFiles/logTest.dir/depend


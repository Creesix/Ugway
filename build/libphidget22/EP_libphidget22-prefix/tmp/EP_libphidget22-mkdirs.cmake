# Distributed under the OSI-approved BSD 3-Clause License.  See accompanying
# file Copyright.txt or https://cmake.org/licensing for details.

cmake_minimum_required(VERSION 3.5)

file(MAKE_DIRECTORY
  "/home/remi/ugway_ws/build/libphidget22/libphidget22-src"
  "/home/remi/ugway_ws/build/libphidget22/EP_libphidget22-prefix/src/EP_libphidget22-build"
  "/home/remi/ugway_ws/build/libphidget22/EP_libphidget22-prefix"
  "/home/remi/ugway_ws/build/libphidget22/EP_libphidget22-prefix/tmp"
  "/home/remi/ugway_ws/build/libphidget22/EP_libphidget22-prefix/src/EP_libphidget22-stamp"
  "/home/remi/ugway_ws/build/libphidget22/EP_libphidget22-prefix/src"
  "/home/remi/ugway_ws/build/libphidget22/EP_libphidget22-prefix/src/EP_libphidget22-stamp"
)

set(configSubDirs )
foreach(subDir IN LISTS configSubDirs)
    file(MAKE_DIRECTORY "/home/remi/ugway_ws/build/libphidget22/EP_libphidget22-prefix/src/EP_libphidget22-stamp/${subDir}")
endforeach()
if(cfgdir)
  file(MAKE_DIRECTORY "/home/remi/ugway_ws/build/libphidget22/EP_libphidget22-prefix/src/EP_libphidget22-stamp${cfgdir}") # cfgdir has leading slash
endif()

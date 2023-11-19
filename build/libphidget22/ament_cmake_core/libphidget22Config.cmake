# generated from ament/cmake/core/templates/nameConfig.cmake.in

# prevent multiple inclusion
if(_libphidget22_CONFIG_INCLUDED)
  # ensure to keep the found flag the same
  if(NOT DEFINED libphidget22_FOUND)
    # explicitly set it to FALSE, otherwise CMake will set it to TRUE
    set(libphidget22_FOUND FALSE)
  elseif(NOT libphidget22_FOUND)
    # use separate condition to avoid uninitialized variable warning
    set(libphidget22_FOUND FALSE)
  endif()
  return()
endif()
set(_libphidget22_CONFIG_INCLUDED TRUE)

# output package information
if(NOT libphidget22_FIND_QUIETLY)
  message(STATUS "Found libphidget22: 2.3.1 (${libphidget22_DIR})")
endif()

# warn when using a deprecated package
if(NOT "" STREQUAL "")
  set(_msg "Package 'libphidget22' is deprecated")
  # append custom deprecation text if available
  if(NOT "" STREQUAL "TRUE")
    set(_msg "${_msg} ()")
  endif()
  # optionally quiet the deprecation message
  if(NOT ${libphidget22_DEPRECATED_QUIET})
    message(DEPRECATION "${_msg}")
  endif()
endif()

# flag package as ament-based to distinguish it after being find_package()-ed
set(libphidget22_FOUND_AMENT_PACKAGE TRUE)

# include all config extra files
set(_extras "libphidget22-extras.cmake")
foreach(_extra ${_extras})
  include("${libphidget22_DIR}/${_extra}")
endforeach()

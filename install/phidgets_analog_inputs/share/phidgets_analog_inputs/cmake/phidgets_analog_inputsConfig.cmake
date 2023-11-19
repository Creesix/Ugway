# generated from ament/cmake/core/templates/nameConfig.cmake.in

# prevent multiple inclusion
if(_phidgets_analog_inputs_CONFIG_INCLUDED)
  # ensure to keep the found flag the same
  if(NOT DEFINED phidgets_analog_inputs_FOUND)
    # explicitly set it to FALSE, otherwise CMake will set it to TRUE
    set(phidgets_analog_inputs_FOUND FALSE)
  elseif(NOT phidgets_analog_inputs_FOUND)
    # use separate condition to avoid uninitialized variable warning
    set(phidgets_analog_inputs_FOUND FALSE)
  endif()
  return()
endif()
set(_phidgets_analog_inputs_CONFIG_INCLUDED TRUE)

# output package information
if(NOT phidgets_analog_inputs_FIND_QUIETLY)
  message(STATUS "Found phidgets_analog_inputs: 2.3.1 (${phidgets_analog_inputs_DIR})")
endif()

# warn when using a deprecated package
if(NOT "" STREQUAL "")
  set(_msg "Package 'phidgets_analog_inputs' is deprecated")
  # append custom deprecation text if available
  if(NOT "" STREQUAL "TRUE")
    set(_msg "${_msg} ()")
  endif()
  # optionally quiet the deprecation message
  if(NOT ${phidgets_analog_inputs_DEPRECATED_QUIET})
    message(DEPRECATION "${_msg}")
  endif()
endif()

# flag package as ament-based to distinguish it after being find_package()-ed
set(phidgets_analog_inputs_FOUND_AMENT_PACKAGE TRUE)

# include all config extra files
set(_extras "")
foreach(_extra ${_extras})
  include("${phidgets_analog_inputs_DIR}/${_extra}")
endforeach()

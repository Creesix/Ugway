// generated from rosidl_generator_c/resource/idl__struct.h.em
// with input from phidgets_msgs:srv/SetDigitalOutput.idl
// generated code does not contain a copyright notice

#ifndef PHIDGETS_MSGS__SRV__DETAIL__SET_DIGITAL_OUTPUT__STRUCT_H_
#define PHIDGETS_MSGS__SRV__DETAIL__SET_DIGITAL_OUTPUT__STRUCT_H_

#ifdef __cplusplus
extern "C"
{
#endif

#include <stdbool.h>
#include <stddef.h>
#include <stdint.h>


// Constants defined in the message

/// Struct defined in srv/SetDigitalOutput in the package phidgets_msgs.
typedef struct phidgets_msgs__srv__SetDigitalOutput_Request
{
  /// index of the output to be set
  uint16_t index;
  bool state;
} phidgets_msgs__srv__SetDigitalOutput_Request;

// Struct for a sequence of phidgets_msgs__srv__SetDigitalOutput_Request.
typedef struct phidgets_msgs__srv__SetDigitalOutput_Request__Sequence
{
  phidgets_msgs__srv__SetDigitalOutput_Request * data;
  /// The number of valid items in data
  size_t size;
  /// The number of allocated items in data
  size_t capacity;
} phidgets_msgs__srv__SetDigitalOutput_Request__Sequence;


// Constants defined in the message

/// Struct defined in srv/SetDigitalOutput in the package phidgets_msgs.
typedef struct phidgets_msgs__srv__SetDigitalOutput_Response
{
  bool success;
} phidgets_msgs__srv__SetDigitalOutput_Response;

// Struct for a sequence of phidgets_msgs__srv__SetDigitalOutput_Response.
typedef struct phidgets_msgs__srv__SetDigitalOutput_Response__Sequence
{
  phidgets_msgs__srv__SetDigitalOutput_Response * data;
  /// The number of valid items in data
  size_t size;
  /// The number of allocated items in data
  size_t capacity;
} phidgets_msgs__srv__SetDigitalOutput_Response__Sequence;

#ifdef __cplusplus
}
#endif

#endif  // PHIDGETS_MSGS__SRV__DETAIL__SET_DIGITAL_OUTPUT__STRUCT_H_

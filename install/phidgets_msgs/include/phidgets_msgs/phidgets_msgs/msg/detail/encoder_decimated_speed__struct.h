// generated from rosidl_generator_c/resource/idl__struct.h.em
// with input from phidgets_msgs:msg/EncoderDecimatedSpeed.idl
// generated code does not contain a copyright notice

#ifndef PHIDGETS_MSGS__MSG__DETAIL__ENCODER_DECIMATED_SPEED__STRUCT_H_
#define PHIDGETS_MSGS__MSG__DETAIL__ENCODER_DECIMATED_SPEED__STRUCT_H_

#ifdef __cplusplus
extern "C"
{
#endif

#include <stdbool.h>
#include <stddef.h>
#include <stdint.h>


// Constants defined in the message

// Include directives for member types
// Member 'header'
#include "std_msgs/msg/detail/header__struct.h"

/// Struct defined in msg/EncoderDecimatedSpeed in the package phidgets_msgs.
/**
  * Encoder averaged speed for a channel in a Phidgets High-Speed Encoder board
 */
typedef struct phidgets_msgs__msg__EncoderDecimatedSpeed
{
  std_msgs__msg__Header header;
  /// Averaged (sliding window) speed estimation
  double avr_speed;
} phidgets_msgs__msg__EncoderDecimatedSpeed;

// Struct for a sequence of phidgets_msgs__msg__EncoderDecimatedSpeed.
typedef struct phidgets_msgs__msg__EncoderDecimatedSpeed__Sequence
{
  phidgets_msgs__msg__EncoderDecimatedSpeed * data;
  /// The number of valid items in data
  size_t size;
  /// The number of allocated items in data
  size_t capacity;
} phidgets_msgs__msg__EncoderDecimatedSpeed__Sequence;

#ifdef __cplusplus
}
#endif

#endif  // PHIDGETS_MSGS__MSG__DETAIL__ENCODER_DECIMATED_SPEED__STRUCT_H_

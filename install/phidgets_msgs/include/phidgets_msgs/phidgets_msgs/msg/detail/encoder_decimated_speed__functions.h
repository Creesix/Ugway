// generated from rosidl_generator_c/resource/idl__functions.h.em
// with input from phidgets_msgs:msg/EncoderDecimatedSpeed.idl
// generated code does not contain a copyright notice

#ifndef PHIDGETS_MSGS__MSG__DETAIL__ENCODER_DECIMATED_SPEED__FUNCTIONS_H_
#define PHIDGETS_MSGS__MSG__DETAIL__ENCODER_DECIMATED_SPEED__FUNCTIONS_H_

#ifdef __cplusplus
extern "C"
{
#endif

#include <stdbool.h>
#include <stdlib.h>

#include "rosidl_runtime_c/visibility_control.h"
#include "phidgets_msgs/msg/rosidl_generator_c__visibility_control.h"

#include "phidgets_msgs/msg/detail/encoder_decimated_speed__struct.h"

/// Initialize msg/EncoderDecimatedSpeed message.
/**
 * If the init function is called twice for the same message without
 * calling fini inbetween previously allocated memory will be leaked.
 * \param[in,out] msg The previously allocated message pointer.
 * Fields without a default value will not be initialized by this function.
 * You might want to call memset(msg, 0, sizeof(
 * phidgets_msgs__msg__EncoderDecimatedSpeed
 * )) before or use
 * phidgets_msgs__msg__EncoderDecimatedSpeed__create()
 * to allocate and initialize the message.
 * \return true if initialization was successful, otherwise false
 */
ROSIDL_GENERATOR_C_PUBLIC_phidgets_msgs
bool
phidgets_msgs__msg__EncoderDecimatedSpeed__init(phidgets_msgs__msg__EncoderDecimatedSpeed * msg);

/// Finalize msg/EncoderDecimatedSpeed message.
/**
 * \param[in,out] msg The allocated message pointer.
 */
ROSIDL_GENERATOR_C_PUBLIC_phidgets_msgs
void
phidgets_msgs__msg__EncoderDecimatedSpeed__fini(phidgets_msgs__msg__EncoderDecimatedSpeed * msg);

/// Create msg/EncoderDecimatedSpeed message.
/**
 * It allocates the memory for the message, sets the memory to zero, and
 * calls
 * phidgets_msgs__msg__EncoderDecimatedSpeed__init().
 * \return The pointer to the initialized message if successful,
 * otherwise NULL
 */
ROSIDL_GENERATOR_C_PUBLIC_phidgets_msgs
phidgets_msgs__msg__EncoderDecimatedSpeed *
phidgets_msgs__msg__EncoderDecimatedSpeed__create();

/// Destroy msg/EncoderDecimatedSpeed message.
/**
 * It calls
 * phidgets_msgs__msg__EncoderDecimatedSpeed__fini()
 * and frees the memory of the message.
 * \param[in,out] msg The allocated message pointer.
 */
ROSIDL_GENERATOR_C_PUBLIC_phidgets_msgs
void
phidgets_msgs__msg__EncoderDecimatedSpeed__destroy(phidgets_msgs__msg__EncoderDecimatedSpeed * msg);

/// Check for msg/EncoderDecimatedSpeed message equality.
/**
 * \param[in] lhs The message on the left hand size of the equality operator.
 * \param[in] rhs The message on the right hand size of the equality operator.
 * \return true if messages are equal, otherwise false.
 */
ROSIDL_GENERATOR_C_PUBLIC_phidgets_msgs
bool
phidgets_msgs__msg__EncoderDecimatedSpeed__are_equal(const phidgets_msgs__msg__EncoderDecimatedSpeed * lhs, const phidgets_msgs__msg__EncoderDecimatedSpeed * rhs);

/// Copy a msg/EncoderDecimatedSpeed message.
/**
 * This functions performs a deep copy, as opposed to the shallow copy that
 * plain assignment yields.
 *
 * \param[in] input The source message pointer.
 * \param[out] output The target message pointer, which must
 *   have been initialized before calling this function.
 * \return true if successful, or false if either pointer is null
 *   or memory allocation fails.
 */
ROSIDL_GENERATOR_C_PUBLIC_phidgets_msgs
bool
phidgets_msgs__msg__EncoderDecimatedSpeed__copy(
  const phidgets_msgs__msg__EncoderDecimatedSpeed * input,
  phidgets_msgs__msg__EncoderDecimatedSpeed * output);

/// Initialize array of msg/EncoderDecimatedSpeed messages.
/**
 * It allocates the memory for the number of elements and calls
 * phidgets_msgs__msg__EncoderDecimatedSpeed__init()
 * for each element of the array.
 * \param[in,out] array The allocated array pointer.
 * \param[in] size The size / capacity of the array.
 * \return true if initialization was successful, otherwise false
 * If the array pointer is valid and the size is zero it is guaranteed
 # to return true.
 */
ROSIDL_GENERATOR_C_PUBLIC_phidgets_msgs
bool
phidgets_msgs__msg__EncoderDecimatedSpeed__Sequence__init(phidgets_msgs__msg__EncoderDecimatedSpeed__Sequence * array, size_t size);

/// Finalize array of msg/EncoderDecimatedSpeed messages.
/**
 * It calls
 * phidgets_msgs__msg__EncoderDecimatedSpeed__fini()
 * for each element of the array and frees the memory for the number of
 * elements.
 * \param[in,out] array The initialized array pointer.
 */
ROSIDL_GENERATOR_C_PUBLIC_phidgets_msgs
void
phidgets_msgs__msg__EncoderDecimatedSpeed__Sequence__fini(phidgets_msgs__msg__EncoderDecimatedSpeed__Sequence * array);

/// Create array of msg/EncoderDecimatedSpeed messages.
/**
 * It allocates the memory for the array and calls
 * phidgets_msgs__msg__EncoderDecimatedSpeed__Sequence__init().
 * \param[in] size The size / capacity of the array.
 * \return The pointer to the initialized array if successful, otherwise NULL
 */
ROSIDL_GENERATOR_C_PUBLIC_phidgets_msgs
phidgets_msgs__msg__EncoderDecimatedSpeed__Sequence *
phidgets_msgs__msg__EncoderDecimatedSpeed__Sequence__create(size_t size);

/// Destroy array of msg/EncoderDecimatedSpeed messages.
/**
 * It calls
 * phidgets_msgs__msg__EncoderDecimatedSpeed__Sequence__fini()
 * on the array,
 * and frees the memory of the array.
 * \param[in,out] array The initialized array pointer.
 */
ROSIDL_GENERATOR_C_PUBLIC_phidgets_msgs
void
phidgets_msgs__msg__EncoderDecimatedSpeed__Sequence__destroy(phidgets_msgs__msg__EncoderDecimatedSpeed__Sequence * array);

/// Check for msg/EncoderDecimatedSpeed message array equality.
/**
 * \param[in] lhs The message array on the left hand size of the equality operator.
 * \param[in] rhs The message array on the right hand size of the equality operator.
 * \return true if message arrays are equal in size and content, otherwise false.
 */
ROSIDL_GENERATOR_C_PUBLIC_phidgets_msgs
bool
phidgets_msgs__msg__EncoderDecimatedSpeed__Sequence__are_equal(const phidgets_msgs__msg__EncoderDecimatedSpeed__Sequence * lhs, const phidgets_msgs__msg__EncoderDecimatedSpeed__Sequence * rhs);

/// Copy an array of msg/EncoderDecimatedSpeed messages.
/**
 * This functions performs a deep copy, as opposed to the shallow copy that
 * plain assignment yields.
 *
 * \param[in] input The source array pointer.
 * \param[out] output The target array pointer, which must
 *   have been initialized before calling this function.
 * \return true if successful, or false if either pointer
 *   is null or memory allocation fails.
 */
ROSIDL_GENERATOR_C_PUBLIC_phidgets_msgs
bool
phidgets_msgs__msg__EncoderDecimatedSpeed__Sequence__copy(
  const phidgets_msgs__msg__EncoderDecimatedSpeed__Sequence * input,
  phidgets_msgs__msg__EncoderDecimatedSpeed__Sequence * output);

#ifdef __cplusplus
}
#endif

#endif  // PHIDGETS_MSGS__MSG__DETAIL__ENCODER_DECIMATED_SPEED__FUNCTIONS_H_

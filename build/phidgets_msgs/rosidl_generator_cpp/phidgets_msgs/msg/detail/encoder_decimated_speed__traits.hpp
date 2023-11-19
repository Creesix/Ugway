// generated from rosidl_generator_cpp/resource/idl__traits.hpp.em
// with input from phidgets_msgs:msg/EncoderDecimatedSpeed.idl
// generated code does not contain a copyright notice

#ifndef PHIDGETS_MSGS__MSG__DETAIL__ENCODER_DECIMATED_SPEED__TRAITS_HPP_
#define PHIDGETS_MSGS__MSG__DETAIL__ENCODER_DECIMATED_SPEED__TRAITS_HPP_

#include <stdint.h>

#include <sstream>
#include <string>
#include <type_traits>

#include "phidgets_msgs/msg/detail/encoder_decimated_speed__struct.hpp"
#include "rosidl_runtime_cpp/traits.hpp"

// Include directives for member types
// Member 'header'
#include "std_msgs/msg/detail/header__traits.hpp"

namespace phidgets_msgs
{

namespace msg
{

inline void to_flow_style_yaml(
  const EncoderDecimatedSpeed & msg,
  std::ostream & out)
{
  out << "{";
  // member: header
  {
    out << "header: ";
    to_flow_style_yaml(msg.header, out);
    out << ", ";
  }

  // member: avr_speed
  {
    out << "avr_speed: ";
    rosidl_generator_traits::value_to_yaml(msg.avr_speed, out);
  }
  out << "}";
}  // NOLINT(readability/fn_size)

inline void to_block_style_yaml(
  const EncoderDecimatedSpeed & msg,
  std::ostream & out, size_t indentation = 0)
{
  // member: header
  {
    if (indentation > 0) {
      out << std::string(indentation, ' ');
    }
    out << "header:\n";
    to_block_style_yaml(msg.header, out, indentation + 2);
  }

  // member: avr_speed
  {
    if (indentation > 0) {
      out << std::string(indentation, ' ');
    }
    out << "avr_speed: ";
    rosidl_generator_traits::value_to_yaml(msg.avr_speed, out);
    out << "\n";
  }
}  // NOLINT(readability/fn_size)

inline std::string to_yaml(const EncoderDecimatedSpeed & msg, bool use_flow_style = false)
{
  std::ostringstream out;
  if (use_flow_style) {
    to_flow_style_yaml(msg, out);
  } else {
    to_block_style_yaml(msg, out);
  }
  return out.str();
}

}  // namespace msg

}  // namespace phidgets_msgs

namespace rosidl_generator_traits
{

[[deprecated("use phidgets_msgs::msg::to_block_style_yaml() instead")]]
inline void to_yaml(
  const phidgets_msgs::msg::EncoderDecimatedSpeed & msg,
  std::ostream & out, size_t indentation = 0)
{
  phidgets_msgs::msg::to_block_style_yaml(msg, out, indentation);
}

[[deprecated("use phidgets_msgs::msg::to_yaml() instead")]]
inline std::string to_yaml(const phidgets_msgs::msg::EncoderDecimatedSpeed & msg)
{
  return phidgets_msgs::msg::to_yaml(msg);
}

template<>
inline const char * data_type<phidgets_msgs::msg::EncoderDecimatedSpeed>()
{
  return "phidgets_msgs::msg::EncoderDecimatedSpeed";
}

template<>
inline const char * name<phidgets_msgs::msg::EncoderDecimatedSpeed>()
{
  return "phidgets_msgs/msg/EncoderDecimatedSpeed";
}

template<>
struct has_fixed_size<phidgets_msgs::msg::EncoderDecimatedSpeed>
  : std::integral_constant<bool, has_fixed_size<std_msgs::msg::Header>::value> {};

template<>
struct has_bounded_size<phidgets_msgs::msg::EncoderDecimatedSpeed>
  : std::integral_constant<bool, has_bounded_size<std_msgs::msg::Header>::value> {};

template<>
struct is_message<phidgets_msgs::msg::EncoderDecimatedSpeed>
  : std::true_type {};

}  // namespace rosidl_generator_traits

#endif  // PHIDGETS_MSGS__MSG__DETAIL__ENCODER_DECIMATED_SPEED__TRAITS_HPP_

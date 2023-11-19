// generated from rosidl_generator_cpp/resource/idl__traits.hpp.em
// with input from phidgets_msgs:srv/SetAnalogOutput.idl
// generated code does not contain a copyright notice

#ifndef PHIDGETS_MSGS__SRV__DETAIL__SET_ANALOG_OUTPUT__TRAITS_HPP_
#define PHIDGETS_MSGS__SRV__DETAIL__SET_ANALOG_OUTPUT__TRAITS_HPP_

#include <stdint.h>

#include <sstream>
#include <string>
#include <type_traits>

#include "phidgets_msgs/srv/detail/set_analog_output__struct.hpp"
#include "rosidl_runtime_cpp/traits.hpp"

namespace phidgets_msgs
{

namespace srv
{

inline void to_flow_style_yaml(
  const SetAnalogOutput_Request & msg,
  std::ostream & out)
{
  out << "{";
  // member: index
  {
    out << "index: ";
    rosidl_generator_traits::value_to_yaml(msg.index, out);
    out << ", ";
  }

  // member: voltage
  {
    out << "voltage: ";
    rosidl_generator_traits::value_to_yaml(msg.voltage, out);
  }
  out << "}";
}  // NOLINT(readability/fn_size)

inline void to_block_style_yaml(
  const SetAnalogOutput_Request & msg,
  std::ostream & out, size_t indentation = 0)
{
  // member: index
  {
    if (indentation > 0) {
      out << std::string(indentation, ' ');
    }
    out << "index: ";
    rosidl_generator_traits::value_to_yaml(msg.index, out);
    out << "\n";
  }

  // member: voltage
  {
    if (indentation > 0) {
      out << std::string(indentation, ' ');
    }
    out << "voltage: ";
    rosidl_generator_traits::value_to_yaml(msg.voltage, out);
    out << "\n";
  }
}  // NOLINT(readability/fn_size)

inline std::string to_yaml(const SetAnalogOutput_Request & msg, bool use_flow_style = false)
{
  std::ostringstream out;
  if (use_flow_style) {
    to_flow_style_yaml(msg, out);
  } else {
    to_block_style_yaml(msg, out);
  }
  return out.str();
}

}  // namespace srv

}  // namespace phidgets_msgs

namespace rosidl_generator_traits
{

[[deprecated("use phidgets_msgs::srv::to_block_style_yaml() instead")]]
inline void to_yaml(
  const phidgets_msgs::srv::SetAnalogOutput_Request & msg,
  std::ostream & out, size_t indentation = 0)
{
  phidgets_msgs::srv::to_block_style_yaml(msg, out, indentation);
}

[[deprecated("use phidgets_msgs::srv::to_yaml() instead")]]
inline std::string to_yaml(const phidgets_msgs::srv::SetAnalogOutput_Request & msg)
{
  return phidgets_msgs::srv::to_yaml(msg);
}

template<>
inline const char * data_type<phidgets_msgs::srv::SetAnalogOutput_Request>()
{
  return "phidgets_msgs::srv::SetAnalogOutput_Request";
}

template<>
inline const char * name<phidgets_msgs::srv::SetAnalogOutput_Request>()
{
  return "phidgets_msgs/srv/SetAnalogOutput_Request";
}

template<>
struct has_fixed_size<phidgets_msgs::srv::SetAnalogOutput_Request>
  : std::integral_constant<bool, true> {};

template<>
struct has_bounded_size<phidgets_msgs::srv::SetAnalogOutput_Request>
  : std::integral_constant<bool, true> {};

template<>
struct is_message<phidgets_msgs::srv::SetAnalogOutput_Request>
  : std::true_type {};

}  // namespace rosidl_generator_traits

namespace phidgets_msgs
{

namespace srv
{

inline void to_flow_style_yaml(
  const SetAnalogOutput_Response & msg,
  std::ostream & out)
{
  out << "{";
  // member: success
  {
    out << "success: ";
    rosidl_generator_traits::value_to_yaml(msg.success, out);
  }
  out << "}";
}  // NOLINT(readability/fn_size)

inline void to_block_style_yaml(
  const SetAnalogOutput_Response & msg,
  std::ostream & out, size_t indentation = 0)
{
  // member: success
  {
    if (indentation > 0) {
      out << std::string(indentation, ' ');
    }
    out << "success: ";
    rosidl_generator_traits::value_to_yaml(msg.success, out);
    out << "\n";
  }
}  // NOLINT(readability/fn_size)

inline std::string to_yaml(const SetAnalogOutput_Response & msg, bool use_flow_style = false)
{
  std::ostringstream out;
  if (use_flow_style) {
    to_flow_style_yaml(msg, out);
  } else {
    to_block_style_yaml(msg, out);
  }
  return out.str();
}

}  // namespace srv

}  // namespace phidgets_msgs

namespace rosidl_generator_traits
{

[[deprecated("use phidgets_msgs::srv::to_block_style_yaml() instead")]]
inline void to_yaml(
  const phidgets_msgs::srv::SetAnalogOutput_Response & msg,
  std::ostream & out, size_t indentation = 0)
{
  phidgets_msgs::srv::to_block_style_yaml(msg, out, indentation);
}

[[deprecated("use phidgets_msgs::srv::to_yaml() instead")]]
inline std::string to_yaml(const phidgets_msgs::srv::SetAnalogOutput_Response & msg)
{
  return phidgets_msgs::srv::to_yaml(msg);
}

template<>
inline const char * data_type<phidgets_msgs::srv::SetAnalogOutput_Response>()
{
  return "phidgets_msgs::srv::SetAnalogOutput_Response";
}

template<>
inline const char * name<phidgets_msgs::srv::SetAnalogOutput_Response>()
{
  return "phidgets_msgs/srv/SetAnalogOutput_Response";
}

template<>
struct has_fixed_size<phidgets_msgs::srv::SetAnalogOutput_Response>
  : std::integral_constant<bool, true> {};

template<>
struct has_bounded_size<phidgets_msgs::srv::SetAnalogOutput_Response>
  : std::integral_constant<bool, true> {};

template<>
struct is_message<phidgets_msgs::srv::SetAnalogOutput_Response>
  : std::true_type {};

}  // namespace rosidl_generator_traits

namespace rosidl_generator_traits
{

template<>
inline const char * data_type<phidgets_msgs::srv::SetAnalogOutput>()
{
  return "phidgets_msgs::srv::SetAnalogOutput";
}

template<>
inline const char * name<phidgets_msgs::srv::SetAnalogOutput>()
{
  return "phidgets_msgs/srv/SetAnalogOutput";
}

template<>
struct has_fixed_size<phidgets_msgs::srv::SetAnalogOutput>
  : std::integral_constant<
    bool,
    has_fixed_size<phidgets_msgs::srv::SetAnalogOutput_Request>::value &&
    has_fixed_size<phidgets_msgs::srv::SetAnalogOutput_Response>::value
  >
{
};

template<>
struct has_bounded_size<phidgets_msgs::srv::SetAnalogOutput>
  : std::integral_constant<
    bool,
    has_bounded_size<phidgets_msgs::srv::SetAnalogOutput_Request>::value &&
    has_bounded_size<phidgets_msgs::srv::SetAnalogOutput_Response>::value
  >
{
};

template<>
struct is_service<phidgets_msgs::srv::SetAnalogOutput>
  : std::true_type
{
};

template<>
struct is_service_request<phidgets_msgs::srv::SetAnalogOutput_Request>
  : std::true_type
{
};

template<>
struct is_service_response<phidgets_msgs::srv::SetAnalogOutput_Response>
  : std::true_type
{
};

}  // namespace rosidl_generator_traits

#endif  // PHIDGETS_MSGS__SRV__DETAIL__SET_ANALOG_OUTPUT__TRAITS_HPP_

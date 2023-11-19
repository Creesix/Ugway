// generated from rosidl_generator_cpp/resource/idl__builder.hpp.em
// with input from phidgets_msgs:msg/EncoderDecimatedSpeed.idl
// generated code does not contain a copyright notice

#ifndef PHIDGETS_MSGS__MSG__DETAIL__ENCODER_DECIMATED_SPEED__BUILDER_HPP_
#define PHIDGETS_MSGS__MSG__DETAIL__ENCODER_DECIMATED_SPEED__BUILDER_HPP_

#include <algorithm>
#include <utility>

#include "phidgets_msgs/msg/detail/encoder_decimated_speed__struct.hpp"
#include "rosidl_runtime_cpp/message_initialization.hpp"


namespace phidgets_msgs
{

namespace msg
{

namespace builder
{

class Init_EncoderDecimatedSpeed_avr_speed
{
public:
  explicit Init_EncoderDecimatedSpeed_avr_speed(::phidgets_msgs::msg::EncoderDecimatedSpeed & msg)
  : msg_(msg)
  {}
  ::phidgets_msgs::msg::EncoderDecimatedSpeed avr_speed(::phidgets_msgs::msg::EncoderDecimatedSpeed::_avr_speed_type arg)
  {
    msg_.avr_speed = std::move(arg);
    return std::move(msg_);
  }

private:
  ::phidgets_msgs::msg::EncoderDecimatedSpeed msg_;
};

class Init_EncoderDecimatedSpeed_header
{
public:
  Init_EncoderDecimatedSpeed_header()
  : msg_(::rosidl_runtime_cpp::MessageInitialization::SKIP)
  {}
  Init_EncoderDecimatedSpeed_avr_speed header(::phidgets_msgs::msg::EncoderDecimatedSpeed::_header_type arg)
  {
    msg_.header = std::move(arg);
    return Init_EncoderDecimatedSpeed_avr_speed(msg_);
  }

private:
  ::phidgets_msgs::msg::EncoderDecimatedSpeed msg_;
};

}  // namespace builder

}  // namespace msg

template<typename MessageType>
auto build();

template<>
inline
auto build<::phidgets_msgs::msg::EncoderDecimatedSpeed>()
{
  return phidgets_msgs::msg::builder::Init_EncoderDecimatedSpeed_header();
}

}  // namespace phidgets_msgs

#endif  // PHIDGETS_MSGS__MSG__DETAIL__ENCODER_DECIMATED_SPEED__BUILDER_HPP_

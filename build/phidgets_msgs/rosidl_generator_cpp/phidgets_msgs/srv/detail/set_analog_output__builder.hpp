// generated from rosidl_generator_cpp/resource/idl__builder.hpp.em
// with input from phidgets_msgs:srv/SetAnalogOutput.idl
// generated code does not contain a copyright notice

#ifndef PHIDGETS_MSGS__SRV__DETAIL__SET_ANALOG_OUTPUT__BUILDER_HPP_
#define PHIDGETS_MSGS__SRV__DETAIL__SET_ANALOG_OUTPUT__BUILDER_HPP_

#include <algorithm>
#include <utility>

#include "phidgets_msgs/srv/detail/set_analog_output__struct.hpp"
#include "rosidl_runtime_cpp/message_initialization.hpp"


namespace phidgets_msgs
{

namespace srv
{

namespace builder
{

class Init_SetAnalogOutput_Request_voltage
{
public:
  explicit Init_SetAnalogOutput_Request_voltage(::phidgets_msgs::srv::SetAnalogOutput_Request & msg)
  : msg_(msg)
  {}
  ::phidgets_msgs::srv::SetAnalogOutput_Request voltage(::phidgets_msgs::srv::SetAnalogOutput_Request::_voltage_type arg)
  {
    msg_.voltage = std::move(arg);
    return std::move(msg_);
  }

private:
  ::phidgets_msgs::srv::SetAnalogOutput_Request msg_;
};

class Init_SetAnalogOutput_Request_index
{
public:
  Init_SetAnalogOutput_Request_index()
  : msg_(::rosidl_runtime_cpp::MessageInitialization::SKIP)
  {}
  Init_SetAnalogOutput_Request_voltage index(::phidgets_msgs::srv::SetAnalogOutput_Request::_index_type arg)
  {
    msg_.index = std::move(arg);
    return Init_SetAnalogOutput_Request_voltage(msg_);
  }

private:
  ::phidgets_msgs::srv::SetAnalogOutput_Request msg_;
};

}  // namespace builder

}  // namespace srv

template<typename MessageType>
auto build();

template<>
inline
auto build<::phidgets_msgs::srv::SetAnalogOutput_Request>()
{
  return phidgets_msgs::srv::builder::Init_SetAnalogOutput_Request_index();
}

}  // namespace phidgets_msgs


namespace phidgets_msgs
{

namespace srv
{

namespace builder
{

class Init_SetAnalogOutput_Response_success
{
public:
  Init_SetAnalogOutput_Response_success()
  : msg_(::rosidl_runtime_cpp::MessageInitialization::SKIP)
  {}
  ::phidgets_msgs::srv::SetAnalogOutput_Response success(::phidgets_msgs::srv::SetAnalogOutput_Response::_success_type arg)
  {
    msg_.success = std::move(arg);
    return std::move(msg_);
  }

private:
  ::phidgets_msgs::srv::SetAnalogOutput_Response msg_;
};

}  // namespace builder

}  // namespace srv

template<typename MessageType>
auto build();

template<>
inline
auto build<::phidgets_msgs::srv::SetAnalogOutput_Response>()
{
  return phidgets_msgs::srv::builder::Init_SetAnalogOutput_Response_success();
}

}  // namespace phidgets_msgs

#endif  // PHIDGETS_MSGS__SRV__DETAIL__SET_ANALOG_OUTPUT__BUILDER_HPP_

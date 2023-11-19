// generated from rosidl_generator_cpp/resource/idl__builder.hpp.em
// with input from phidgets_msgs:srv/SetDigitalOutput.idl
// generated code does not contain a copyright notice

#ifndef PHIDGETS_MSGS__SRV__DETAIL__SET_DIGITAL_OUTPUT__BUILDER_HPP_
#define PHIDGETS_MSGS__SRV__DETAIL__SET_DIGITAL_OUTPUT__BUILDER_HPP_

#include <algorithm>
#include <utility>

#include "phidgets_msgs/srv/detail/set_digital_output__struct.hpp"
#include "rosidl_runtime_cpp/message_initialization.hpp"


namespace phidgets_msgs
{

namespace srv
{

namespace builder
{

class Init_SetDigitalOutput_Request_state
{
public:
  explicit Init_SetDigitalOutput_Request_state(::phidgets_msgs::srv::SetDigitalOutput_Request & msg)
  : msg_(msg)
  {}
  ::phidgets_msgs::srv::SetDigitalOutput_Request state(::phidgets_msgs::srv::SetDigitalOutput_Request::_state_type arg)
  {
    msg_.state = std::move(arg);
    return std::move(msg_);
  }

private:
  ::phidgets_msgs::srv::SetDigitalOutput_Request msg_;
};

class Init_SetDigitalOutput_Request_index
{
public:
  Init_SetDigitalOutput_Request_index()
  : msg_(::rosidl_runtime_cpp::MessageInitialization::SKIP)
  {}
  Init_SetDigitalOutput_Request_state index(::phidgets_msgs::srv::SetDigitalOutput_Request::_index_type arg)
  {
    msg_.index = std::move(arg);
    return Init_SetDigitalOutput_Request_state(msg_);
  }

private:
  ::phidgets_msgs::srv::SetDigitalOutput_Request msg_;
};

}  // namespace builder

}  // namespace srv

template<typename MessageType>
auto build();

template<>
inline
auto build<::phidgets_msgs::srv::SetDigitalOutput_Request>()
{
  return phidgets_msgs::srv::builder::Init_SetDigitalOutput_Request_index();
}

}  // namespace phidgets_msgs


namespace phidgets_msgs
{

namespace srv
{

namespace builder
{

class Init_SetDigitalOutput_Response_success
{
public:
  Init_SetDigitalOutput_Response_success()
  : msg_(::rosidl_runtime_cpp::MessageInitialization::SKIP)
  {}
  ::phidgets_msgs::srv::SetDigitalOutput_Response success(::phidgets_msgs::srv::SetDigitalOutput_Response::_success_type arg)
  {
    msg_.success = std::move(arg);
    return std::move(msg_);
  }

private:
  ::phidgets_msgs::srv::SetDigitalOutput_Response msg_;
};

}  // namespace builder

}  // namespace srv

template<typename MessageType>
auto build();

template<>
inline
auto build<::phidgets_msgs::srv::SetDigitalOutput_Response>()
{
  return phidgets_msgs::srv::builder::Init_SetDigitalOutput_Response_success();
}

}  // namespace phidgets_msgs

#endif  // PHIDGETS_MSGS__SRV__DETAIL__SET_DIGITAL_OUTPUT__BUILDER_HPP_

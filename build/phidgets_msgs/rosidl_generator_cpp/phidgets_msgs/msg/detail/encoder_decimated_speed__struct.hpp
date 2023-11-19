// generated from rosidl_generator_cpp/resource/idl__struct.hpp.em
// with input from phidgets_msgs:msg/EncoderDecimatedSpeed.idl
// generated code does not contain a copyright notice

#ifndef PHIDGETS_MSGS__MSG__DETAIL__ENCODER_DECIMATED_SPEED__STRUCT_HPP_
#define PHIDGETS_MSGS__MSG__DETAIL__ENCODER_DECIMATED_SPEED__STRUCT_HPP_

#include <algorithm>
#include <array>
#include <memory>
#include <string>
#include <vector>

#include "rosidl_runtime_cpp/bounded_vector.hpp"
#include "rosidl_runtime_cpp/message_initialization.hpp"


// Include directives for member types
// Member 'header'
#include "std_msgs/msg/detail/header__struct.hpp"

#ifndef _WIN32
# define DEPRECATED__phidgets_msgs__msg__EncoderDecimatedSpeed __attribute__((deprecated))
#else
# define DEPRECATED__phidgets_msgs__msg__EncoderDecimatedSpeed __declspec(deprecated)
#endif

namespace phidgets_msgs
{

namespace msg
{

// message struct
template<class ContainerAllocator>
struct EncoderDecimatedSpeed_
{
  using Type = EncoderDecimatedSpeed_<ContainerAllocator>;

  explicit EncoderDecimatedSpeed_(rosidl_runtime_cpp::MessageInitialization _init = rosidl_runtime_cpp::MessageInitialization::ALL)
  : header(_init)
  {
    if (rosidl_runtime_cpp::MessageInitialization::ALL == _init ||
      rosidl_runtime_cpp::MessageInitialization::ZERO == _init)
    {
      this->avr_speed = 0.0;
    }
  }

  explicit EncoderDecimatedSpeed_(const ContainerAllocator & _alloc, rosidl_runtime_cpp::MessageInitialization _init = rosidl_runtime_cpp::MessageInitialization::ALL)
  : header(_alloc, _init)
  {
    if (rosidl_runtime_cpp::MessageInitialization::ALL == _init ||
      rosidl_runtime_cpp::MessageInitialization::ZERO == _init)
    {
      this->avr_speed = 0.0;
    }
  }

  // field types and members
  using _header_type =
    std_msgs::msg::Header_<ContainerAllocator>;
  _header_type header;
  using _avr_speed_type =
    double;
  _avr_speed_type avr_speed;

  // setters for named parameter idiom
  Type & set__header(
    const std_msgs::msg::Header_<ContainerAllocator> & _arg)
  {
    this->header = _arg;
    return *this;
  }
  Type & set__avr_speed(
    const double & _arg)
  {
    this->avr_speed = _arg;
    return *this;
  }

  // constant declarations

  // pointer types
  using RawPtr =
    phidgets_msgs::msg::EncoderDecimatedSpeed_<ContainerAllocator> *;
  using ConstRawPtr =
    const phidgets_msgs::msg::EncoderDecimatedSpeed_<ContainerAllocator> *;
  using SharedPtr =
    std::shared_ptr<phidgets_msgs::msg::EncoderDecimatedSpeed_<ContainerAllocator>>;
  using ConstSharedPtr =
    std::shared_ptr<phidgets_msgs::msg::EncoderDecimatedSpeed_<ContainerAllocator> const>;

  template<typename Deleter = std::default_delete<
      phidgets_msgs::msg::EncoderDecimatedSpeed_<ContainerAllocator>>>
  using UniquePtrWithDeleter =
    std::unique_ptr<phidgets_msgs::msg::EncoderDecimatedSpeed_<ContainerAllocator>, Deleter>;

  using UniquePtr = UniquePtrWithDeleter<>;

  template<typename Deleter = std::default_delete<
      phidgets_msgs::msg::EncoderDecimatedSpeed_<ContainerAllocator>>>
  using ConstUniquePtrWithDeleter =
    std::unique_ptr<phidgets_msgs::msg::EncoderDecimatedSpeed_<ContainerAllocator> const, Deleter>;
  using ConstUniquePtr = ConstUniquePtrWithDeleter<>;

  using WeakPtr =
    std::weak_ptr<phidgets_msgs::msg::EncoderDecimatedSpeed_<ContainerAllocator>>;
  using ConstWeakPtr =
    std::weak_ptr<phidgets_msgs::msg::EncoderDecimatedSpeed_<ContainerAllocator> const>;

  // pointer types similar to ROS 1, use SharedPtr / ConstSharedPtr instead
  // NOTE: Can't use 'using' here because GNU C++ can't parse attributes properly
  typedef DEPRECATED__phidgets_msgs__msg__EncoderDecimatedSpeed
    std::shared_ptr<phidgets_msgs::msg::EncoderDecimatedSpeed_<ContainerAllocator>>
    Ptr;
  typedef DEPRECATED__phidgets_msgs__msg__EncoderDecimatedSpeed
    std::shared_ptr<phidgets_msgs::msg::EncoderDecimatedSpeed_<ContainerAllocator> const>
    ConstPtr;

  // comparison operators
  bool operator==(const EncoderDecimatedSpeed_ & other) const
  {
    if (this->header != other.header) {
      return false;
    }
    if (this->avr_speed != other.avr_speed) {
      return false;
    }
    return true;
  }
  bool operator!=(const EncoderDecimatedSpeed_ & other) const
  {
    return !this->operator==(other);
  }
};  // struct EncoderDecimatedSpeed_

// alias to use template instance with default allocator
using EncoderDecimatedSpeed =
  phidgets_msgs::msg::EncoderDecimatedSpeed_<std::allocator<void>>;

// constant definitions

}  // namespace msg

}  // namespace phidgets_msgs

#endif  // PHIDGETS_MSGS__MSG__DETAIL__ENCODER_DECIMATED_SPEED__STRUCT_HPP_

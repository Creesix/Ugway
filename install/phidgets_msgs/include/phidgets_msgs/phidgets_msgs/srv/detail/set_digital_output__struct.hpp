// generated from rosidl_generator_cpp/resource/idl__struct.hpp.em
// with input from phidgets_msgs:srv/SetDigitalOutput.idl
// generated code does not contain a copyright notice

#ifndef PHIDGETS_MSGS__SRV__DETAIL__SET_DIGITAL_OUTPUT__STRUCT_HPP_
#define PHIDGETS_MSGS__SRV__DETAIL__SET_DIGITAL_OUTPUT__STRUCT_HPP_

#include <algorithm>
#include <array>
#include <memory>
#include <string>
#include <vector>

#include "rosidl_runtime_cpp/bounded_vector.hpp"
#include "rosidl_runtime_cpp/message_initialization.hpp"


#ifndef _WIN32
# define DEPRECATED__phidgets_msgs__srv__SetDigitalOutput_Request __attribute__((deprecated))
#else
# define DEPRECATED__phidgets_msgs__srv__SetDigitalOutput_Request __declspec(deprecated)
#endif

namespace phidgets_msgs
{

namespace srv
{

// message struct
template<class ContainerAllocator>
struct SetDigitalOutput_Request_
{
  using Type = SetDigitalOutput_Request_<ContainerAllocator>;

  explicit SetDigitalOutput_Request_(rosidl_runtime_cpp::MessageInitialization _init = rosidl_runtime_cpp::MessageInitialization::ALL)
  {
    if (rosidl_runtime_cpp::MessageInitialization::ALL == _init ||
      rosidl_runtime_cpp::MessageInitialization::ZERO == _init)
    {
      this->index = 0;
      this->state = false;
    }
  }

  explicit SetDigitalOutput_Request_(const ContainerAllocator & _alloc, rosidl_runtime_cpp::MessageInitialization _init = rosidl_runtime_cpp::MessageInitialization::ALL)
  {
    (void)_alloc;
    if (rosidl_runtime_cpp::MessageInitialization::ALL == _init ||
      rosidl_runtime_cpp::MessageInitialization::ZERO == _init)
    {
      this->index = 0;
      this->state = false;
    }
  }

  // field types and members
  using _index_type =
    uint16_t;
  _index_type index;
  using _state_type =
    bool;
  _state_type state;

  // setters for named parameter idiom
  Type & set__index(
    const uint16_t & _arg)
  {
    this->index = _arg;
    return *this;
  }
  Type & set__state(
    const bool & _arg)
  {
    this->state = _arg;
    return *this;
  }

  // constant declarations

  // pointer types
  using RawPtr =
    phidgets_msgs::srv::SetDigitalOutput_Request_<ContainerAllocator> *;
  using ConstRawPtr =
    const phidgets_msgs::srv::SetDigitalOutput_Request_<ContainerAllocator> *;
  using SharedPtr =
    std::shared_ptr<phidgets_msgs::srv::SetDigitalOutput_Request_<ContainerAllocator>>;
  using ConstSharedPtr =
    std::shared_ptr<phidgets_msgs::srv::SetDigitalOutput_Request_<ContainerAllocator> const>;

  template<typename Deleter = std::default_delete<
      phidgets_msgs::srv::SetDigitalOutput_Request_<ContainerAllocator>>>
  using UniquePtrWithDeleter =
    std::unique_ptr<phidgets_msgs::srv::SetDigitalOutput_Request_<ContainerAllocator>, Deleter>;

  using UniquePtr = UniquePtrWithDeleter<>;

  template<typename Deleter = std::default_delete<
      phidgets_msgs::srv::SetDigitalOutput_Request_<ContainerAllocator>>>
  using ConstUniquePtrWithDeleter =
    std::unique_ptr<phidgets_msgs::srv::SetDigitalOutput_Request_<ContainerAllocator> const, Deleter>;
  using ConstUniquePtr = ConstUniquePtrWithDeleter<>;

  using WeakPtr =
    std::weak_ptr<phidgets_msgs::srv::SetDigitalOutput_Request_<ContainerAllocator>>;
  using ConstWeakPtr =
    std::weak_ptr<phidgets_msgs::srv::SetDigitalOutput_Request_<ContainerAllocator> const>;

  // pointer types similar to ROS 1, use SharedPtr / ConstSharedPtr instead
  // NOTE: Can't use 'using' here because GNU C++ can't parse attributes properly
  typedef DEPRECATED__phidgets_msgs__srv__SetDigitalOutput_Request
    std::shared_ptr<phidgets_msgs::srv::SetDigitalOutput_Request_<ContainerAllocator>>
    Ptr;
  typedef DEPRECATED__phidgets_msgs__srv__SetDigitalOutput_Request
    std::shared_ptr<phidgets_msgs::srv::SetDigitalOutput_Request_<ContainerAllocator> const>
    ConstPtr;

  // comparison operators
  bool operator==(const SetDigitalOutput_Request_ & other) const
  {
    if (this->index != other.index) {
      return false;
    }
    if (this->state != other.state) {
      return false;
    }
    return true;
  }
  bool operator!=(const SetDigitalOutput_Request_ & other) const
  {
    return !this->operator==(other);
  }
};  // struct SetDigitalOutput_Request_

// alias to use template instance with default allocator
using SetDigitalOutput_Request =
  phidgets_msgs::srv::SetDigitalOutput_Request_<std::allocator<void>>;

// constant definitions

}  // namespace srv

}  // namespace phidgets_msgs


#ifndef _WIN32
# define DEPRECATED__phidgets_msgs__srv__SetDigitalOutput_Response __attribute__((deprecated))
#else
# define DEPRECATED__phidgets_msgs__srv__SetDigitalOutput_Response __declspec(deprecated)
#endif

namespace phidgets_msgs
{

namespace srv
{

// message struct
template<class ContainerAllocator>
struct SetDigitalOutput_Response_
{
  using Type = SetDigitalOutput_Response_<ContainerAllocator>;

  explicit SetDigitalOutput_Response_(rosidl_runtime_cpp::MessageInitialization _init = rosidl_runtime_cpp::MessageInitialization::ALL)
  {
    if (rosidl_runtime_cpp::MessageInitialization::ALL == _init ||
      rosidl_runtime_cpp::MessageInitialization::ZERO == _init)
    {
      this->success = false;
    }
  }

  explicit SetDigitalOutput_Response_(const ContainerAllocator & _alloc, rosidl_runtime_cpp::MessageInitialization _init = rosidl_runtime_cpp::MessageInitialization::ALL)
  {
    (void)_alloc;
    if (rosidl_runtime_cpp::MessageInitialization::ALL == _init ||
      rosidl_runtime_cpp::MessageInitialization::ZERO == _init)
    {
      this->success = false;
    }
  }

  // field types and members
  using _success_type =
    bool;
  _success_type success;

  // setters for named parameter idiom
  Type & set__success(
    const bool & _arg)
  {
    this->success = _arg;
    return *this;
  }

  // constant declarations

  // pointer types
  using RawPtr =
    phidgets_msgs::srv::SetDigitalOutput_Response_<ContainerAllocator> *;
  using ConstRawPtr =
    const phidgets_msgs::srv::SetDigitalOutput_Response_<ContainerAllocator> *;
  using SharedPtr =
    std::shared_ptr<phidgets_msgs::srv::SetDigitalOutput_Response_<ContainerAllocator>>;
  using ConstSharedPtr =
    std::shared_ptr<phidgets_msgs::srv::SetDigitalOutput_Response_<ContainerAllocator> const>;

  template<typename Deleter = std::default_delete<
      phidgets_msgs::srv::SetDigitalOutput_Response_<ContainerAllocator>>>
  using UniquePtrWithDeleter =
    std::unique_ptr<phidgets_msgs::srv::SetDigitalOutput_Response_<ContainerAllocator>, Deleter>;

  using UniquePtr = UniquePtrWithDeleter<>;

  template<typename Deleter = std::default_delete<
      phidgets_msgs::srv::SetDigitalOutput_Response_<ContainerAllocator>>>
  using ConstUniquePtrWithDeleter =
    std::unique_ptr<phidgets_msgs::srv::SetDigitalOutput_Response_<ContainerAllocator> const, Deleter>;
  using ConstUniquePtr = ConstUniquePtrWithDeleter<>;

  using WeakPtr =
    std::weak_ptr<phidgets_msgs::srv::SetDigitalOutput_Response_<ContainerAllocator>>;
  using ConstWeakPtr =
    std::weak_ptr<phidgets_msgs::srv::SetDigitalOutput_Response_<ContainerAllocator> const>;

  // pointer types similar to ROS 1, use SharedPtr / ConstSharedPtr instead
  // NOTE: Can't use 'using' here because GNU C++ can't parse attributes properly
  typedef DEPRECATED__phidgets_msgs__srv__SetDigitalOutput_Response
    std::shared_ptr<phidgets_msgs::srv::SetDigitalOutput_Response_<ContainerAllocator>>
    Ptr;
  typedef DEPRECATED__phidgets_msgs__srv__SetDigitalOutput_Response
    std::shared_ptr<phidgets_msgs::srv::SetDigitalOutput_Response_<ContainerAllocator> const>
    ConstPtr;

  // comparison operators
  bool operator==(const SetDigitalOutput_Response_ & other) const
  {
    if (this->success != other.success) {
      return false;
    }
    return true;
  }
  bool operator!=(const SetDigitalOutput_Response_ & other) const
  {
    return !this->operator==(other);
  }
};  // struct SetDigitalOutput_Response_

// alias to use template instance with default allocator
using SetDigitalOutput_Response =
  phidgets_msgs::srv::SetDigitalOutput_Response_<std::allocator<void>>;

// constant definitions

}  // namespace srv

}  // namespace phidgets_msgs

namespace phidgets_msgs
{

namespace srv
{

struct SetDigitalOutput
{
  using Request = phidgets_msgs::srv::SetDigitalOutput_Request;
  using Response = phidgets_msgs::srv::SetDigitalOutput_Response;
};

}  // namespace srv

}  // namespace phidgets_msgs

#endif  // PHIDGETS_MSGS__SRV__DETAIL__SET_DIGITAL_OUTPUT__STRUCT_HPP_

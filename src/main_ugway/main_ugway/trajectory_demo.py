import rclpy
import time
from rclpy.node import Node
from rclpy.action import ActionClient

from phidget_stepper_controllers_msgs.action import Trajectoire
## Verification du StepControllerGoal ##

from std_msgs.msg import Float64, Bool


class TrajectoryActionServer(Node):
    def __init__(self):
        super().__init__('trajectory_server')

        # ROS 2 action client
        self._action_client = ActionClient(
            self,
            Trajectoire, 
            'TrajectoireController'
        )

        self.get_logger().info('trajectory ocntroller Init')


    def send_goal(self, dir, x, y):
        self.get_logger().info('Creating trajectory goal')

        goal_msg = Trajectoire.Goal()
        goal_msg.traj_dir = dir
        goal_msg.traj_x = x
        goal_msg.traj_y = y

        self.get_logger().info('Waiting step_test action')
        self._action_client.wait_for_server()

        self.get_logger().info('Sending goal to step_test')

        return self._action_client.send_goal_async(goal_msg)

def main(args=None):
    rclpy.init(args=args)

    time.sleep(10)

    minimal_Trajectory = TrajectoryActionServer()

    time.sleep(3)
    # ==== TEST 1 SQUARE

    traj_dir = [1.0, 1.0, -1.0, -1.0]
    traj_x = [0.5, 0.5, 1.0, 1.0]
    traj_y = [0.2, 0.7, 0.7, 0.2]

    minimal_Trajectory.get_logger().info(f"Order de fou")

    future = minimal_Trajectory.send_goal_async(traj_dir, traj_x, traj_y)
    minimal_Trajectory.get_logger().info(f"order given actually working on it")
    rclpy.spin_until_future_complete(minimal_Trajectory, future)

    time.sleep(5)

    # Destroy the node explicitly
    # (optional - otherwise it will be done automatically
    # when the garbage collector destroys the node object)
    minimal_Trajectory.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()
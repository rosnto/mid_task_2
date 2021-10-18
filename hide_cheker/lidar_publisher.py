import rospy
from std_msgs.msg import UInt32

def main():
    pub = rospy.Publisher('temp', UInt32, queue_size=10)
    rospy.init_node('node', anonymous=True)
    rate = rospy.Rate(10) # 10hz
    while not rospy.is_shutdown():
        temp = 32
        hello_str = "hello world"
        pub.publish(temp)
        rate.sleep()

if __name__ == '__main__':
    try:
        main()
    except rospy.ROSInterruptException:
        pass
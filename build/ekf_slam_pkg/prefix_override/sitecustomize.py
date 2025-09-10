import sys
if sys.prefix == '/usr':
    sys.real_prefix = sys.prefix
    sys.prefix = sys.exec_prefix = '/home/vyom/EKF_SLAM/install/ekf_slam_pkg'

import sys
if sys.prefix == '/usr':
    sys.real_prefix = sys.prefix
    sys.prefix = sys.exec_prefix = '/home/nishant/Desktop/Projects/Navigation_/hospitalbot_pathplanning/install/hospital_robot_spawner'

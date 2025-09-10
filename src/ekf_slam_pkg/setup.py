from setuptools import find_packages, setup

package_name = 'ekf_slam_pkg'

setup(
    name=package_name,
    version='0.0.0',
    packages=find_packages(exclude=['test']),
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='vyom',
    maintainer_email='vyom2512vyas@gmail.com',
    description='TODO: Package description',
    license='TODO: License declaration',
    tests_require=['pytest'],
    entry_points={
    'console_scripts': [
        'ekf_slam = ekf_slam_pkg.EKF_slam:main',
        'ekf_slam_viz = ekf_slam_pkg.viz_ekf_slam:main',
    ],
},
)

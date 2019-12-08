from setuptools import setup, find_packages
PACKAGES = find_packages()
opts = dict(
    name='AviationAccidentDataVisualizer',
    version='1.0',
    packages=PACKAGES,
    url='https://github.com/TianyiZhang0315/AviationAccidentDataVisualizer',
    license='LICENSE.txt',
    author='Yetao Chen, Yifan Xu, Tianyi Zhang',
    author_email='cyt1208@uw.edu, yxu666@uw.edu, zhang506@uw.edu',
    description='Aviation Accident Data Visualizer is a python package for the use of extraction\
                and visualization of  aviation accident data\
                from the provided dataset.',
    install_requires=['pandas', 'numpy'],


)
if __name__ == '__main__':
    setup(**opts)

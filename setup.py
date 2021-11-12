from setuptools import setup, find_packages
setup(
    name='STDF',
    version='1.0',
    description='STDF Toolbox',
    author= 'wangfei',
    #url='https://github.com/open-mmlab/mmdetection',
    packages=find_packages(exclude=('configs', 'tools', 'demo')),
    
    classifiers=[
        
        'License :: OSI Approved :: Apache Software License',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 3.6',
    ],
    # install_requires=[
    #     'mmcv', 'numpy', 
    # ],
    zip_safe=False)
from setuptools import setup

setup(name='simple_sensor_readers',
      version='0.0.0dev',
      description='A list of scripts to turn all simple sensor readings into one, standardized reading and send to a local SQLite server',
      long_description=open('README.md').read(),
      url='https://github.com/ethan92429/simple_sensor_readers',
      author='Maelstrom Mining',
      author_email='maelstrommining@gmail.com',
      license='MIT',
      packages=['simple_sensor_readers'],
      install_requires=[
          'flask', 'w1thermsensor'
      ],
      zip_safe=False)
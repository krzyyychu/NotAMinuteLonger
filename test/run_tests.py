import unittest

"""
python -m unittest discover <test_directory>
works the same as this script 
"""

loader = unittest.TestLoader()
start_dir = '.'
suite = loader.discover(start_dir)

test_runner = unittest.TextTestRunner(verbosity=2)
test_runner.run(suite)

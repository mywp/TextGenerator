#macbook

from distutils.core import setup

import numpy as np
from Cython.Build import cythonize

numpy_include = np.get_include()

#修改后macos 10.15.6
from Cython.Distutils import build_ext
#修改后macos 10.15.6
class CustomBuildExtCommand(build_ext):
    """build_ext command for use when numpy headers are needed."""
    def run(self):

        # Import numpy here, only when headers are needed
        import numpy

        # Add numpy headers to include_dirs
        self.include_dirs.append(numpy.get_include())

        # Call original build_ext command
        build_ext.run(self)
#原有项目
#setup(ext_modules=cythonize("select_by_kp.pyx"), include_dirs=[numpy_include])

#修改后macos 10.15.6
setup(cmdclass = {'build_ext': CustomBuildExtCommand},include_dirs = [np.get_include()],ext_modules=cythonize("select_by_kp.pyx"))

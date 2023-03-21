# Use the built-in `platform` module to print out the following info:

import platform

placeholder1 = platform.platform()
placeholder2 = platform.python_compiler()
placeholder3 = platform.python_version()
placeholder4 = platform.system()
placeholder5 = platform.release()
placeholder6 = platform.processor()
 
print(f"{'Platform:':>10} {placeholder1}",)  # platform.platform()
print(f"{'Compiler:':>10} {placeholder2}",)  # platform.python_compiler()
print(f"{'Python:':>10} {placeholder3}",)  # platform.python_version()
print(f"{'System:':>10} {placeholder4}",)  # platform.system()
print(f"{'Release:':>10} {placeholder5}",)  # platform.release()
print(f"{'System:':>10} {placeholder6}",)  # platform.processor()


print(f"{'python:':>10} is a good boy")
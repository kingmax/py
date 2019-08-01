import pyblish.api

pyblish.api.register_plugin_path(r'D:\git\py\learn_pyblish\myplugins')

import pyblish.util

context = pyblish.util.publish()
print(context.data)
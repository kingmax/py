import pyblish.api

class MyPlugin(pyblish.api.ContextPlugin):
    def process(self, context):
        print('hello, pyblish')
        

pyblish.api.register_plugin(MyPlugin)

print(MyPlugin.__name__)

import pyblish.util
pyblish.util.publish()
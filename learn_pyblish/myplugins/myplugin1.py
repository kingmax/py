import pyblish.api

########################################################################
class MyPlugin1(pyblish.api.ContextPlugin):
    """"""

    #----------------------------------------------------------------------
    def process(self, context):
        context.create_instance('MyPlugin1', isHero = False)
        print('hello from plugin1')
        

    
    
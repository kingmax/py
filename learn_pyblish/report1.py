import pyblish.api

class CollectCaptainAmerica(pyblish.api.ContextPlugin):
    order = pyblish.api.CollectorOrder

    def process(self, context):
        context.create_instance("Captain America", isHero=False)

class ValidateCaptainAmerica(pyblish.api.InstancePlugin):
    order = pyblish.api.ValidatorOrder

    def process(self, instance):
        # Any raised exception will mark a plug-in as failed
        assert instance.data.get("isHero") == True, "%s must be a hero" % instance

pyblish.api.register_plugin(CollectCaptainAmerica)
pyblish.api.register_plugin(ValidateCaptainAmerica)

import pyblish.util
context = pyblish.util.publish()

'''
results = context.data.get("results")
header = "{:<10}{:<40} -> {}".format("Success", "Plug-in", "Instance")
result = "{success:<10}{plugin.__name__:<40} -> {instance}"
results = "\n".join(result.format(**r) for r in results)
report = """
{header}
{line}
{results}
"""
print(report.format(header=header,
                    results=results,
                    line="-" * 70))
'''

# report2
header = "{:<10}{:<40} -> {}".format("Success", "Plug-in", "Instance")
result = "{success:<10}{plugin.__name__:<40} -> {instance}"
error = "{:<10}+-- EXCEPTION: {:<70}"

results = list()
for r in context.data["results"]:
  results.append(result.format(**r))
  if r["error"]:
    results.append(error.format("", r["error"]))

report = """
{header}
{line}
{results}
"""
print(report.format(header=header,
                    results="\n".join(results),
                    line="-" * 70))
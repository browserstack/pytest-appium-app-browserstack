from paver.easy import *
from paver.setuputils import setup
from multiprocess import Process
import platform
import json

def run_py_test(config, task_id=0):
    if platform.system() == "Windows":
        if(config=="local"):
            sh('cmd /C "set CONFIG_FILE=run-local-test/%s.json && set TASK_ID=%s && pytest -s run-local-test/tests/*.py"' % (config, task_id))
        elif(config == "parallel"): 
            sh('cmd /C "set CONFIG_FILE=run-parallel-test/%s.json && set TASK_ID=%s && pytest -s run-parallel-test/tests/*.py -n 2"' % (config, task_id))
        else: 
            sh('cmd /C "set CONFIG_FILE=run-single-test/%s.json && set TASK_ID=%s && pytest -s run-single-test/tests/*.py"' % (config, task_id))
   
    else:
        if(config=="local"):
            sh('CONFIG_FILE=run-local-test/%s.json TASK_ID=%s pytest -s run-local-test/tests/*.py' % (config, task_id))
        elif(config == "parallel"): 
            sh('CONFIG_FILE=run-parallel-test/%s.json TASK_ID=%s pytest -s run-parallel-test/tests/*.py -n 2' % (config, task_id))
        else:
            sh('CONFIG_FILE=run-single-test/%s.json TASK_ID=%s pytest -s run-single-test/tests/*.py' % (config, task_id))

@task
@consume_nargs(1)
def run(args):
    """Run single, local and parallel test using different config."""
    jobs = []
    config_file = 'run-%s-test/%s.json' % (args[0], args[0])
    with open(config_file) as data_file:
        CONFIG = json.load(data_file)
    environments = CONFIG['environments']
    for i in range(len(environments)):
        p = Process(target=run_py_test, args=(args[0], i))
        jobs.append(p)
        p.start()

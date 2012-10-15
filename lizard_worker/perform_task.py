import os
import logging  # , threading, time, datetime, random, math

from django.conf import settings

log = logging.getLogger('worker.perform_task')

TASK_ADMIN_CREATES_SCENARIO_050 = 50
TASK_COMPUTE_SOBEK_MODEL_120 = 120
TASK_PERFORM_SOBEK_SIMULATION_130 = 130
TASK_COMPUTE_RISE_SPEED_132 = 132
TASK_COMPUTE_MORTALITY_GRID_134 = 134
TASK_SOBEK_PNG_GENERATION_150 = 150
TASK_HISSSM_SIMULATION_160 = 160
TASK_SOBEK_EMBANKMENT_DAMAGE_162 = 162
TASK_HISSSM_PNG_GENERATION_180 = 180
TASK_SOBEK_PRESENTATION_GENERATION_155 = 155
TASK_HISSSM_PRESENTATION_GENERATION_185 = 185
TASK_CALCULATE_STATISTICS = 190


def perform_task(
    scenario_id, tasktype_id, worker_nr, broker_logging_handler=None):
    """
    execute specific task
    scenario_id  = id of scenario
    tasktype_id  = id of tasktype (120,130,132)
    worker_nr = number of worker (1,2,3,4,5,6,7,8). Used for temp
    directory and sobek project.
    broker_logging_handler = sends loggings to broker
    """
    #logging handler
    if broker_logging_handler is not None:
        log.addHandler(broker_logging_handler)
    else:
        log.warning("Broker logging handler does not set.")

    try:
        success = False
        if tasktype_id == TASK_COMPUTE_SOBEK_MODEL_120:
            success = True
            ## success = execute_function(scenario_id, worker_nr, ..)
        else:
            log.warning("selected a '%d' task but don't know what it is" %
                        tasktype_id)
        return success

    except Exception, e:
        from sys import exc_info
        from traceback import format_tb
        (this_exctype, this_value, this_traceback) = exc_info()

        log.warning(''.join(['traceback: \n'] + format_tb(this_traceback)))

        log.error("while executing task %s: '%s(%s)'" %
                  (tasktype_id,  type(e), str(e)))

        return False

import sys
sys.path.append('./IOH-Profiler-HDBO-Comparison')
from wrapper import * 
from Practical_Problems.Practical_Problems_Suite import get_practical_problem
from ioh.iohcpp.logger import Analyzer
from ioh.iohcpp.logger.property import RAWYBEST
from ioh.iohcpp.logger.trigger import ALWAYS, ON_IMPROVEMENT, Each
import numpy as np


dim:int = 12
total_budget:int = 30
doe_size:int = dim
seed:int = 2
algorithm_name:str = "BAxUS_botorch"

# Try to get the Tersoff_potentialC1
problem_instance = get_practical_problem(1124,dim=dim)

# Set up the logger
logger = Analyzer(
    triggers=[ON_IMPROVEMENT, Each(3)],
    additional_properties=[RAWYBEST],
    folder_name=f'./results/{algorithm_name}_{problem_instance.meta_data.name}_{dim}D',
    algorithm_name=algorithm_name,
    algorithm_info="Santoni Implementation",
    store_positions=False
)

# Attach the logger to the problem instance
problem_instance.attach_logger(logger)


# Run the optimization loop
opt = wrapopt(algorithm_name, problem_instance, dim, total_budget, doe_size, seed)
opt.run()

# Detach the logger
problem_instance.detach_logger()

problem_instance.reset()



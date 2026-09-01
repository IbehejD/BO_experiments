import sys
sys.path.append('./IOH-Profiler-HDBO-Comparison')
from wrapper import * 
from Practical_Problems.Practical_Problems_Suite import get_practical_problem
from ioh.iohcpp.logger import Analyzer
from ioh.iohcpp.logger.property import RAWYBEST
from ioh.iohcpp.logger.trigger import ALWAYS, ON_IMPROVEMENT, Each
import numpy as np


dim:int = 24
total_budget:int = 250
doe_size:int = dim
seed:int = 1001
algorithm_name:str = "BO_botorch" # Select from [BO_botorch, HEBO, BAxUS, turbo1, turbom]

# For using the practical problem suite, we need to get the problem instance first
# Problem selection:
# 1121 -> Bench_EPS
# 1122 -> Bench_Pitz-Daily
# 1123 -> Circular_antenna_array
# 1124 -> Frequency_modulated_sound_waves
# 1125 -> Lennard_Jones_Potential
# 1126 -> Spacecraft_trajectory_optimizationC1
# 1127 -> Spacecraft_trajectory_optimizationC2
# 1128 -> Spread_spectrum_radar
# 1129 -> Tersoff_potentialC1
# 1130 -> Windwake

# Set up the logger
logger = Analyzer(
    triggers=[ALWAYS],
    additional_properties=[RAWYBEST],
    folder_name=f'./results/{algorithm_name}_{problem_instance.meta_data.name}_{dim}D',
    algorithm_name=algorithm_name,
    algorithm_info="Santoni (et al.) Implementation",
    store_positions=True
)

logger.add_run_attribute(
    "seed",
    seed,
)

# Attach the logger to the problem instance
problem_instance.attach_logger(logger)


# Run the optimization loop
opt = wrapopt(algorithm_name, problem_instance, dim, total_budget, doe_size, seed)
opt.run()

# Detach the logger
problem_instance.detach_logger()

problem_instance.reset()



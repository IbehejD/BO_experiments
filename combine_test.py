import sys
sys.path.append('./IOH-Profiler-HDBO-Comparison')
from wrapper import * 
from Practical_Problems.Practical_Problems_Suite import get_practical_problem
import numpy as np


dim:int = 12
total_budget:int = 30
doe_size:int = dim
seed:int = 2
algorithm_name:str = "HEBO"

# Try to get the Tersoff_potentialC1
problem_instance = get_practical_problem(1123,dim=dim)
f = problem_instance.evaluate

opt = wrapopt(algorithm_name, f, dim, total_budget, doe_size, seed)
opt.run()


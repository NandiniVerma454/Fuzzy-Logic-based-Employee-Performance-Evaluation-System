import numpy as np
import skfuzzy as fuzz
from skfuzzy import control as ctrl


def evaluate_performance(att, quality, teamwork, task, involvement, wlb):

    # ================= INPUT VARIABLES =================
    attendance = ctrl.Antecedent(np.arange(0, 101, 1), 'attendance')
    quality_var = ctrl.Antecedent(np.arange(0, 11, 1), 'quality')
    teamwork_var = ctrl.Antecedent(np.arange(0, 11, 1), 'teamwork')
    task_var = ctrl.Antecedent(np.arange(0, 11, 1), 'task')
    involvement_var = ctrl.Antecedent(np.arange(0, 11, 1), 'involvement')
    wlb_var = ctrl.Antecedent(np.arange(0, 11, 1), 'wlb')

    performance = ctrl.Consequent(np.arange(0, 101, 1), 'performance')

    # ================= MEMBERSHIP FUNCTIONS =================
    attendance['low'] = fuzz.trimf(attendance.universe, [0, 0, 50])
    attendance['medium'] = fuzz.trimf(attendance.universe, [30, 60, 90])
    attendance['high'] = fuzz.trimf(attendance.universe, [70, 100, 100])

    for var in [quality_var, teamwork_var, task_var, involvement_var, wlb_var]:
        var['low'] = fuzz.trimf(var.universe, [0, 0, 5])
        var['medium'] = fuzz.trimf(var.universe, [3, 6, 9])
        var['high'] = fuzz.trimf(var.universe, [7, 10, 10])

    performance['poor'] = fuzz.trimf(performance.universe, [0, 0, 40])
    performance['average'] = fuzz.trimf(performance.universe, [30, 50, 70])
    performance['good'] = fuzz.trimf(performance.universe, [60, 75, 90])
    performance['excellent'] = fuzz.trimf(performance.universe, [80, 100, 100])

    # ================= RULE BASE (20+) =================
    rules = [

        # Basic rules
        ctrl.Rule(attendance['low'], performance['poor']),
        ctrl.Rule(quality_var['low'], performance['poor']),
        ctrl.Rule(task_var['low'], performance['poor']),

        # Medium conditions
        ctrl.Rule(attendance['medium'] & quality_var['medium'], performance['average']),
        ctrl.Rule(teamwork_var['medium'] & task_var['medium'], performance['average']),
        ctrl.Rule(involvement_var['medium'] & wlb_var['medium'], performance['average']),

        # Good conditions
        ctrl.Rule(attendance['high'] & quality_var['medium'], performance['good']),
        ctrl.Rule(attendance['medium'] & quality_var['high'], performance['good']),
        ctrl.Rule(teamwork_var['high'] & task_var['medium'], performance['good']),
        ctrl.Rule(involvement_var['high'] & wlb_var['medium'], performance['good']),

        # Excellent conditions
        ctrl.Rule(quality_var['high'] & teamwork_var['high'] & task_var['high'], performance['excellent']),
        ctrl.Rule(attendance['high'] & involvement_var['high'], performance['excellent']),
        ctrl.Rule(teamwork_var['high'] & wlb_var['high'], performance['excellent']),
        ctrl.Rule(attendance['high'] & quality_var['high'] & task_var['high'], performance['excellent']),

        # Mixed rules
        ctrl.Rule(attendance['low'] & quality_var['high'], performance['average']),
        ctrl.Rule(attendance['medium'] & involvement_var['high'], performance['good']),
        ctrl.Rule(wlb_var['low'], performance['average']),
        ctrl.Rule(involvement_var['low'], performance['average']),

        # Strong combined rules
        ctrl.Rule(attendance['high'] & quality_var['high'] & teamwork_var['high'], performance['excellent']),
        ctrl.Rule(quality_var['high'] & involvement_var['high'], performance['excellent']),
        ctrl.Rule(task_var['high'] & involvement_var['high'], performance['excellent']),

        # Safety rules
        ctrl.Rule(attendance['low'] & task_var['low'], performance['poor']),
        ctrl.Rule(teamwork_var['low'] & quality_var['low'], performance['poor']),
    ]

    system = ctrl.ControlSystem(rules)
    sim = ctrl.ControlSystemSimulation(system)

    # ================= INPUT VALUES =================
    sim.input['attendance'] = att
    sim.input['quality'] = quality
    sim.input['teamwork'] = teamwork
    sim.input['task'] = task
    sim.input['involvement'] = involvement
    sim.input['wlb'] = wlb

    sim.compute()

    score = sim.output['performance']

    # ================= CATEGORY =================
    if score < 40:
        level = "Poor"
    elif score < 60:
        level = "Average"
    elif score < 80:
        level = "Good"
    else:
        level = "Excellent"

    return score, level
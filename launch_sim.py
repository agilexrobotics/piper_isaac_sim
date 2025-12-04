# launch_sim.py
from isaacsim import SimulationApp

# 設定
config = {"headless": False}
simulation_app = SimulationApp(config)

print("Isaac Sim is running...")

while simulation_app.is_running():
    simulation_app.update()

simulation_app.close()
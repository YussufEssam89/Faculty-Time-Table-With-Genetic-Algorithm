import Data
data = Data.Data()

import Schedule

class Population:
    def __init__(self, size):
        self._size = size
        self._data = data
        self._schedules = []
        for i in range(0, size): self._schedules.append(Schedule.Schedule().initialize())
    def get_schedules(self): return self._schedules

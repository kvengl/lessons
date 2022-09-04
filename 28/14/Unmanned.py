def Unmanned(L, N, track):
    total_time = 0
    total_time_without_stop = 0
    traffic_lights = TrafficLights(N, track)
    for i in range(L):
        if traffic_lights.is_exist_traffic_light(total_time_without_stop) and traffic_lights.get_current_traffic_light(total_time_without_stop).is_red():
            while traffic_lights.get_current_traffic_light(total_time_without_stop).is_red():
                traffic_lights.update()
                total_time += 1
        total_time += 1
        total_time_without_stop += 1
        traffic_lights.update()
    return total_time


class TrafficLights:
    def __init__(self, N, track):
        self.traffic_lights = {}
        for i in range(N):
            [begin_time, red_time, green_time] = track[i]
            self.traffic_lights[begin_time] = TrafficLight(red_time, green_time)

    def is_exist_traffic_light(self, elapsed_time):
        if elapsed_time in self.traffic_lights:
            return True
        return False

    def get_current_traffic_light(self, elapsed_time):
        return self.traffic_lights[elapsed_time]

    def update(self):
        for key in self.traffic_lights:
            self.traffic_lights[key].update()


class TrafficLight:
    def __init__(self, red_time, green_time):
        self.elapsed_time = 0
        self.red_time = red_time
        self.green_time = green_time

    def update(self):
        self.elapsed_time += 1

    def is_red(self):
        if self.elapsed_time % (self.red_time + self.green_time) < self.red_time:
            return True
        return False

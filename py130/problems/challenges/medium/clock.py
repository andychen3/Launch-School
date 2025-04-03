# https://launchschool.com/exercises/433788c7

"""
input:
output:
rules:


DS:


Algo:


"""

class Clock:
    TIME = None

    @classmethod
    def at(cls, hour, minutes=0):
        time = []
        if hour < 10:
            time.append(f"0{hour}")
        else:
            time.append(str(hour))

        if minutes < 10:
            time.append(f"0{minutes}")
        else:
            time.append(str(minutes))

        new_clock = Clock()
        new_clock.TIME = ":".join(time)

        return new_clock.TIME


    def __str__(self):
        print(self.TIME)

    def __add__(self, minutes):
        if not isinstance(minutes, str):
            raise NotImplemented
        
        hours, minute = self.TIME.split(":")
        add_hours, add_minutes = divmod(int(minutes), 60)

        combined_hours = int(hours) + add_hours
        combined_minutes = int(minute) + add_minutes

        return self.at(combined_hours, combined_minutes)


    def __sub__(self, minutes):
        if not isinstance(minutes, int):
            return NotImplemented
        
        pass
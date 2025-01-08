class Time:
    def __init__(self):
        # Initialize the Time object
        self.__hours = int(input("Enter the hours: "))
        self.__minutes = int(input("Enter the minutes: "))
        self.__seconds = int(input("Enter the seconds: "))

    def __add__(self, other):
        # Overload the '+' operator to add two Time objects
        total_seconds = self.__seconds + other.__seconds
        total_minutes = self.__minutes + other.__minutes + (total_seconds // 60)
        total_hours = self.__hours + other.__hours + (total_minutes // 60)

        # Keep time within a 24-hour format
        seconds = total_seconds % 60
        minutes = total_minutes % 60
        hours = total_hours % 24

        # Return the sum as a new Time object
        result_time = Time()
        result_time.__hours = hours
        result_time.__minutes = minutes
        result_time.__seconds = seconds
        return result_time

    def display_time(self):
        # Helper method to display time in hh:mm:ss format
        return f"{self.__hours:02d}:{self._

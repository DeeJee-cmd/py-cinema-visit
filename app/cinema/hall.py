class CinemaHall:

    def __init__(self, hall_number):
        self.number = hall_number

    def movie_session(self, movie_name, customers, cleaning_staff):
        print(f"Movie \"{movie_name}\" starts in hall {self.number}.")
        for customer in customers:
            customer.watch_movie(movie_name)
        print(f"Movie \"{movie_name}\" ended.")
        cleaning_staff.clean_hall(self.number)

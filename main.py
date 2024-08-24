import csv
from fuzzywuzzy import fuzz

class BusRouteFinder:
    def __init__(self):
        self.routes = {}

    def preprocess(self, location):
        return ''.join(e.lower() for e in location if e.isalnum())

    def get_best_match(self, input_location, locations, threshold=70):
        input_processed = self.preprocess(input_location)
        best_match = None
        best_ratio = 0

        for location in locations:
            location_processed = self.preprocess(location)
            ratio = fuzz.partial_ratio(input_processed, location_processed)
            if ratio > best_ratio and ratio >= threshold:
                best_ratio = ratio
                best_match = location

        return best_match, best_ratio

    def add_route(self, route_name, locations):
        self.routes[route_name] = locations

    def find_route(self, current_location, destination):
        print(f"\nSearching for routes from {current_location} to {destination}...")

        current_routes = []
        destination_routes = []

        for route_name, locations in self.routes.items():
            current_match, current_ratio = self.get_best_match(current_location, locations)
            if current_match:
                current_routes.append((route_name, current_match, current_ratio))

            dest_match, dest_ratio = self.get_best_match(destination, locations)
            if dest_match:
                destination_routes.append((route_name, dest_match, dest_ratio))

        if not current_routes:
            print(f"No routes found for the current location '{current_location}'.")
        else:
            print("Possible routes from your current location:")
            for route, match, ratio in current_routes:
                print(f"- Route: {route}, Matched Stop: {match} (Confidence: {ratio}%)")

        if not destination_routes:
            print(f"No routes found for the destination '{destination}'.")
        else:
            print("\nPossible routes to your destination:")
            for route, match, ratio in destination_routes:
                print(f"- Route: {route}, Matched Stop: {match} (Confidence: {ratio}%)")

        direct_routes = set(route for route, _, _ in current_routes) & set(route for route, _, _ in destination_routes)

        if direct_routes:
            print("\nDirect routes available:")
            for route in direct_routes:
                print(f"- {route}")
        else:
            print("\nNo direct routes found. You may need to change buses.")

def load_routes_from_csv(filename):
    finder = BusRouteFinder()
    with open(filename, 'r') as csvfile:
        reader = csv.reader(csvfile)
        for row in reader:
            route_name = row[0]
            locations = row[1:]
            finder.add_route(route_name, locations)
    return finder

def main():
    finder = load_routes_from_csv('bus_routes.csv')
    
    current_location = input("Enter your current location: ")
    destination = input("Enter your destination: ")
    
    finder.find_route(current_location, destination)

if __name__ == "__main__":
    main()
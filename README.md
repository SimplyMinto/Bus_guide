#Bus



1. CSV Data Structure:
   The bus routes are stored in a CSV file (bus_routes.csv). Each line represents a route:
   - The first column is the route name
   - Subsequent columns are the stops on that route

2. Loading Data:
   - The `load_routes_from_csv()` function reads the CSV file.
   - It creates a BusRouteFinder object and adds each route to it.

3. BusRouteFinder Class:
   This class is the core of the system. Here's how it works:

   a) Initialization:
      - The `__init__` method creates an empty dictionary to store routes.

   b) Adding Routes:
      - The `add_route()` method adds a route name and its stops to the routes dictionary.

   c) Preprocessing:
      - The `preprocess()` method cleans up location names by removing non-alphanumeric characters and converting to lowercase.
      - This helps in matching user input to actual stop names, even if there are slight differences.

   d) Matching Locations:
      - The `get_best_match()` method uses fuzzy string matching (from the fuzzywuzzy library) to find the best match for a given location among a list of locations.
      - It returns the best match and a confidence score.

   e) Finding Routes:
      The `find_route()` method is the main functionality:
      - It takes the user's current location and destination as input.
      - For both the current location and destination, it searches all routes to find matching stops.
      - It then displays possible routes from the current location and to the destination.
      - Finally, it identifies and displays any direct routes (routes that contain both the start and end locations).

4. Main Execution:
   - The script loads the routes from the CSV file.
   - It prompts the user for their current location and destination.
   - It then calls the `find_route()` method to search for and display possible routes.

5. Fuzzy Matching:
   - The system uses fuzzy string matching to handle slight variations in input.
   - For example, if a stop is "Central Park" but the user types "central prk", the system can still match it.

6. Output:
   - The system displays possible routes from the current location and to the destination.
   - For each possible route, it shows:
     * The route name
     * The matched stop name
     * A confidence score for the match
   - If there are any direct routes (routes that include both the start and end locations), these are highlighted.

This system is flexible and can handle various routes and locations. It's also forgiving of user input, thanks to the fuzzy matching. The CSV-based data storage makes it easy to update or change the route information without modifying the code.

Would you like me to elaborate on any specific part of the system?

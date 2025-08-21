# Receives a random seed (integer) and a timeinterval(int), returns a list of (seed+timeinterval) closing prices (floats)

from datacleaner import CleanRow
from datetime import timedelta
import bisect

class MarketDataLoader:
    def __init__(self, seed:int, game_length:int, step_size: int):
        self.seed = seed
        self.gamelength = game_length
        self.stepsize = step_size


    def _compute_indices(self, clean_data: list[CleanRow]):
        """
        Returns a list of indices where each index corresponds to a trading day closest
        to every 365 calendar days from the initial date (seed).
        Uses Binary Search
        """

        # start with index and date of seed
        indices = []
        current_index = self.seed
        current_date = clean_data[current_index].date
        
        indices.append(current_index) 
        # we need (gamelength) more trading days
        for _ in range(self.gamelength):
            # the potential date which is exactly stepsize away, might not be in shared trading days though
            target_date = current_date + timedelta(days=self.stepsize)

            # only need to consider days after the last selected day, rest is in the past
            all_dates = [row.date for row in clean_data[current_index:]] 
            
            # Find the position where the target_date could be inserted (binary search)
            # bisect_left gives the leftmost (earliest) position at which an element could be inserted while maintaing a sorted list
            # meaning: this gives the index of the target date, if present. if not, it gives the index of the first trading day that actually exists before that day
            pos = bisect.bisect_left(all_dates, target_date)

            # If pos is 0, the target date is before the first date in the remaining day range (index of first existing trading day = 0)
            # target_date falls before the first available trading day in the remaining data
            # then we fall back to selecting the next day - which might not be step_size away though - this is edge case handling
            if pos == 0:
                closest_index = current_index + 1
            else:
                # Otherwise, check the closest of the two surrounding elements
                prev_date = all_dates[pos - 1]
                next_date = all_dates[pos] if pos < len(all_dates) else None

                # if the earliest we can insert is the end of the list, just use the last entry in the list
                # both edge cases should be avoided by the define_seed_bounds anyway
                if next_date is None:
                    closest_index = len(clean_data) - 1

                
                # exact match, earliest day stepsize away is exactly pos-1 or pos
                if prev_date == target_date:
                    closest_index = current_index + (pos - 1)
                elif next_date == target_date:
                    closest_index = current_index + pos
                # compare the difference between the day before the earliest the target_date could be inserted and the day after
                else:
                    prev_diff = abs((prev_date - target_date).days)
                    next_diff = abs((next_date - target_date).days)
                    
                    # Choose the closest of the two
                    if prev_diff <= next_diff:
                        closest_index = current_index + (pos - 1)
                    else:
                        closest_index = current_index + pos

            if self.stepsize == 1 and closest_index == current_index:
            # Skip to the next day
                closest_index += 1
            # Append the closest index
            indices.append(closest_index)
            current_index = closest_index
            current_date = clean_data[current_index].date
        
        return indices

        # start_index = self.seed
        # end_index = start_index + self.gamelength*self.stepsize +1 #slicing excludes the last index, hence the +1
        # return (start_index, end_index)
    

    def load(self, clean_data:list[CleanRow]) -> list[CleanRow]:
        """
        Returns a slice of cleaned data based on seed and game_length.
        """
        indices = self._compute_indices(clean_data)
        sliced_clean_data = [clean_data[i] for i in indices]

        return sliced_clean_data

    def load_last_day(self, clean_data: list[CleanRow]) -> CleanRow:
        """
        Returns the last entry in the dataset (the final day).
        """
        return clean_data[-1]  # The very last row of the full dataset
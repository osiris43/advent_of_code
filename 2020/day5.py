class Seat:
    def __init__(self, encoded_position):
        self.position = (0, 0)
        self.id = 0
        self.encoded_position = encoded_position
        self.determine_position()

    def determine_position(self):
        encoded_row = self.encoded_position[:7] 
        encoded_col = self.encoded_position[-3:]
        cur_row_floor, cur_col_floor = 0, 0
        cur_row_ceiling = 127
        cur_col_ceiling = 7

        for pos in encoded_row:
            if pos == "F":
                cur_row_ceiling = (cur_row_ceiling + cur_row_floor) // 2
            else:
                cur_row_floor = ((cur_row_ceiling + cur_row_floor) // 2) + 1

        for pos in encoded_col:
            if pos == "L":
                cur_col_ceiling = (cur_col_ceiling + cur_col_floor) // 2
            else:
                cur_col_floor = ((cur_col_ceiling + cur_col_floor) // 2) + 1

        self.position = (cur_row_floor,cur_col_floor)
        self.id = cur_row_floor * 8 + cur_col_floor

def compute_answer():
    with open('boarding_passes.txt') as fp:
        passes = fp.readlines()
        print(passes[0])
        seats = [Seat(x.strip()) for x in passes]
        maxid_seat = max(seats, key=lambda seat: seat.id)
        min_seat = min(seats, key=lambda s: s.id)
        print(f"Max SeatId: {maxid_seat.id}\tEncoded Seat Position: {maxid_seat.encoded_position}")
        print(f"min SeatId: {min_seat.id}\tEncoded Seat Position: {min_seat.encoded_position}")

        previous_seat = min_seat.id
        for seat in sorted(seats, key=lambda s: s.id):
            if seat.id - previous_seat == 2:
                print(f"your seat is {previous_seat + 1}")
            
            previous_seat = seat.id
            




if __name__ == "__main__":
    compute_answer()

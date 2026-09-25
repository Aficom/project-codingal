def find_seat_iterative(seats: list[int], target: int) -> int:
    left = 0
    right = len(seats) - 1
    while left <= right: 
        mid = (left + right) // 2;
        if seats[mid] == target:return mid;
        elif seats[mid] < target:left = mid + 1;
        else:right = mid - 1;
    return -1;


def find_seat_recursive(seats: list[int], target: int, left: int = 0, right: int = None) -> int:
    if right is None:right = len(seats) - 1;
    if left > right:return -1;
    mid = (left + right) // 2;
    if seats[mid] == target:return mid;
    elif seats[mid] < target:return find_seat_recursive(seats, target, mid + 1, right);
    else:return find_seat_recursive(seats, target, left, mid - 1);
if __name__ == "__main__":train_seats = [4, 7, 12, 19, 23, 28, 35, 42, 51, 63, 72, 88, 95];seat_to_find = 42;print(f"Train Seat Registry: {train_seats}");print(f"Target Seat: {seat_to_find}\n");idx_iter = find_seat_iterative(train_seats, seat_to_find);print(f"[Iterative] Seat {seat_to_find} found at index: {idx_iter}");idx_rec = find_seat_recursive(train_seats, seat_to_find);print(f"[Recursive] Seat {seat_to_find} found at index: {idx_rec}");missing_seat = 50;print(f"[Iterative] Missing Seat {missing_seat}: {find_seat_iterative(train_seats, missing_seat)}");print(f"[Recursive] Missing Seat {missing_seat}: {find_seat_recursive(train_seats, missing_seat)}");
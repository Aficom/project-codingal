class BinarySubsetBuilder:
    def __init__(self, items: list):
        self.items = items
        self.n = len(items)
        
    def is_bit_set(self, mask: int, i: int) -> bool:
        """
        Check if the i-th bit is set in the mask (Bit Probe).
        Example: mask = 5 (101 in binary), i = 1 -> checks the middle bit.
        """
        return (mask & (1 << i)) != 0
        
    def get_subset(self, mask: int) -> list:
        """
        Select items from the list using the binary mask.
        """
        subset = []
        for i in range(self.n):
            if self.is_bit_set(mask, i):
                subset.append(self.items[i])
        return subset
        
    def generate_power_set(self) -> list:
        """
        Enumerate all 2^N subsets using binary counting and two loops 
        (implicit outer loop over range, inner loop over items).
        """
        power_set = []
        total_subsets = 1 << self.n  # Equivalent to 2^N
        
        for mask in range(total_subsets):
            subset = self.get_subset(mask)
            power_set.append(subset)
            
        return power_set
        
    @staticmethod
    def bit_difference(a: int, b: int) -> int:
        """
        Compare the bit difference (Hamming distance) between two numbers 
        using the XOR operator (^).
        """
        xor_result = a ^ b
        # Count the number of set bits in the XOR result
        return bin(xor_result).count('1')


# ==========================================
# Example Usage and Walkthrough
# ==========================================
if __name__ == "__main__":
    menu_items = ["Burger", "Fries", "Soda"]
    builder = BinarySubsetBuilder(menu_items)
    
    print(f"--- Generating Power Set for {menu_items} ---")
    print(f"Total items (N): {len(menu_items)} | Total subsets (2^N): {1 << len(menu_items)}\n")
    
    for mask, subset in enumerate(builder.generate_power_set()):
        binary_str = bin(mask)[2:].zfill(len(menu_items))
        print(f"Mask {mask:02d} (Binary: {binary_str}) -> Sub-order: {subset}")
        
    print("\n--- Testing Individual Bit Probe ---")
    # Let's check mask 5 (binary 101) for bit positions
    test_mask = 5
    print(f"Probing mask {test_mask} (binary {bin(test_mask)}):")
    for i in range(len(menu_items)):
        active = builder.is_bit_set(test_mask, i)
        print(f"  Bit {i} ({menu_items[i]}): {'Active (1)' if active else 'Inactive (0)'}")
        
    print("\n--- Comparing Bit Differences ---")
    num1, num2 = 5, 3  # 5 is 101, 3 is 011
    diffs = builder.bit_difference(num1, num2)
    print(f"Number {num1} ({bin(num1)}) and Number {num2} ({bin(num2)}) differ by {diffs} bit(s).")
import sys

def sorter(width, height, length, mass):
    """
    Sorts a package based on its dimensions and mass.
    Parameters: 
        width (int), 
        height (int), 
        length (int), 
        mass (int)
    Returns: "REJECTED", "SPECIAL", or "STANDARD"
    """

    volume = (width * height * length)
    
    bulky = volume >= 1_000_000 or max(width, height, length) >= 150
    heavy = mass >= 20

    if (bulky and heavy):
        return "REJECTED"
    elif(bulky or heavy):
        return "SPECIAL"
    else:
        return "STANDARD"

if __name__ == "__main__":

    args = sys.argv
    if len(args) != 5:
        print("Usage: python sorter.py <width> <height> <length> <mass>")
        sys.exit(1)
    
    w, h, l, m = map(int, args[1:5])
    print(sorter(w, h, l, m))
    
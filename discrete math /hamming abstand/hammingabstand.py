def hammingAbstand(inp1, inp2):
    return sum(c1 != c2 for c1, c2 in zip(inp1, inp2))

def main():
    codes = [
        "000000",
        "000111",
        "011100",
        "101010",
        "110001",
        "110110",
        "101101",
        "011011"
    ]
    
    abstand = []
    print("Hamming Abstände von allen Codewörtern:")
    for i in range(len(codes)):
        for j in range(i + 1, len(codes)):
            inp1 = codes[i]
            inp2 = codes[j]
            dist = hammingAbstand(inp1, inp2)
            abstand.append(dist)
            print(f"{inp1} to {inp2}: Abstand = {dist}")
    
    minAbstand = min(abstand)
    print(f"\nMinimalabstand: {minAbstand}")

main()
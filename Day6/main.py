import os 
import string




def _count_packets(datastream: str) -> int:
    counter = 0
    for i in range(len(datastream)):
        ledger = set()
        for j in range(14):
            if i+j == 1948:
                None
            packet = datastream[i+j]
            if packet in ledger:
                counter = 0
                break
            else:
                ledger.add(packet)
                counter += 1
                if counter == 14:
                    return i+j+1


def main():
    path = os.path.dirname(os.path.realpath(__file__)) + "/input.csv"
    datastream = [line.strip() for line in open(path, "r")][0]
    
    
    index = _count_packets(datastream)
    
    print(index)


if __name__ == "__main__":
    main()
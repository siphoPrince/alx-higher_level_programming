#!/usr/bin/python3
import hidden_4

if __name__ == "__main__":
    Names = dir(hidden_4)
    for nam in Names:
        if nam[:2] != "__":
            print(nam)

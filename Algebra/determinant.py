from typing import List
import numpy as np

class Negative(Exception):
    pass

def get_element(array: List, index: int):
    try:
        element = float(input(f" {index}º element: "))
    except ValueError:
        print(" Error: Enter only numbers.")
        get_element(array, index)
    else:
        array.append(element)

def main():
    print(
    """
    \t===================
    \t*   Determinant   *
    \t*   Calculator    *
    \t===================
    """
    )

    leave = False
    while not leave:
        
        negative = False
        non_integer = False
        
        try:
            rows = cols = int(input("\n Size of square matrix: "))
            if rows < 0:
                raise Negative

        except ValueError:
            non_integer = True
            print(" Must be an integer")

        except Negative:
            negative = True
            print(" Enter a positive integer")

        else:
            if rows > 0:
                print()
                elements = []
                counter: int = 0
                for r in range(rows):
                    line = []
                    for c in range(cols):
                        counter += 1
                        get_element(line, counter)
                    elements.append(line)

                matrix = np.array(elements)
                result = np.linalg.det(matrix)

                print(f"\n {matrix}\n")
                print(" Calculated Determinant: {:.2f}".format(result))
            else:
                print("\n Matrix size can\'t be zero\n Stopping...")

        finally:
            if negative:
                continue
            if non_integer:
                continue

            while True:
                if leave:
                    break

                again = str(input("\n Restart? [y/n/c]: ")).lower()

                if again.startswith("n") or again == "":
                    leave = True
                    break

                elif not again.startswith("y"):
                    if again.startswith("c"):
                        print("""
        ===================
              Credits
        ===================""")
                        print("\n Author: Vinícius Souza Cândido")
                        print(" Year: 2021")
                        print(" Using Python and the Numpy module")
                        continue

                    print(" Enter \"yes\" (y) or \"no\" (n)")
                else:
                    print(
    """
 +===============================+""")
                    break

if __name__ == "__main__":
    main()

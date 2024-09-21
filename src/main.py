import sys
import mounika
import choti
import puppy
import revanth
import praneeth  # Importing Praneeth's details

def print_details(module):
    print(f"Age: {module.age}")
    print(f"School: {module.school}")
    print(f"College: {module.college}")
    print(f"Graduation: {module.graduation}")
    if hasattr(module, 'gender'):  # If gender is available, print it
        print(f"Gender: {module.gender}")
    print("\n")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python main.py <choice>")
        print("M: Mounika")
        print("C: Choti")
        print("P: Puppy")
        print("R: Revanth")
        print("Pr: Praneeth")
        sys.exit(1)

    choice = sys.argv[1]

    if choice == 'M':
        print("Mounika's Details:")
        print_details(mounika)
    elif choice == 'C':
        print("Choti's Details:")
        print_details(choti)
    elif choice == 'P':
        print("Puppy's Details:")
        print_details(puppy)
    elif choice == 'R':
        print("Revanth's Details:")
        print_details(revanth)
    elif choice == 'Pr':  # Handle Praneeth's choice
        print("Praneeth's Details:")
        print_details(praneeth)
    else:
        print("Invalid choice. Please use M, C, P, R, or Pr.")

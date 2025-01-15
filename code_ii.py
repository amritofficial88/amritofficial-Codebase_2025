# by amrit_official
class ArrayOperations:
    def __init__(self):
        self.array = []

    def insert(self, element):
        """Insert an element into the array"""
        self.array.append(element)
        print(f"Element {element} inserted.")

    def delete(self, element):
        """Delete an element from the array"""
        if element in self.array:
            self.array.remove(element)
            print(f"Element {element} deleted.")
        else:
            print(f"Element {element} not found.")

    def search(self, element):
        """Search for an element in the array"""
        if element in self.array:
            index = self.array.index(element)
            print(f"Element {element} found at index {index}.")
            return index
        else:
            print(f"Element {element} not found.")
            return -1

    def update(self, index, element):
        """Update the element at a given index"""
        if 0 <= index < len(self.array):
            old_element = self.array[index]
            self.array[index] = element
            print(f"Element at index {index} updated from {old_element} to {element}.")
        else:
            print("Invalid index.")

    def traverse(self):
        """Traverse and display all elements of the array"""
        print("Array elements:", self.array)


# Example Usage
if __name__ == "__main__":
    arr_ops = ArrayOperations()

    # Insert elements
    arr_ops.insert(10)
    arr_ops.insert(20)
    arr_ops.insert(30)

    # Traverse elements
    arr_ops.traverse()

    # Search for an element
    arr_ops.search(20)

    # Update an element
    arr_ops.update(1, 25)

    # Delete an element
    arr_ops.delete(10)

    # Traverse after deletion
    arr_ops.traverse()

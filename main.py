class TupleConverter:
    def __init__(self, input_tuple):
        self.input_tuple = input_tuple
    
    def convert_to_list(self):
        return list(self.input_tuple)
    
    def display(self):
        converted_list = self.convert_to_list()
        print(f"Tuple: {self.input_tuple}")
        print(f"Converted List: {converted_list}")

# Example usage
if __name__ == "__main__":
    input_tuple = (1, 2, 3, 4, 5)
    converter = TupleConverter(input_tuple)
    converter.display()

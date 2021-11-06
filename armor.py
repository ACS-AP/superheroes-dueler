class Armor:
  def __init__(self, name, max_block):
    '''Instantiate instance properties.
        name: String
        max_block: Integer
    '''
    # TODO: Create instance variables for the values passed in.
    pass

  def block(self):
    # TODO: Return a random value between 0 and the
    # initialized max_block strength.
    pass
 

  if __name__ == "__main__":
  # If you run this file from the terminal
  # this block is executed.
  armor = Armor("Debugging Shield", 10)
  print(armor.name)
  print(armor.block())
class Tree:
  def __init__(self, root = None):
    self.root = root

  def get_element_by_id(self, id):
    nodes_to_check = []
    nodes_to_check.append(self.root)
    current_node = []
    while len(nodes_to_check) > 0:
      current_node = nodes_to_check[0]
      if current_node['id'] == id:
        print('ID matches')
        return current_node
      elif current_node['children']:
        for i in range(len(current_node['children'])):
          nodes_to_check.append(current_node['children'][i])
      nodes_to_check.pop(0)
    print('No ID matches')
    return None

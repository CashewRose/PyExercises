class Bag():

    def __init__(self):
        self.directory = dict()

    def add_child_toy(self, item, child, delivered=False):

        if child in self.directory:
            self.directory[child].append(item)
        else:
            self.directory[child] = [item]

    def remove_child_toy(self, item, child):

        if child in self.directory and item in self.directory[child]:
            self.directory[child].remove(item)
            return f'{child}\'s {item} is no longer in the bag.'
        if child not in self.directory:
            return "We dont have any toys for this child!"
        else:
            return "This child doesn't have that toy to begin with."

    def kids_to_get_toys(self):

        children = list()

        for kid in self.directory.keys():
            children.append(kid)
        
        return children

    def child_is_getting(self, child):

        if child in self.directory:
            child_list = []
            for item in self.directory[child]:
                child_list.append(item)

            return child_list
        else:
            return f'{child} has no toys in this bag.'
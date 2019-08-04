import os.path

class Component:

    def __init__(self, name):
        self.name = name

    def move(self, new_path):
        new_folder = get_path(new_path)
        del self.parent.children[self.name]
        new_folder.children[self.name] = self
        self.parent = new_folder


    def delete(self):
        del self.parent.children[self.name]

class Folder(Component):

    def __init__(self, name):
        super().__init__(name)
        self.children = {}

    def add_child(self, child):
        child.parent = self
        self.children[child.name] = child

    def copy(self, new_path):
        folder = Folder(self.name)
        node = get_path(new_path)
        node.add_child(folder)

        for child in self.children.values():
            current_path = new_path + '/' + self.name
            print(current_path)
            child.copy(current_path)


class File(Component):

    def __init__(self, name, contents):
        super().__init__(name)
        self.contents = contents

    def copy(self, new_path):
       node = get_path(new_path)
       obj = File(self.name, self.contents)
       node.add_child(obj)

root = Folder('')

def get_path(path):
    names = path.split('/')[1:]
    node = root
    for name in names:
        node = node.children[name]
    return node


root = Folder('')
folder1 = Folder('folder1')
root.add_child(folder1)
folder12 = Folder('folder12')
folder123 =Folder('folder123')
file121 = File('file1','nowy')
folder12.add_child(folder123)
folder123.add_child(file121)
folder123.add_child(Folder('folderxxx'))
folder12.add_child(file121)
folder12.copy('/folder1')
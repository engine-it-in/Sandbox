
class CollectionRoot(object):
    """
           Goal:
           Work with messages
    """

    RzdU = '/'
    RzdW = '\\'
    RzdDiskW = ':'

    def __init__(self, disk=None, folder=None):
        self.disk = disk
        self.folder = folder

    def CollectRoot(self, OS):
        OS = 'A'
        quest_end = '2'
        rf = []

        while OS == 'A':
            OS = input('OS *nux [*], Windows [W] or another [A]? ')

            if OS == 'W':
                disk = input('What disk? ')

            while quest_end == '2':

                if OS == '*':
                    rf.append(input('What folder? '))
                    quest_end = input('Is it all [1] or there are more folder [2]? ')
                    if quest_end == '1':
                        self.folder = self.RzdU + self.RzdU.join(rf)
                        break
                    elif quest_end == '2':
                        continue
                elif OS == 'W':
                    rf.append(input('What folder? '))
                    quest_end = input('Is it all [1] or there are more folder [2]? ')
                    if quest_end == '1':
                        self.folder = disk + RzdDiskW + self.RzdW + self.RzdW.join(rf)
                        break
                    elif quest_end == '2':
                        continue
                else:
                    print('I can not work in such cases')
                    break
        return self


z = CollectionRoot()
a = z.CollectRoot('W')
print(a.folder)

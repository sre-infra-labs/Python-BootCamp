class Sorter:
    def __bubble(self, data):
        print('bubble sort')

    def __quick(self, data):
        print('quick sort')
    
    def __call__(self, data):
        if(len(data) > 5):
            return self.__quick(data)
        else:
            return self.__bubble(data)

sort = Sorter()
sort([1, 2, 3, 4, 5, 6])
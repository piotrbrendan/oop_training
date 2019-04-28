class EvenOnly(list):
    def append(self, integer):
        if not isinstance(integer, int):
            raise TypeError("Only integers can be added")
        if integer % 2:
            raise ValueError("Only even numbers can be added")
        super().append(integer)

    def __add__(self,lst):

        for item in lst:
            if not isinstance(item, int):
                raise TypeError("Only integers can be added")
            if item % 2:
                raise ValueError("Only even numbers can be added")

        return super().__add__(lst)

ev_lst = EvenOnly()
ev_lst.append(4)
ev_lst + [6]
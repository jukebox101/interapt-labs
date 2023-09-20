class President:
    def __init__(self, term_num):
        with open("presidents.txt") as file:
            for line in file:
                field_list = line.split(":")
                if term_num == int(field_list[0]):
                    self._term_num = term_num
                    self._last_name = field_list[1]
                    self._first_name = field_list[2]
                    self._birth_date = field_list[3]
                    self._death_date = field_list[4]
                    self._birth_place = field_list[5]
                    self._birth_state = field_list[6]
                    self._term_start_date = field_list[7]
                    self._term_end_date = field_list[8]
                    self._party = field_list[9]

                    break
                else:
                    raise ValueError(f"Invalid term number '{term_num}' passed")
    @property
    def term_num(self):
        return self._term_num
    
    @property
    def last_name(self):
        return self._last_name   
     
    @property
    def first_name(self):
        return self._first_name   
     
    @property
    def birth_date(self):
        return self._birth_date    
    
    @property
    def death_date(self):
        return self._death_date    
    
    @property
    def birth_place(self):
        return self._birth_place    
    
    @property
    def birth_state(self):
        return self._birth_state   
    
    @property
    def term_start_date(self):
        return self._term_start_date    
    
    @property
    def term_end_date(self):
        return self._term_end_date
    
    @property
    def party(self):
        return self._party
    
from schema import CrewResponse


def add_column_with_padding(start_index, column_width, value, res_arr):
    j = 0
    for _ in range(column_width):
        if j < len(value):
            c = value[j]
        else:
            c = ' '
        res_arr[start_index] = c
        start_index += 1
        j += 1
    return start_index


class CliPrinter:
    NAME_HEADER = 'Name'
    CRAFT_HEADER = 'Craft'
    COLUMN_SEP = '|'
    HEADER_SEP = '-'
    NEW_LINE = '\n'

    def __init__(self, crew_response: CrewResponse, max_header_width=200):
        self.crew_response = crew_response
        self.max_header_width = max_header_width

    def get_table(self) -> str:
        people_list = self.crew_response.get_people_by_craft()
        max_name = len(CliPrinter.NAME_HEADER)
        max_craft = len(CliPrinter.CRAFT_HEADER)
        for p in people_list:
            if len(p.name) > self.max_header_width:
                p.name = p.name[:self.max_header_width]
            if len(p.craft) > self.max_header_width:
                p.craft = p.craft[:self.max_header_width]
            if len(p.name) > max_name:
                max_name = len(p.name)
            if len(p.craft) > max_craft:
                max_craft = len(p.craft)

        # Craft has a space after the COLUMN_SEP
        max_craft += 1

        # reserve enough memory
        res_arr = [''] * ((len(people_list)+2)*(max_name+max_craft+3))

        i = 0
        i = self._add_headers(i, max_name, max_craft, res_arr)
        # add lines between headers and values
        i = self._add_row(i, self.HEADER_SEP * max_name, self.HEADER_SEP * (1+max_craft), max_name, max_craft, res_arr)
        # add people
        for p in people_list:
            i = self._add_row(i, p.name, ' ' + p.craft, max_name, max_craft, res_arr)

        return ''.join(res_arr)

    def _add_row(self, start_index, col1_val, col2_val, col1_len, col2_len, res_arr):
        start_index = add_column_with_padding(start_index, col1_len, col1_val, res_arr)
        start_index = add_column_with_padding(start_index, 1, self.COLUMN_SEP, res_arr)
        start_index = add_column_with_padding(start_index, col2_len, col2_val, res_arr)
        start_index = add_column_with_padding(start_index, 1, self.NEW_LINE, res_arr)
        return start_index

    def _add_headers(self, start_index, col1_len, col2_len, res_arr):
        return self._add_row(start_index, self.NAME_HEADER, ' ' + self.CRAFT_HEADER, col1_len, col2_len, res_arr)

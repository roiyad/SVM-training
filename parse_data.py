from single_point import parse


def parse_data(data_file_full_path):
    """ This method parses the data into the final matrix [M x N] - called X matrix.
        and Nx1 vector of classifier results - Y vector.
    """
    median_counter = [0] * 14
    median_value = [0] * 14
    lines_for_later = list()
    vals = dict()
    for i in range(14):
        vals[i] = dict()
    f = open(data_file_full_path)
    final_x_matrix = list()
    final_y_vector = list()
    lines = f.readlines()
    for line in lines:
        if line.find("?") != -1:           # delete rows with blank information
            lines_for_later.append(line)
            continue
        split_line_array = [x.strip() for x in line.split(",")]
        if len(split_line_array) < 15:
            continue
        res = parse(split_line_array)
        section = 0
        for value in split_line_array:
            if section == 14:
                continue
            if value not in vals[section]:
                vals[section][value] = 0
            vals[section][value] += 1
            if vals[section][value] > median_counter[section]:
                median_value[section] = value
                median_counter[section] = vals[section][value]
            section += 1
        final_x_matrix.append(res[0])
        final_y_vector.append(res[1])
    result_of_modify_data = parse_rest_of_the_data(median_value, lines_for_later)
    for i in range(len(result_of_modify_data[0])):
        final_x_matrix.append(result_of_modify_data[0][i])
        final_y_vector.append(result_of_modify_data[1][i])
    return final_x_matrix, final_y_vector


def parse_rest_of_the_data(median_value, lines):
    final_x_matrix = list()
    final_y_vector = list()
    for line in lines:
        split_line_array = [x.strip() for x in line.split(",")]
        if split_line_array[14] == "?":
            continue
        col = 0
        for value in split_line_array:
            if split_line_array[col] == '?':
                split_line_array[col] = median_value[col]
            col += 1
        res = parse(split_line_array)
        final_x_matrix.append(res[0])
        final_y_vector.append(res[1])
    return final_x_matrix, final_y_vector

parse_data("C:\\Users\\roiya\\Downloads\\rnd_velis_ml_test (1)\\data\\adult.data")
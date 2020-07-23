import pyexcel
from desk_generator import generate_desk_locations, generate_desk_data
from meet_generator import generate_meet_data, generate_meet_locations
import constraints as con


if __name__ == '__main__':
    desk_location = generate_desk_locations()
    pyexcel.isave_as(records=desk_location, dest_file_name=f'{con.survey_name}_desk_location.csv')
    desk_data = generate_desk_data(desk_location)
    pyexcel.isave_as(records=desk_data, dest_file_name=f'{con.survey_name}_desk_data.csv')

    meet_location = generate_meet_locations()
    pyexcel.isave_as(records=meet_location, dest_file_name=f'{con.survey_name}_meet_location.csv')
    meet_data = generate_meet_data(meet_location)
    pyexcel.isave_as(records=meet_data, dest_file_name=f'{con.survey_name}_meet_data.csv')





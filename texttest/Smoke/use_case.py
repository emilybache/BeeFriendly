from step_definitions import *

print_html_page("start_page")

select_garden_size("Balcony")
select_flowers(["daisy", "rhododendron"])
submit_garden_quizz()

print_html_page("end_page")
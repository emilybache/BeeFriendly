from step_definitions import *

print_html_page("start_page")

select_garden_size("Balcony")
select_flowers(["azalea", "rhododendron"])
submit_garden_quizz()
wait_for_garden_quizz_response()

print_html_page("end_page")
from step_definitions import *

print_html_page("start_page")

enter_contact_details("Charles Darwin", "charles@example.com")
submit_newsletter()
wait_for_newsletter_response()

print_html_page("end_page")
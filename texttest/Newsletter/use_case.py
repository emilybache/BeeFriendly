from step_definitions import *

enter_contact_details("Charles Darwin", "charles@example.com")
submit_newsletter()
wait_for_newsletter_response()

import os


def run_client(url):
    import step_definitions
    step_definitions.setup(url)
    try:
        if os.path.isfile("use_case.py"):
            exec(compile(open("use_case.py").read(), "use_case.py", 'exec'))
    finally:
        step_definitions.close()


if __name__ == "__main__":
    url = "http://localhost:3000/"
    run_client(url)

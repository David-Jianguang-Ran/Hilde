import project.settings as settings


def debug_print(some_str):
  if settings.DEBUG:
    print("Debug Printout Below\n",some_str)
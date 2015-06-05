from PicrossUI import StateHandler
import logging

root_logger = logging.getLogger('')
ch = logging.StreamHandler()
root_logger.addHandler(ch)
root_logger.setLevel(logging.INFO)


g = StateHandler()
try:
    g.setup()
    g.run_game()
except Exception as e:
    root_logger.exception('Faulted during game execution.')
    raise e
finally:
    g.teardown()

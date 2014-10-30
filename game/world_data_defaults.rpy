init 1 python:
    if persistent.defaults_initialized == None:
        persistent.defaults_initialized = True
        persistent.response_text = False
        persistent.scouted = "park"
        persistent.ftm_early_arrival = True
        
def trace_event(events, agent, status, detail=None):
    event = {"agent": agent, "status": status, "detail": detail}
    events.append(event)
    return event

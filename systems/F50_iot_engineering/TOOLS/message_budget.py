def message_budget(bytes_per_message: int, messages_per_minute: int) -> dict:
    return {"bytes_per_minute": bytes_per_message * messages_per_minute}

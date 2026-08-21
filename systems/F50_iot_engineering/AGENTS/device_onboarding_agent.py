class DeviceOnboardingAgent:
    name = "Device Onboarding Agent"
    def run(self, context: dict) -> dict:
        return {"device_types": context.get("device_types", []), "identity_review": True}

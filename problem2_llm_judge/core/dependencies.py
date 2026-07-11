from problem2_llm_judge.core.config import Settings, get_settings

def get_app_settings() -> Settings:
    # Returns application settings.

    # This function exists so FastAPI dependencies can inject the settings object consistently.
    return get_settings()
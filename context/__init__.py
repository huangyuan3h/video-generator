from dynaconf import Dynaconf

settings = Dynaconf(
    settings_files=["settings.example.toml"],
)


__all__ = ["settings"]
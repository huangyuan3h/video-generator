from dynaconf import Dynaconf

settings = Dynaconf(
    settings_files=["settings.toml"],
)


__all__ = ["settings"]
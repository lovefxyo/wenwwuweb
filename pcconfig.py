import pynecone as pc

class WenwuwebConfig(pc.Config):
    pass

config = WenwuwebConfig(
    app_name="wenwuweb",
    db_url="sqlite:///pynecone.db",
    env=pc.Env.DEV,
)
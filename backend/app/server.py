import uvicorn
import sentry_sdk
from core.settings import settings

sentry_sdk.init(
    dsn="https://609a466cfc984669a638731c185c9cb0@o4504281252233216.ingest.sentry.io/4504282261487616",

    # Set traces_sample_rate to 1.0 to capture 100%
    # of transactions for performance monitoring.
    # We recommend adjusting this value in production,
    traces_sample_rate=1.0,
)


def main() -> None:
    """Entrypoint of the application."""
    uvicorn.run(
        "core.app:get_app",
        workers=settings.WORKERS_COUNT,
        host=settings.HOST,
        port=settings.PORT,
        reload=settings.RELOAD,
        factory=True,
    )


if __name__ == "__main__":
    main()



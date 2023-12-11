import inngest
import os

inngest_client = inngest.Inngest(
    app_id="django_example",
    is_production=os.getenv("ENV") == "production",
)

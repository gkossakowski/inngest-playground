import inngest
import requests

@inngest.create_function(
    fn_id="find_person",
    trigger=inngest.TriggerEvent(event="app/person.find"),
)
def fetch_person(
    ctx: inngest.Context,
    step: inngest.StepSync,
) -> dict:
    person_id = ctx.event.data["person_id"]
    res = requests.get(f"https://swapi.dev/api/people/{person_id}")
    return res.json()

from ninja import NinjaAPI

api = NinjaAPI(urls_namespace="consentbb", version="1.0.0")


@api.get("/add")
def add(request, a: int, b: int):
    return {"result": a + b}

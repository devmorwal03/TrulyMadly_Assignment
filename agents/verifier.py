def verify(results):
    if not results:
        return {"error": "No data found"}

    return {
        "status": "success",
        "data": results
    }
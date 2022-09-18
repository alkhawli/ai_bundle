"""Main execution function."""
# import os

import uvicorn

from ai_bundle.app import app


@app.get("/")
async def root():
    """Defining the function of the root of the fast api."""
    return {"message": "Hello World"}


# and os.getenv("DEBUG", "0") == 1

if __name__ == "__main__":  # pragma: no cover
    uvicorn.run(app, host="0.0.0.0", port=5000, reload=True, debug=True)

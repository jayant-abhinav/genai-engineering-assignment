from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse
from problem2_llm_judge.exceptions import (
    LLMGenerationError,
    ResponseParsingError,
    ResponseValidationError,
)

def register_exception_handlers(app: FastAPI) -> None:
    @app.exception_handler(LLMGenerationError)
    async def llm_error_handler(
        request: Request,
        exc: LLMGenerationError,
    ):
        return JSONResponse(
            status_code=502,
            content={
                "error": "LLMGenerationError",
                "message": str(exc),
            },
        )

    @app.exception_handler(ResponseParsingError)
    async def parsing_error_handler(
        request: Request,
        exc: ResponseParsingError,
    ):
        return JSONResponse(
            status_code=500,
            content={
                "error": "ResponseParsingError",
                "message": str(exc),
            },
        )

    @app.exception_handler(ResponseValidationError)
    async def validation_error_handler(
        request: Request,
        exc: ResponseValidationError,
    ):
        return JSONResponse(
            status_code=500,
            content={
                "error": "ResponseValidationError",
                "message": str(exc),
            },
        )

    @app.exception_handler(Exception)
    async def generic_error_handler(
        request: Request,
        exc: Exception,
    ):
        return JSONResponse(
            status_code=500,
            content={
                "error": "InternalServerError",
                "message": "An unexpected error occurred.",
            },
        )
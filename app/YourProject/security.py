import hashlib
import hmac

from YourProject.settings import settings
from fastapi import HTTPException, Request, Security
from fastapi.security import APIKeyHeader


class GithubApiKeyHeader(APIKeyHeader):
    pass


GithubSignatureHeader = GithubApiKeyHeader(name="X-Hub-Signature-256")
ApiKeyHeader = APIKeyHeader(name="X-Api-Key")


async def valid_github_webhook(
    *, github_signature: str = Security(GithubSignatureHeader), request: Request
):
    if not github_signature:
        raise HTTPException(status_code=401, detail="Unauthorized")
    body = await request.body()
    hash_object = hmac.new(
        settings.API_KEY_WEBHOOK.get_secret_value().encode("utf-8"),
        msg=body,
        digestmod=hashlib.sha256,
    )
    expected_signature = "sha256=" + hash_object.hexdigest()
    if not hmac.compare_digest(expected_signature, github_signature):
        raise HTTPException(status_code=403, detail="Request signatures didn't match!")


def require_api_key(api_key_header: str = Security(ApiKeyHeader)):
    api_key = settings.API_KEY.get_secret_value() if settings.API_KEY else None
    if not api_key or api_key != api_key_header:
        raise HTTPException(
            status_code=401,
            detail="Unauthorized",
        )
    return {}
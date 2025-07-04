# generated by fastapi-codegen:
#   filename:  openapi.yaml
#   timestamp: 2025-06-28T09:07:57+00:00



import argparse
import json
import os
from typing import *
from typing import Union

from autogen.mcp.mcp_proxy import MCPProxy
from autogen.mcp.mcp_proxy.security import APIKeyHeader, BaseSecurity, HTTPBasic

from models import (
    CreatePermitRequest,
    CreatePermitResult,
    DisablePermitRequest,
    DisablePermitResult,
    DisableRequest,
    DisableResult,
    NotifyShopperRequest,
    NotifyShopperResult,
    RecurringDetailsRequest,
    RecurringDetailsResult,
    ScheduleAccountUpdaterRequest,
    ScheduleAccountUpdaterResult,
    ServiceError,
)

app = MCPProxy(
    contact={
        'email': 'developer-experience@adyen.com',
        'name': 'Adyen Developer Experience team',
        'url': 'https://www.adyen.help/hc/en-us/community/topics',
        'x-twitter': 'Adyen',
    },
    description='The Recurring APIs allow you to manage and remove your tokens or saved payment details. Tokens should be created with validation during a payment request.\n\nFor more information, refer to our [Tokenization documentation](https://docs.adyen.com/online-payments/tokenization).\n## Authentication\nYou need an [API credential](https://docs.adyen.com/development-resources/api-credentials) to authenticate to the API.\n\nIf using an API key, add an `X-API-Key` header with the API key as the value, for example:\n\n ```\ncurl\n-H "Content-Type: application/json" \\\n-H "X-API-Key: YOUR_API_KEY" \\\n...\n```\n\nAlternatively, you can use the username and password to connect to the API using basic authentication, for example:\n\n```\ncurl\n-U "ws@Company.YOUR_COMPANY_ACCOUNT":"YOUR_BASIC_AUTHENTICATION_PASSWORD" \\\n-H "Content-Type: application/json" \\\n...\n```\n\n## Versioning\nRecurring API supports [versioning](https://docs.adyen.com/development-resources/versioning) using a version suffix in the endpoint URL. This suffix has the following format: "vXX", where XX is the version number.\n\nFor example:\n```\nhttps://pal-test.adyen.com/pal/servlet/Recurring/v68/disable\n```\n\n## Going live\n\nTo authenticate to the live endpoints, you need an [API credential](https://docs.adyen.com/development-resources/api-credentials) from your live Customer Area.\n\nThe live endpoint URLs contain a prefix which is unique to your company account:\n```\n\nhttps://{PREFIX}-pal-live.adyenpayments.com/pal/servlet/Recurring/v68/disable\n```\n\nGet your `{PREFIX}` from your live Customer Area under **Developers** > **API URLs** > **Prefix**.',
    termsOfService='https://www.adyen.com/legal/terms-and-conditions',
    title='Adyen Recurring API',
    version='68',
    servers=[{'url': 'https://pal-test.adyen.com/pal/servlet/Recurring/v68'}],
)


@app.post(
    '/createPermit',
    description=""" Create permits for a recurring contract, including support for defining restrictions. """,
    tags=['permit_management'],
    security=[
        HTTPBasic(name="None"),
        APIKeyHeader(name="X-API-Key"),
    ],
)
def post_create_permit(body: CreatePermitRequest = None):
    """
    Create new permits linked to a recurring contract.
    """
    raise RuntimeError("Should be patched by MCPProxy and never executed")


@app.post(
    '/disable',
    description=""" Disables stored payment details to stop charging a shopper with this particular recurring detail ID.

For more information, refer to [Disable stored details](https://docs.adyen.com/classic-integration/recurring-payments/disable-stored-details/). """,
    tags=['payment_methods_management'],
    security=[
        HTTPBasic(name="None"),
        APIKeyHeader(name="X-API-Key"),
    ],
)
def post_disable(body: DisableRequest = None):
    """
    Disable stored payment details
    """
    raise RuntimeError("Should be patched by MCPProxy and never executed")


@app.post(
    '/disablePermit',
    description=""" Disable a permit that was previously linked to a recurringDetailReference. """,
    tags=['permit_management'],
    security=[
        HTTPBasic(name="None"),
        APIKeyHeader(name="X-API-Key"),
    ],
)
def post_disable_permit(body: DisablePermitRequest = None):
    """
    Disable an existing permit.
    """
    raise RuntimeError("Should be patched by MCPProxy and never executed")


@app.post(
    '/listRecurringDetails',
    description=""" Lists the stored payment details for a shopper, if there are any available. The recurring detail ID can be used with a regular authorisation request to charge the shopper. A summary of the payment detail is returned for presentation to the shopper.

For more information, refer to [Retrieve stored details](https://docs.adyen.com/classic-integration/recurring-payments/retrieve-stored-details/). """,
    tags=['payment_methods_management'],
    security=[
        HTTPBasic(name="None"),
        APIKeyHeader(name="X-API-Key"),
    ],
)
def post_list_recurring_details(body: RecurringDetailsRequest = None):
    """
    Get stored payment details
    """
    raise RuntimeError("Should be patched by MCPProxy and never executed")


@app.post(
    '/notifyShopper',
    description=""" Sends a request to the issuer so they can inform the shopper about the upcoming recurring payment. This endpoint is used only for local acquiring in India. For more information, refer to [Recurring card payments in India](https://docs.adyen.com/payment-methods/cards/cards-recurring-india). """,
    tags=['notification_service'],
    security=[
        HTTPBasic(name="None"),
        APIKeyHeader(name="X-API-Key"),
    ],
)
def post_notify_shopper(body: NotifyShopperRequest = None):
    """
    Ask issuer to notify the shopper
    """
    raise RuntimeError("Should be patched by MCPProxy and never executed")


@app.post(
    '/scheduleAccountUpdater',
    description=""" When making the API call, you can submit either the credit card information, or the recurring detail reference and the shopper reference:
* If the card information is provided, all the sub-fields for `card` are mandatory.
* If the recurring detail reference is provided, the fields for `shopperReference` and `selectedRecurringDetailReference` are mandatory. """,
    tags=['account_updater_process_scheduling'],
    security=[
        HTTPBasic(name="None"),
        APIKeyHeader(name="X-API-Key"),
    ],
)
def post_schedule_account_updater(body: ScheduleAccountUpdaterRequest = None):
    """
    Schedule running the Account Updater
    """
    raise RuntimeError("Should be patched by MCPProxy and never executed")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="MCP Server")
    parser.add_argument(
        "transport",
        choices=["stdio", "sse", "streamable-http"],
        help="Transport mode (stdio, sse or streamable-http)",
    )
    args = parser.parse_args()

    if "CONFIG_PATH" in os.environ:
        config_path = os.environ["CONFIG_PATH"]
        app.load_configuration(config_path)

    if "CONFIG" in os.environ:
        config = os.environ["CONFIG"]
        app.load_configuration_from_string(config)

    if "SECURITY" in os.environ:
        security_params = BaseSecurity.parse_security_parameters_from_env(
            os.environ,
        )

        app.set_security_params(security_params)

    mcp_settings = json.loads(os.environ.get("MCP_SETTINGS", "{}"))

    app.get_mcp(**mcp_settings).run(transport=args.transport)

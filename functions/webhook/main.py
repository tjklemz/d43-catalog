# -*- coding: utf-8 -*-

#
# Lambda function to handle a Gogs' webhook for updating the catalog
#

from __future__ import print_function
from webhook_handler import WebhookHandler


def handle(event, context):
    try:
        handler = WebhookHandler(event)
        handler.run()
    except Exception as e:
        raise Exception('Bad Request: {0}'.format(e))

    return {
        "success": True,
        "message": "Successfully added {0} ({1}) to the catalog".format(handler.repo_name, handler.commit_id)
    }

from hook_set_updated_at import set_updated_at


def append_hooks(app):
    app.on_update += set_updated_at
    return app

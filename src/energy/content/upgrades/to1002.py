def run_upgrade(setup_context):
    """
    """

    setup_context.runImportStepFromProfile(
        "profile-energy.content:default",
        "plone.app.registry",
        run_dependencies=False,
        purge_old=False,
    )

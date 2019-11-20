def import_catalog(setup_context):
    """
    """

    setup_context.runImportStepFromProfile(
        "profile-energy.content:default",
        "catalog",
        run_dependencies=False,
        purge_old=False,
    )

''' upgrade to 1001 '''


def run_upgrade(setup_context):
    """run_upgrade.

    :param setup_context:
    """
    setup_context.runImportStepFromProfile(
        "profile-energy.content:default",
        "catalog",
        run_dependencies=False,
        purge_old=False,
    )

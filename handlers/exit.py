from ..export.image import ImageExporter
from ..bin import pyluxcore


def handler():
    ImageExporter.cleanup()

    # Workaround for a bug in LuxCore:
    # We have to uninstall the log handler to prevent a crash.
    # https://github.com/LuxCoreRender/LuxCore/issues/29
    pyluxcore.SetLogHandler(None)

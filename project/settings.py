from irekua_dev_settings.settings import *
from selia_templates.settings import *
from selia_about.settings import *


INSTALLED_APPS = (
    SELIA_ABOUT_APPS +
    SELIA_TEMPLATES_APPS +
    IREKUA_BASE_APPS
)


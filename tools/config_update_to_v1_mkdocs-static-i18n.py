"""
mkdocs-static-i18n v0.x config migration script to v1.x.

This is provided as-is, pay special attention to the fact
that if you are using !ENV variables, they will be expanded
and converted in the resulting configuration so you will have
to update them back on your mkdocs.yml.
"""
import sys

from mkdocs.config.defaults import MkDocsConfig
from yaml import Dumper, dump

try:
    mkdocs_config_path = sys.argv[1]
except IndexError:
    mkdocs_config_path = "mkdocs.yml"

mkdocs_config = MkDocsConfig()

with open(mkdocs_config_path, "rb") as config_file:
    mkdocs_config.load_file(config_file)
    #
    if "plugins" not in mkdocs_config:
        raise ValueError(f"missing 'plugins' configuration key, found {mkdocs_config.keys()}")
    for plugin in mkdocs_config["plugins"]:
        if isinstance(plugin, dict) and "i18n" in plugin:
            i18n_config = plugin["i18n"]
            break
    else:
        raise ValueError("missing 'plugins.i18n' configuration!")
    if "languages" not in i18n_config:
        raise ValueError("missing 'plugins.i18n.languages' configuration!")
    # basic check that we are using a v0.x config
    if not isinstance(i18n_config["languages"], dict):
        raise ValueError("your 'plugins.i18n.languages' configuration should be a dict")

    # old config
    default_language_only = i18n_config.get("default_language_only", False)
    default_language = i18n_config["default_language"]
    docs_structure = i18n_config.get("docs_structure", "suffix")
    languages = i18n_config["languages"]
    material_alternate = i18n_config.get("material_alternate", True)
    nav_translations = i18n_config.get("nav_translations", {})
    search_reconfigure = i18n_config.get("search_reconfigure", True)

    # new config
    v1_config = {
        "docs_structure": docs_structure,
        "reconfigure_material": material_alternate,
        "reconfigure_search": search_reconfigure,
        "fallback_to_default": True,
        "languages": [],
    }
    for lang, lang_config in languages.items():
        if lang == "default":
            continue

        new_config = {
            "build": True,
            "default": False,
            "fixed_link": None,
            "link": None,
            "locale": lang,
            "name": None,
            "nav_translations": nav_translations.get(lang, {}),
            "site_name": None,
        }
        # very old lang config as simple str
        if isinstance(lang_config, str):
            new_config["name"] = lang_config
            new_config["default"] = lang == default_language

        # v0.x dict language
        if isinstance(lang_config, dict):
            new_config["build"] = (
                lang_config.get("build", True)
                and not default_language_only
                or lang == default_language
            )
            new_config["name"] = lang_config["name"]
            new_config["default"] = lang_config.get("default", lang == default_language)
            new_config["fixed_link"] = lang_config.get("fixed_link", None)
            new_config["link"] = lang_config.get("link", None)
            new_config["site_name"] = lang_config.get("site_name", None)

        # cleanup useless keys
        for key in list(new_config.keys()):
            if new_config[key] in [None, {}]:
                new_config.pop(key)

        v1_config["languages"].append(new_config)

    # ident two spaces for lists as advertised by mkdocs docs
    #
    class MyDumper(Dumper):
        def increase_indent(self, flow=False, indentless=False):
            return super(MyDumper, self).increase_indent(flow, False)

    print("please update your mkdocs plugins.i18n configuration to:")
    print("-" * 10)
    print(dump({"i18n": v1_config}, Dumper=MyDumper, default_flow_style=False, allow_unicode=True))
#!/usr/bin/env python
import os
import shutil
import yaml
from pathlib import Path


def delete_resources_for_disabled_features():
    script_dir = Path(__file__).resolve().parent
    manifest_path = script_dir / "manifest.yml"

    # The root of the generated project
    project_root = Path.cwd()

    # Load the manifest
    with open(manifest_path, encoding="utf-8") as manifest_file:
        manifest = yaml.safe_load(manifest_file)

    for feature in manifest['features']:
        if ((feature['enabled'] == 'no' and not feature['inverted']) or
           (feature['enabled'] == 'yes' and feature['inverted'])):

            print("removing resources for {} feature {}...".format(
                'enabled' if feature['inverted'] else 'disabled', feature['name']))
            for resource in feature['resources']:
                delete_resource(project_root / resource)

    print("cleanup complete, removing manifest...")
    delete_resource(manifest_path)


def delete_resource(resource):
    if resource.is_file():
        print("removing file: {}".format(resource))
        resource.unlink()
    elif resource.is_dir():
        print("removing directory: {}".format(resource))
        shutil.rmtree(resource)


if __name__ == "__main__":
    delete_resources_for_disabled_features()
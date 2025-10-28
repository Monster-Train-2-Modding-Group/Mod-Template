#!/usr/bin/env python
import os
import shutil
import yaml


def delete_resources_for_disabled_features():
    script_dir = Path(__file__).resolve().parent
    manifest_path = script_dir / "manifest.yml"
    with open(manifest_path) as manifest_file:
        manifest = yaml.load(manifest_file)
        for feature in manifest['features']:
            if ((feature['enabled'] == 'no' and not feature['inverted']) or 
               (feature['enabled'] == 'yes' and feature['inverted'])):
                
                print("removing resources for {} feature {}...".format('enabled' if feature['inverted'] else 'disabled', feature['name']))
                for resource in feature['resources']:
                    delete_resource(resource)
    print("cleanup complete, removing manifest...")
    delete_resource(MANIFEST)


def delete_resource(resource):
    if os.path.isfile(resource):
        print("removing file: {}".format(resource))
        os.remove(resource)
    elif os.path.isdir(resource):
        print("removing directory: {}".format(resource))
        shutil.rmtree(resource)

if __name__ == "__main__":
    delete_resources_for_disabled_features()
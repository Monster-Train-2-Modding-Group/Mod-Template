#!/usr/bin/env python
import os
import shutil
import yaml
from pathlib import Path

MANIFEST_CONTENT = """
features:
  - name: generate_minimal_clan
    enabled: {{cookiecutter.generate_minimal_clan|lower}}
    inverted: false
    resources:
      - {{cookiecutter.__project_slug}}.Plugin/json/relics/basic_artifact.json
      - {{cookiecutter.__project_slug}}.Plugin/json/champions/basic_champion.json
      - {{cookiecutter.__project_slug}}.Plugin/json/clan/clan.json
      - {{cookiecutter.__project_slug}}.Plugin/json/clan/clan_banner.json
      - {{cookiecutter.__project_slug}}.Plugin/json/clan/clan_card_frame.json
      - {{cookiecutter.__project_slug}}.Plugin/json/clan/clan_subtypes.json
      - {{cookiecutter.__project_slug}}.Plugin/json/enhancers/basic_enhancer.json
      - {{cookiecutter.__project_slug}}.Plugin/json/equipment/basic_equipment.json
      - {{cookiecutter.__project_slug}}.Plugin/json/rooms/basic_room.json
      - {{cookiecutter.__project_slug}}.Plugin/json/spells/basic_common.json
      - {{cookiecutter.__project_slug}}.Plugin/json/spells/basic_starter.json
      - {{cookiecutter.__project_slug}}.Plugin/json/units/basic_ability_unit.json
      - {{cookiecutter.__project_slug}}.Plugin/json/units/basic_banner_unit.json
      - {{cookiecutter.__project_slug}}.Plugin/json/units/basic_draft_unit.json
      - {{cookiecutter.__project_slug}}.Plugin/textures/banners/BasicBanner_Disabled.png
      - {{cookiecutter.__project_slug}}.Plugin/textures/banners/BasicBanner_Enabled.png
      - {{cookiecutter.__project_slug}}.Plugin/textures/banners/BasicBanner_Frozen.png
      - {{cookiecutter.__project_slug}}.Plugin/textures/banners/BasicBanner_MapIcon.png
      - {{cookiecutter.__project_slug}}.Plugin/textures/banners/BasicBanner_VisitedDisabled.png
      - {{cookiecutter.__project_slug}}.Plugin/textures/banners/ClanBannerMinimapIcon.png
      - {{cookiecutter.__project_slug}}.Plugin/textures/card_art/BasicAbilityUnit.png
      - {{cookiecutter.__project_slug}}.Plugin/textures/card_art/BasicBannerUnit.png
      - {{cookiecutter.__project_slug}}.Plugin/textures/card_art/BasicCommonSpell.png
      - {{cookiecutter.__project_slug}}.Plugin/textures/card_art/BasicDraftUnit.png
      - {{cookiecutter.__project_slug}}.Plugin/textures/card_art/BasicEquipment.png
      - {{cookiecutter.__project_slug}}.Plugin/textures/card_art/BasicRoom.png
      - {{cookiecutter.__project_slug}}.Plugin/textures/card_art/ChampionA.png
      - {{cookiecutter.__project_slug}}.Plugin/textures/card_art/ChampionAStarter.png
      - {{cookiecutter.__project_slug}}.Plugin/textures/card_borders/BasicCardBorderEquipmentRoom.png
      - {{cookiecutter.__project_slug}}.Plugin/textures/card_borders/BasicCardBorderSpell.png
      - {{cookiecutter.__project_slug}}.Plugin/textures/card_borders/BasicCardBorderUnit.png
      - {{cookiecutter.__project_slug}}.Plugin/textures/character_art/BasicAbilityUnit.png
      - {{cookiecutter.__project_slug}}.Plugin/textures/character_art/BasicBannerUnit.png
      - {{cookiecutter.__project_slug}}.Plugin/textures/character_art/BasicDraftUnit.png
      - {{cookiecutter.__project_slug}}.Plugin/textures/character_art/ChampionA.png
      - {{cookiecutter.__project_slug}}.Plugin/textures/icons/BasicClanCardDraft.png
      - {{cookiecutter.__project_slug}}.Plugin/textures/icons/BasicClanLargeIcon.png
      - {{cookiecutter.__project_slug}}.Plugin/textures/icons/BasicClanMediumIcon.png
      - {{cookiecutter.__project_slug}}.Plugin/textures/icons/BasicClanSilhouetteIcon.png
      - {{cookiecutter.__project_slug}}.Plugin/textures/icons/BasicClanSmallIcon.png
      - {{cookiecutter.__project_slug}}.Plugin/textures/icons/BasicEquipmentIcon.png
      - {{cookiecutter.__project_slug}}.Plugin/textures/icons/BasicRoomIcon.png
      - {{cookiecutter.__project_slug}}.Plugin/textures/icons/Basicstone.png
      - {{cookiecutter.__project_slug}}.Plugin/textures/icons/ChampionA.png
      - {{cookiecutter.__project_slug}}.Plugin/textures/icons/ChampionALocked.png
      - {{cookiecutter.__project_slug}}.Plugin/textures/icons/ChampionAPortrait.png
      - {{cookiecutter.__project_slug}}.Plugin/textures/relic_art/BasicArtifactIcon.png
      - {{cookiecutter.__project_slug}}.Plugin/textures/relic_art/BasicArtifactSmallIcon.png

  - name: basic_mod_setup
    enabled: {{cookiecutter.generate_minimal_clan|lower}}
    inverted: true
    resources:
      - {{cookiecutter.__project_slug}}.Plugin/json/plugin.json
      - {{cookiecutter.__project_slug}}.Plugin/textures/card_art/gas.png

  - name: remove_stubs
    enabled: no
    inverted: false
    resources:
      - {{cookiecutter.__project_slug}}.Plugin/code/CardEffects/STUB
      - {{cookiecutter.__project_slug}}.Plugin/code/CardTraits/STUB
      - {{cookiecutter.__project_slug}}.Plugin/code/RelicEffects/STUB
      - {{cookiecutter.__project_slug}}.Plugin/code/RoomModifiers/STUB
      - {{cookiecutter.__project_slug}}.Plugin/code/StatusEffects/STUB
      - {{cookiecutter.__project_slug}}.Plugin/json/relics/STUB
      - {{cookiecutter.__project_slug}}.Plugin/json/champions/STUB
      - {{cookiecutter.__project_slug}}.Plugin/json/clan/STUB
      - {{cookiecutter.__project_slug}}.Plugin/json/enhancers/STUB
      - {{cookiecutter.__project_slug}}.Plugin/json/equipment/STUB
      - {{cookiecutter.__project_slug}}.Plugin/json/rooms/STUB
      - {{cookiecutter.__project_slug}}.Plugin/json/spells/STUB
      - {{cookiecutter.__project_slug}}.Plugin/json/status_effects/STUB
      - {{cookiecutter.__project_slug}}.Plugin/json/units/STUB
      - {{cookiecutter.__project_slug}}.Plugin/patches/STUB
      - {{cookiecutter.__project_slug}}.Plugin/textures/banners/STUB
      - {{cookiecutter.__project_slug}}.Plugin/textures/card_art/STUB
      - {{cookiecutter.__project_slug}}.Plugin/textures/card_borders/STUB
      - {{cookiecutter.__project_slug}}.Plugin/textures/character_art/STUB
      - {{cookiecutter.__project_slug}}.Plugin/textures/icons/STUB
      - {{cookiecutter.__project_slug}}.Plugin/textures/relic_art/STUB
"""

def delete_resources_for_disabled_features():
    # The root of the generated project
    project_root = Path.cwd()

    # Load the manifest
    manifest = yaml.safe_load(MANIFEST_CONTENT)

    for feature in manifest['features']:
        if ((not feature['enabled'] and not feature['inverted']) or
           (feature['enabled'] and feature['inverted'])):

            #print("removing resources for {} feature {}...".format(
            #    'enabled' if feature['inverted'] else 'disabled', feature['name']))
            for resource in feature['resources']:
                delete_resource(project_root / resource)

    print("project setup successfully!")


def delete_resource(resource):
    if resource.is_file():
        #print("removing file: {}".format(resource))
        resource.unlink()
    elif resource.is_dir():
        #print("removing directory: {}".format(resource))
        shutil.rmtree(resource)


if __name__ == "__main__":
    delete_resources_for_disabled_features()
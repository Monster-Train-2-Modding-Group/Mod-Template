using BepInEx;
using BepInEx.Logging;
using TrainworksReloaded.Core;
using TrainworksReloaded.Core.Extensions;
using System.Reflection
{% if cookiecutter.enable_harmony_patching == 'yes' %}
using HarmonyLib;
{% endif %}

namespace {{cookiecutter.__project_slug}}.Plugin
{
    [BepInPlugin(MyPluginInfo.PLUGIN_GUID, MyPluginInfo.PLUGIN_NAME, MyPluginInfo.PLUGIN_VERSION)]
    [BepInDependency("TrainworksReloaded.Plugin")]
    [BepInDependency("Conductor")]
    public class Plugin : BaseUnityPlugin
    {
        internal static new ManualLogSource Logger { get; private set; } = null!;

        public static void Log(string message)
        {
            var timestamp = DateTime.UtcNow.ToString("HH:mm:ss.ffffff");
            Logger.LogError($"[{timestamp}] {message}");
        }
        
        // Plugin startup logic. This function is automatically called when your plugin initializes
        public void Awake()
        {
            Logger = base.Logger;
            var builder = Railhead.GetBuilder();
            builder.Configure(
                MyPluginInfo.PLUGIN_GUID,
                c =>
                {
                    // Be sure to include any new json files if you add more.
{% if cookiecutter.generate_minimal_clan == 'yes' %}
                    // Please keep the JSON files readable.
                    // That is one <monster/spell/equipment/room>card  or artifact definition per JSON file exactly like it is specified in the example JSON files below.
                    // It helps when something breaks, and needs to be debugged or inspected by others.
                    c.AddMergedJsonFile(
                        "json/global.json",
                        // Clan Definition
                        "json/clan/clan.json",
                        // Required: Clan Map Banner Node definition and Card Pool
                        "json/clan/clan_banner.json",
                        // Optional: Custom Card Border (if removed edit clan.json)
                        "json/clan/clan_card_frame.json",
                        // Optional: Custom Clan Subtypes used by units.
                        "json/clan/clan_subtypes.json",
                        // Required: A Clan Champion with one Upgrade Path.
                        "json/champions/basic_champion.json",
                        // Spell Cards (Starter is required)
                        "json/spells/basic_starter.json",
                        "json/spells/basic_common.json",
                        // Units
                        "json/units/basic_ability_unit.json",
                        "json/units/basic_banner_unit.json",
                        // Non-Banner Unit, draftable as a Battle Reward
                        "json/units/basic_draft_unit.json",
                        // Equipment & Rooms
                        "json/equipment/basic_equipment.json",
                        "json/rooms/basic_room.json",
                        // Shop Upgrades (Enhancer) & Artifacts
                        "json/enhancers/basic_enhancer.json",
                        "json/relics/basic_artifact.json"
                    );
{% else %}
                    c.AddMergedJsonFile(
                        "json/plugin.json",
                        "json/global.json"
                    );
{% endif %}
                }
            );

            // -------------------
            // POST INITIALIZATION
            // -------------------

            // Non-programmers: You do NOT need to edit below this line. Request new triggers, keywords, or status effects on Discord (#mt2-modding):
            // https://discord.com/invite/6qBCCMU8vP
            //
            // Necessary if you need to write:
            //   -> new custom triggers (See Conductor.CharacterTriggerExtensions) and the associated Tutorial in the wiki
            //   -> new tracked value statistics (see Conductor.TrackedValueTypeExtensions) and the associated tutorial
            //   -> new TargetModes (highly prefer that you consider sending a PR to Conductor repo if it is reusuable as these are limited)
            //   -> new Status Effect Triggers (same as above there can only be a limited number of these)
            //
            // If you need to do any post initialization. i.e. Modifying GameObjects to add Components that Trainworks creates for your
            // characters/cards do it here rather than patching the framework
            //
            // Avoid usage of generative AI/LLMs for the above items, again you can request/get guidance for implementing new keywords on discord.

            // This function is called when everything is loaded and ready
            Roundhouse.WhenReady(MyPluginInfo.PLUGIN_GUID,
                ctx =>
                {
                   // Example: Wire a custom CharacterTrigger (Requires Conductor -> using Conductor.Extensions)
                   // var trigger = ctx.GetCharacterTriggerEnum("MyCustomTriggerId");
                   // trigger.SetToTriggerOnCharacterHit(MyEventFunction)

                   // Example: Attach a custom Unity Component to a generated Character GameObject
                   // var myCharacter = ctx.GetCharacterArt("MyCharacterGameObjectId");
                   // myCharacter.AddComponent<MyAdvancedComponent>();
                }
            );

            // ------------------------------------------
            // Tooltip whitelisting (Requires Conductor)
            // ------------------------------------------
            // (1) Uncomment if you have written CardTraitState subclasses that have tooltips. (Requires Conductor)            
            //Conductor.Utilities.SetupTraitTooltips(Assembly.GetExecutingAssembly());

            // (2) Uncomment if you have defined CardEffectBase subclasses that have tooltips to display. (Requires Conductor)
            //Conductor.Utilities.SetupCardEffectTooltips(Assembly.GetExecutingAssembly());

{% if cookiecutter.enable_harmony_patching == 'yes' %}
            // WARNING: Only use Harmony to patch base game classes if absolutely necessary.
            // Harmony patches do tend to be fragile and can easily break when content updates happen.

            // If you need help/guidance implementing an new mechanic please ask in #mt2-modding (rather than use generative AI/LLMs)
            // NEVER patch TrainworksReloaded or Conductor. Use Roundhouse.WhenReady (above) instead.
            var harmony = new Harmony(MyPluginInfo.PLUGIN_GUID);
            harmony.PatchAll();
{% endif %}

            Logger.LogInfo($"Plugin {MyPluginInfo.PLUGIN_GUID} is loaded!");
        }
    }
}

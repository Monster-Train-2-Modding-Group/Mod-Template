# Getting Started

## On usage of AI/LLMs

We strongly discourage usage of generative AI/LLMs to generate JSON content or code wholesale, especially if you are **not proficient** with programming. 

In our experience, AI will routinely:

* Hallucinate APIs/methods/etc that do not exist.
* Bypass native code and conventions.
* Cause perfomance issues, or produce more code than required.
* Produce brittle, brute-forced logic that introduces game-breaking bugs such as corrupting replay or causes hard to trace conflicts among mods.

If you choose to use AI for strictly limit the scope to schema-compliant JSON. Feed it the official JSON schema (https://github.com/Monster-Train-2-Modding-Group/Trainworks-Reloaded/releases/latest/download/schema.json) and documentation(https://github.com/Monster-Train-2-Modding-Group/Trainworks-Reloaded/wiki/Base-Game-Card-Effect-Reference) directly.
Review the code it produced, or avoid it entirely if you can't read code.

Avoid using AI to generate Custom Card Effects/Traits/Status Effects, generally any C# code. If you are not a programmer you can request mechanics be made for you see Getting Help below.

The Monster Train 2 Modding Group will not debug your AI generated mod if it breaks gameplay or causes issues or if it breaks due to a content update (via the game developers or Trainwroks/Conductor updates).

## Recommended Workflow

1. Draft your clan with the Clan Design Spreadsheet found [here](https://github.com/Monster-Train-2-Modding-Group/Trainworks-Reloaded/wiki/Custom-Clan-Design-Guide)
   Flesh out your mechanics, cards, units, and artifacts using the template before you write a single line of code or JSON configuration

2. Share for early feedback in [#mt2-modding](https://discord.com/channels/336546996779483136/1377778943674810368)
Post your completed spreadsheet in #mt2-modding. The community can help identify:
  * Mechanics fully supported out-of-the-box by vanilla data or frameworks (Conductor).
  * Mechanics that require custom code.
  * Potential balance issues, infinites, and know edge cases before you spend time implementing them.

3. Implement by Example

Follow the [official modding tutorials](https://github.com/Monster-Train-2-Modding-Group/Trainworks-Reloaded/wiki). When building cards, artifacts, and status effects, find an existing item in [MonsterTrain2GameData](https://github.com/brandonandzeus/MonsterTrain2GameData) with similar behavior and adapt its structure. This ensures that the item will work with all other game mechanics.

4. Playtest & Review

Once your clan is functional and buildable, share a build in the modding channel. Community playtesters can help verify balance and catch errors prior to public release.

## Getting Help

If your clan mod requires novel mechanics that cannot be achieved with the vanilla codebase and requires new mechanics (effects, keywords, status effects). Please make a request in the #mt2-modding channel [link](https://discord.com/invite/6qBCCMU8vP), we would be happy to provide the code for you or provide guidance on how to best implement the new mechanic.
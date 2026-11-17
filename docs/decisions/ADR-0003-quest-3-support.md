# ADR-0003: Quest 3 and 3S in the first release

- **Status:** Accepted · 2026-11-17 · decided by the owner ("make it available for Quest 3 too"); approach by Claude
- **Bible patch:** P-31 (bible v1.2)

## Context
Bible v1.1 targeted Quest 2 only, with Quest 3/3S as later platform work. The owner wants the game on Quest 3 as well.

What already supports this, as of 17 Nov 2026 on UE 5.8.4:
- The Android manifest already declares `com.oculus.supportedDevices = quest2|questpro|quest3|quest3s` (from Epic's VR template, set in T-0005).
- The engine ships device profiles that match Quest 3 and 3S by headset name (`Meta_Quest_3`, `Meta_Quest_3S` in `Engine/Config/BaseDeviceProfiles.ini`).
- The project uses only core OpenXR. The engine's OpenXR input plugin binds the Oculus Touch interaction profile, and Meta's runtime serves Quest 3's Touch Plus controllers through that profile.

One trap: the engine's Quest 2 profile sets `sg.ShadowQuality=1`, but its Quest 3 and 3S profiles do not. Left alone, Quest 3 would quietly render with different settings from Quest 2.

## Decision
- **One build** (one APK) for Quest 2, 3 and 3S. No separate Quest 3 package or content.
- **Quest 2 is the performance floor.** Every budget in bible section 14 applies to all three headsets.
- **Same settings everywhere until measured.** Project device profiles pin Quest 3 and 3S to the Quest 2 baseline (T-0046). Raising resolution, foveation or effects on Quest 3 is a later, measured change that may never alter gameplay, timing, enemy counts or warning readability.
- **72 Hz on every headset**, the same as Quest 2.
- **Device checks on Quest 3 or 3S** at each hardware gate and before release (T-0047, plus the release tasks).
- **Quest Pro** stays in the manifest from the template but is not a promised target. Decide before store submission (T-0041) whether to keep it.

## Consequences
- Supporting Quest 3 costs device testing, not a port. Someone needs access to a Quest 3 or 3S headset; the build PC has only a Quest 2 today.
- The P-15 deadline still applies to Quest 2. If the Quest 2 cutoff (December 2027) is missed, the release can still go ahead on Quest 3/3S.
- Touch Plus behaviour is expected, not yet verified. If Meta's runtime ever stops serving Touch Plus through the Touch profile, the project needs the Meta XR plugin or a newer engine profile, and the P-15 check in `docs/TOOLCHAIN.md` must be redone.

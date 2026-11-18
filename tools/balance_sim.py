#!/usr/bin/env python3
"""
Balance simulator for Enter The Matricks (bible v1.1, section 5 + bosses).

Deterministic, stdlib-only. Mirrors the heat rules that UCannonComponent
must implement, so design numbers and code can be checked against each other.

Usage:
    python3 tools/balance_sim.py            # print report
    python3 tools/balance_sim.py --check    # exit 1 if any design assertion fails (used in CI)
"""
import argparse
import sys

DT = 0.001  # 1 ms simulation step

# ---- Tuning (keep in sync with Content/ETM/Data and docs/PRODUCT_BIBLE.md §5) ----
FIRE_RATE = 10.0          # shots/s per cannon (P-34)
DAMAGE = 25.0             # (P-34)
WEAK_MULT = 2.0
HEAT_CAP = 100.0
HEAT_PER_SHOT = 1.0       # (P-34) about 100 shots from cold to overheat
PASSIVE_COOL = 18.0       # /s
PASSIVE_DELAY = 0.4       # s since last shot
VENT_COOL = 40.0          # /s, replaces passive while venting (not additive)
OVERHEAT_UNLOCK = 35.0
VENT_DURING_LOCK = False  # v1.1 patch P-01: overheat lock = passive cooling only


class Cannon:
    def __init__(self):
        self.heat = 0.0
        self.locked = False
        self.since_shot = 99.0
        self.cooldown = 0.0
        self.shots = 0

    def step(self, trigger: bool, vent: bool):
        """Advance one DT. Returns True if a shot fired this step."""
        fired = False
        self.cooldown = max(0.0, self.cooldown - DT)
        self.since_shot += DT
        if vent and self.locked and not VENT_DURING_LOCK:
            vent = False
        if vent:
            self.heat = max(0.0, self.heat - VENT_COOL * DT)
        elif self.since_shot >= PASSIVE_DELAY:
            self.heat = max(0.0, self.heat - PASSIVE_COOL * DT)
        if self.locked and self.heat <= OVERHEAT_UNLOCK:
            self.locked = False
        # Venting blocks firing on that cannon (bible §5)
        if trigger and not vent and not self.locked and self.cooldown <= 0.0:
            self.heat += HEAT_PER_SHOT
            self.shots += 1
            self.since_shot = 0.0
            self.cooldown = 1.0 / FIRE_RATE
            fired = True
            if self.heat >= HEAT_CAP:
                self.heat = HEAT_CAP
                self.locked = True
        return fired


def time_to_overheat():
    c = Cannon()
    t = 0.0
    while not c.locked:
        c.step(True, False)
        t += DT
    return t, c.shots


def recovery_time(vent: bool):
    c = Cannon()
    c.heat, c.locked, c.since_shot = HEAT_CAP, True, 0.0
    t = 0.0
    while c.locked:
        c.step(False, vent)
        t += DT
    return t


def sustained_dps(policy: str, seconds=60.0, mult=1.0):
    """policy: 'hold' (trigger held, passive only), 'hold_vent' (vent when locked),
    'burst_vent' (fire until heat>=81 then vent to 0)."""
    c = Cannon()
    venting = False
    t = 0.0
    while t < seconds:
        if policy == "hold":
            c.step(True, False)
        elif policy == "hold_vent":
            c.step(not c.locked, c.locked)
        elif policy == "burst_vent":
            if not venting and c.heat >= HEAT_CAP - HEAT_PER_SHOT * 2:
                venting = True
            if venting and c.heat <= 0.0:
                venting = False
            c.step(not venting, venting)
        t += DT
    return c.shots * DAMAGE * mult / seconds


def window_damage(window_s, cannons=2, accuracy=0.7, mult=WEAK_MULT, start_heat=0.0):
    """Max damage both cannons deal to a weak point in one exposure window."""
    total = 0.0
    for _ in range(cannons):
        c = Cannon()
        c.heat = start_heat
        t = 0.0
        while t < window_s:
            c.step(True, False)
            t += DT
        total += c.shots * DAMAGE * mult * accuracy
    return total


def report():
    lines, failures = [], []

    def check(cond, msg):
        (lines if cond else failures).append(("OK   " if cond else "FAIL ") + msg)

    t_oh, shots_oh = time_to_overheat()
    rec_passive = recovery_time(False)
    rec_vent = recovery_time(True)
    lines.append(f"Time to overheat from cold: {t_oh:.2f}s ({shots_oh} shots, {shots_oh*DAMAGE:.0f} dmg)")
    lines.append(f"Overheat recovery (passive): {rec_passive:.2f}s | (venting): {rec_vent:.2f}s")
    check(9.0 <= t_oh <= 11.0 and 95 <= shots_oh <= 105, "P-34: cold cannon overheats after ~100 shots / ~10 s of continuous fire")

    d_hold = sustained_dps("hold")
    d_hold_vent = sustained_dps("hold_vent")
    d_burst = sustained_dps("burst_vent")
    lines.append(f"Sustained DPS/cannon: hold={d_hold:.1f}  hold+vent-on-lock={d_hold_vent:.1f}  burst+vent={d_burst:.1f}")
    lines.append(f"Theoretical both-cannon peak {2*FIRE_RATE*DAMAGE:.0f} dps vs sustained both-cannon (burst+vent): {2*d_burst:.0f} dps")
    check(d_burst > d_hold, "Bible: alternating bursts + venting outperforms holding the trigger")
    check(d_burst > d_hold_vent * 1.2, "P-01: skilled burst+vent beats 'hold until lock then vent' by >20%")

    # Enemy shots-to-kill (body hits unless noted)
    enemies = {"Shardling": 80, "Needle Drone": 120, "Siphon": 200, "Cradle Bomber": 160,
               "Lance Walker": 320, "Bulwark (body after node)": 480}
    for name, hp in enemies.items():
        n = -(-hp // DAMAGE)
        lines.append(f"  {name:<26} {hp:>4} HP -> {int(n)} body shots ({n/FIRE_RATE:.2f}s one cannon)")
    check(-(-120 // DAMAGE) / FIRE_RATE < 1.5, "Needle Drone killable by one cannon inside its 1.5s telegraph")

    # Bosses (v1.1: all designated boss targets are weak points, x2)
    acc = 0.7
    gb_window = window_damage(4.0, accuracy=acc)
    gb_core = 6500  # P-34
    lines.append(f"Gatebreaker: 4s core window @70% acc both cannons = {gb_window:.0f} dmg -> "
                 f"{gb_core/gb_window:.1f} windows for {gb_core} HP core")
    check(2 <= gb_core / gb_window <= 4, "Gatebreaker core needs 2-4 exposures (not a sponge, not a one-shot)")

    cd_window = window_damage(5.0, accuracy=acc)
    cd_core = 8000  # P-34
    lines.append(f"Conductor: 5s core window @70% acc = {cd_window:.0f} dmg -> "
                 f"{cd_core/cd_window:.1f} windows for {cd_core} HP core (3 node sets = 3 guaranteed windows)")
    check(cd_core / cd_window <= 3.0, "Conductor core killable within its 3 guaranteed node-set exposures at 70% acc")
    cd_window_50 = window_damage(5.0, accuracy=0.5)
    lines.append(f"Conductor at 50% acc: {cd_core/cd_window_50:.1f} windows -> fallback interrupt-reopen required "
                 f"({'YES' if cd_core/cd_window_50 > 3 else 'no'})")

    node_shots = -(-240 // (DAMAGE * WEAK_MULT))
    lines.append(f"Conductor node 240 HP = {int(node_shots)} weak-point shots; 6s pairing window (10s assisted)")

    # Population audit (bible v1.0 claimed 60 non-boss in L1)
    l1 = [8, 6 + 8, 2 + 6 + 2, 3 + 4 + 4, 6 + 2]
    l2 = [6 + 8, 4 + 2 + 4, 3 + 6 + 2, 4]
    lines.append(f"Level 1 non-boss population from storyboard: {sum(l1)} (v1.0 text said 60)")
    lines.append(f"Level 2 pre-boss population from storyboard: {sum(l2)} (v1.0 text said 39)")
    check(sum(l1) == 51, "Level 1 population matches v1.1 text (51)")
    check(sum(l2) == 39, "Level 2 population matches v1.1 text (39)")
    return lines, failures


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--check", action="store_true")
    args = ap.parse_args()
    lines, failures = report()
    print("\n".join(lines))
    if failures:
        print("\n".join(failures))
    if args.check and failures:
        sys.exit(1)


if __name__ == "__main__":
    main()

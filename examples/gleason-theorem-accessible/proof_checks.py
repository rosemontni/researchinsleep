from __future__ import annotations

from dataclasses import dataclass

import sympy as sp


A = sp.Matrix([[1, 0, 0], [0, 0, -1], [0, 1, 0]])  # p-hat
B = sp.Matrix([[0, -1, 0], [1, 0, 0], [0, 0, 1]])  # q-hat


@dataclass(frozen=True)
class CircleCase:
    name: str
    vector: sp.Matrix
    word: str


def apply_word(word: str, vector: sp.Matrix) -> sp.Matrix:
    result = vector
    for ch in word:
        result = {"A": A, "B": B}[ch] * result
    return sp.simplify(result)


def circle_cases() -> list[CircleCase]:
    x, z = sp.symbols("x z")
    x2, y = sp.symbols("x2 y")
    x3, y3 = sp.symbols("x3 y3")
    return [
        CircleCase("x=y", sp.Matrix([x, x, z]), "BAA"),
        CircleCase("x=z", sp.Matrix([x2, y, x2]), "ABBBA"),
        CircleCase("y=z", sp.Matrix([x3, y3, y3]), "BBA"),
        CircleCase("x=-y", sp.Matrix([x, -x, z]), "AAB"),
        CircleCase("x=-z", sp.Matrix([x2, y, -x2]), "ABA"),
        CircleCase("y=-z", sp.Matrix([x3, y3, -y3]), "ABB"),
    ]


def verify_zero_circle_words() -> list[str]:
    lines = []
    for case in circle_cases():
        transformed = apply_word(case.word, case.vector)
        lines.append(f"{case.name}: {case.word} -> {sp.simplify(transformed + case.vector) == sp.zeros(3, 1)}")
    return lines


def verify_intersections() -> list[str]:
    x, y, z = sp.symbols("x y z", real=True)
    eqs_xyz = [
        [sp.Eq(x, y), sp.Eq(x, z), sp.Eq(x**2 + y**2 + z**2, 1)],
        [sp.Eq(x, -y), sp.Eq(x, -z), sp.Eq(x**2 + y**2 + z**2, 1)],
    ]
    sols = []
    for system in eqs_xyz:
        sols.append(sp.solve(system, (x, y, z), dict=True))
    return [
        f"x=y and x=z intersection count: {len(sols[0])}, points: {sols[0]}",
        f"x=-y and x=-z intersection count: {len(sols[1])}, points: {sols[1]}",
    ]


def verify_unique_circle_through_special_points() -> str:
    a = sp.symbols("a", positive=True)
    u = sp.Matrix([a, a, a])
    v = sp.Matrix([a, -a, -a])
    normal = sp.simplify(u.cross(v))
    # normal proportional to (0,1,-1), i.e. plane y=z
    return f"cross(u, v) = {normal}"


def verify_saddle_zero_set_on_xeqy() -> str:
    t, z = sp.symbols("t z", real=True)
    eqs = [
        sp.Eq(2 * t**2 + z**2, 1),
        sp.Eq(t**2, z**2),
    ]
    sols = sp.solve(eqs, (t, z), dict=True)
    return f"saddle zeros on x'=y' circle: {sols}"


def main() -> None:
    print("Quarter-turn words:")
    for line in verify_zero_circle_words():
        print("  ", line)
    print()
    print("Intersection checks:")
    for line in verify_intersections():
        print("  ", line)
    print()
    print("Great circle through u and v:")
    print("  ", verify_unique_circle_through_special_points())
    print()
    print("Saddle zero set on x'=y':")
    print("  ", verify_saddle_zero_set_on_xeqy())


if __name__ == "__main__":
    main()

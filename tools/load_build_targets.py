import sys
import json


targets = set(sys.argv[1:])
print(targets)

MACHINE_TYPE = {
    "linux": "ubuntu-20.04",
    "macos": "macos-10.15",
    "windows": "windows-2019",
}


def get_os(target):
    if "macos" in target:
        return MACHINE_TYPE["macos"]
    if "win" in target:
        return MACHINE_TYPE["windows"]
    return MACHINE_TYPE["linux"]


def get_cibw_build(target):
    if target in {"linux", "macos", "windows"}:
        return ""
    return target


# sdist
if "sdist" in targets:
    print("::set-output name=sdist::true")
else:
    print("::set-output name=sdist::false")

# universal
if "wheels_universal" in targets:
    print("::set-output name=universal::true")
    exit(0)
else:
    print("::set-output name=universal::false")

# wheels
matrix = {"include": []}
for target in targets:
    if not target.startswith("wheels_"):
        continue  # Not implemented
    target = target.replace("wheels_", "")
    item = {"os": get_os(target)}
    if target not in {"linux", "macos", "windows"}:
        item["CIBW_BUILD"] = target
    if "aarch64" in target:
        item["CIBW_ARCH"] = "aarch64"
    matrix["include"].append(item)
print(json.dumps(matrix))
print(f"::set-output name=matrix::{json.dumps(matrix)}")
